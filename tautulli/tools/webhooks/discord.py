import json
from typing import Optional, List

from pydantic import BaseModel


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


class DiscordWebhookData(BaseModel):
    """
    Data from a Discord-style webhook
    """
    content: str
    username: Optional[str] = None
    avatar_url: Optional[str] = None
    tts: Optional[bool] = False
    embeds: Optional[List[DiscordWebhookEmbed]] = []

    @classmethod
    def from_flask_request_body(cls, body: dict) -> "DiscordWebhookData":
        """
        Ingest a Discord-style webhook from a Flask request body
        :param body: The body of the Flask request
        :return: Data from the Discord-style webhook
        """
        return cls(**body)

    @classmethod
    def from_fastapi_request_body(cls, body: dict) -> "DiscordWebhookData":
        """
        Ingest a Discord-style webhook from a FastAPI request body
        :param body: The body of the FastAPI request
        :return: Data from the Discord-style webhook
        """
        return cls(**body)


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
        for key, value in files.items():
            content = value.read()
            yield cls(filename=value.filename, file_type=value.content_type, content=content)


# ref: https://github.com/Tautulli/Tautulli/blob/d019efcf911b4806618761c2da48bab7d04031ec/plexpy/notifiers.py#L1148
class DiscordWebhookIngestor(BaseModel):
    """
    An ingestor for Discord-style webhooks from Tautulli
    """
    data: DiscordWebhookData
    attachments: Optional[List[DiscordWebhookAttachment]]

    @classmethod
    def from_flask_request(cls, request) -> "DiscordWebhookIngestor":
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

        data = DiscordWebhookData.from_flask_request_body(body=body)
        attachments = list(DiscordWebhookAttachment.from_flask_request_files(files=files))

        return cls(data=data, attachments=attachments)
