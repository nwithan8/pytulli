import json
import re
from typing import Optional, List, Union

from pydantic import BaseModel, Field

from tautulli.internal.static import webhook_trigger_pattern
from tautulli.tools.webhooks.base import _TautulliWebhook, TautulliWebhookTrigger


class DiscordWebhookEmbedImage(BaseModel):
    """
    An image from a Discord-style webhook embed
    """
    url: str


class DiscordWebhookEmbedField(BaseModel):
    """
    A field from a Discord-style webhook embed
    """
    name: str
    value: str
    inline: Optional[bool] = False


class DiscordWebhookEmbed(BaseModel):
    """
    An embed from a Discord-style webhook
    """
    title: Optional[str] = None
    timestamp: Optional[str] = None
    thumbnail: Optional[DiscordWebhookEmbedImage] = None
    image: Optional[DiscordWebhookEmbedImage] = None
    color: Optional[int] = None
    description: Optional[str] = None
    fields: Optional[List[DiscordWebhookEmbedField]] = []


class DiscordWebhookAttachment(BaseModel):
    """
    An attachment from a Discord-style webhook
    """
    filename: str
    file_type: str
    content: bytes

    @classmethod
    def from_flask_request_files(cls, files: dict) -> List["DiscordWebhookAttachment"]:
        """
        Ingest a list of files from a Discord webhook Flask request
        :param files: The files from the Flask request
        :return: A list of Discord webhook attachments
        """
        # Will probably only have one key, 'files[0]'
        # ref: https://github.com/Tautulli/Tautulli/blob/d019efcf911b4806618761c2da48bab7d04031ec/plexpy/notifiers.py#L1170
        attachments = []
        for key, value in files.items():
            content = value.read()
            attachments.append(cls(filename=value.filename, file_type=value.content_type, content=content))
        return attachments


class _DiscordWebhookData(BaseModel):
    """
    Data from a Discord-style webhook
    """

    @classmethod
    def from_flask_request_body(cls, body: dict) -> "_DiscordWebhookData":
        """
        Ingest a Discord-style webhook from a Flask request body
        :param body: The body of the Flask request
        :return: Data from the Discord-style webhook
        """
        return cls(**body)

    @classmethod
    def from_fastapi_request_body(cls, body: dict) -> "_DiscordWebhookData":
        """
        Ingest a Discord-style webhook from a FastAPI request body
        :param body: The body of the FastAPI request
        :return: Data from the Discord-style webhook
        """
        return cls(**body)


class PlaybackStateChangeDiscordWebhookData(_DiscordWebhookData):
    """
    Data from a Discord-style webhook for playback state changes
    """
    content: str
    username: Optional[str] = None
    avatar_url: Optional[str] = None
    tts: Optional[bool] = False
    embeds: Optional[List[DiscordWebhookEmbed]] = []

    @classmethod
    def from_flask_request_body(cls, body: dict) -> "PlaybackStateChangeDiscordWebhookData":
        """
        Ingest a Discord-style webhook from a Flask request body
        :param body: The body of the Flask request
        :return: Data from the Discord-style webhook
        """
        return cls(**body)

    @classmethod
    def from_fastapi_request_body(cls, body: dict) -> "PlaybackStateChangeDiscordWebhookData":
        """
        Ingest a Discord-style webhook from a FastAPI request body
        :param body: The body of the FastAPI request
        :return: Data from the Discord-style webhook
        """
        return cls(**body)


