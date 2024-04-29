import json
from typing import Optional, List

from pydantic import BaseModel


class DiscordWebhookEmbedImage(BaseModel):
    url: str


class DiscordWebhookEmbedField(BaseModel):
    name: str
    value: str
    inline: Optional[bool] = False


class DiscordWebhookEmbed(BaseModel):
    title: Optional[str] = None
    timestamp: Optional[str] = None
    thumbnail: Optional[DiscordWebhookEmbedImage] = None
    image: Optional[DiscordWebhookEmbedImage] = None
    color: Optional[int] = None
    description: Optional[str] = None
    fields: Optional[List[DiscordWebhookEmbedField]] = []


class DiscordWebhookData(BaseModel):
    content: str
    username: Optional[str] = None
    avatar_url: Optional[str] = None
    tts: Optional[bool] = False
    embeds: Optional[List[DiscordWebhookEmbed]] = []

    @classmethod
    def from_flask_request_body(cls, body: dict) -> "DiscordWebhookData":
        return cls(**body)

    @classmethod
    def from_fastapi_request_body(cls, body: dict) -> "DiscordWebhookData":
        return cls(**body)


class DiscordWebhookAttachment(BaseModel):
    filename: str
    file_type: str
    content: bytes

    @classmethod
    def from_flask_request_files(cls, files: dict) -> List["DiscordWebhookAttachment"]:
        # Will probably only have one key, 'files[0]'
        # ref: https://github.com/Tautulli/Tautulli/blob/d019efcf911b4806618761c2da48bab7d04031ec/plexpy/notifiers.py#L1170
        for key, value in files.items():
            content = value.read()
            yield cls(filename=value.filename, file_type=value.content_type, content=content)


# ref: https://github.com/Tautulli/Tautulli/blob/d019efcf911b4806618761c2da48bab7d04031ec/plexpy/notifiers.py#L1148
class DiscordWebhookIngestor(BaseModel):
    data: DiscordWebhookData
    attachments: Optional[List[DiscordWebhookAttachment]]

    @classmethod
    def from_flask_request(cls, request) -> "DiscordWebhookIngestor":
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