class RecentlyAddedDiscordWebhookData(_DiscordWebhookData):
    """
    Data from a Discord-style webhook for recently added media
    """
    media_type: Optional[str] = None
    library_name: Optional[str] = None
    title: Optional[str] = None
    year_: Optional[str] = Field(None, alias='year')
    duration_: Optional[str] = Field(None, alias='duration')
    tagline: Optional[str] = None
    summary: Optional[str] = None
    studio: Optional[str] = None
    directors_: Optional[str] = Field(None, alias='directors')
    actors_: Optional[str] = Field(None, alias='actors')
    genres_: Optional[str] = Field(None, alias='genres')
    plex_id: Optional[str] = None
    critic_rating_: Optional[str] = Field(None, alias='critic_rating')
    audience_rating_: Optional[str] = Field(None, alias='audience_rating')
    poster_url: Optional[str] = None

    @property
    def year(self) -> Union[int, None]:
        return int(self.year_) if self.year_ else None

    @property
    def duration(self) -> Union[int, None]:
        """
        Get the duration of the media in minutes
        """
        if not self.duration_:
            return None

        if ':' not in self.duration_:
            return int(self.duration_)

        hours, minutes = self.duration_.split(':')
        return int(hours) * 60 + int(minutes)

    @property
    def directors(self) -> List[str]:
        return self.directors_.split(', ') if self.directors_ else []

    @property
    def actors(self) -> List[str]:
        return self.actors_.split(', ') if self.actors_ else []

    @property
    def genres(self) -> List[str]:
        return self.genres_.split(', ') if self.genres_ else []

    @property
    def critic_rating(self) -> Union[float, None]:
        return float(self.critic_rating_) if self.critic_rating_ else None

    @property
    def audience_rating(self) -> Union[float, None]:
        return float(self.audience_rating_) if self.audience_rating_ else None

    @classmethod
    def from_flask_request_body(cls, body: dict) -> "RecentlyAddedDiscordWebhookData":
        """
        Ingest a Discord-style webhook from a Flask request body
        :param body: The body of the Flask request
        :return: Data from the Discord-style webhook
        """
        return cls(**body)

    @classmethod
    def from_fastapi_request_body(cls, body: dict) -> "RecentlyAddedDiscordWebhookData":
        """
        Ingest a Discord-style webhook from a FastAPI request body
        :param body: The body of the FastAPI request
        :return: Data from the Discord-style webhook
        """
        return cls(**body)


# ref: https://github.com/Tautulli/Tautulli/blob/d019efcf911b4806618761c2da48bab7d04031ec/plexpy/notifiers.py#L1148
class DiscordWebhook(_TautulliWebhook):
    """
    A Discord-style webhook from Tautulli
    """
    data: Optional[_DiscordWebhookData] = None
    attachments: Optional[List[DiscordWebhookAttachment]] = []

    @classmethod
    def from_flask_request(cls, request) -> "DiscordWebhook":
        """
        Ingest a Discord-style webhook from a Flask request

        :param request: The incoming Flask request
        :return: The processed Discord-style webhook
        """
        try:
            body = request.get_json()
        except Exception:
            # JSON data is stored in the form field 'payload_json' if files are present
            # ref: https://github.com/Tautulli/Tautulli/blob/d019efcf911b4806618761c2da48bab7d04031ec/plexpy/notifiers.py#L1225
            body = json.loads(request.form.get('payload_json', '{}'))

        files = request.files
        attachments: List[DiscordWebhookAttachment] = DiscordWebhookAttachment.from_flask_request_files(files=files)

        # Determine how to parse the data based on the webhook trigger
        keys = body.keys()
        if 'content' in keys:
            data = PlaybackStateChangeDiscordWebhookData.from_flask_request_body(body=body)
        elif 'plex_id' in keys:
            data = RecentlyAddedDiscordWebhookData.from_flask_request_body(body=body)
        else:
            data = None

        return cls(data=data, attachments=attachments)

    def _determine_trigger(self, **kwargs) -> Union[TautulliWebhookTrigger, None]:
        """
        Determine the trigger of a Discord-style webhook.

        :param kwargs: The arguments to determine the trigger
        :return: The Discord-style webhook trigger
        """
        if isinstance(self.data, RecentlyAddedDiscordWebhookData):
            return TautulliWebhookTrigger.RECENTLY_ADDED

        if isinstance(self.data, PlaybackStateChangeDiscordWebhookData):
            # Couldn't parse webhook data
            if not self.data or not self.data.content:
                return None

            text = self.data.content
            if not text:
                return None

            match = re.search(webhook_trigger_pattern, text)

            if not match:
                return None

            trigger = match.group(1)
            return TautulliWebhookTrigger.from_string(trigger=trigger)

        return None
