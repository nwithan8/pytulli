import enum
from abc import abstractmethod, ABC
from typing import Union, Optional

from pydantic import BaseModel


class TautulliWebhookTrigger(enum.Enum):
    PLAYBACK_START = "on_play"
    PLAYBACK_STOP = "on_stop"
    PLAYBACK_PAUSE = "on_pause"
    PLAYBACK_RESUME = "on_resume"
    PLAYBACK_ERROR = "on_error"
    TRANSCODE_DECISION_CHANGE = "on_change"
    INTRO_MARKER = "on_intro"
    COMMERCIAL_MARKER = "on_commercial"
    CREDITS_MARKER = "on_credits"
    WATCHED = "on_watched"
    BUFFER_WARNING = "on_buffer"
    USER_CONCURRENT_STREAMS = "on_concurrent"
    USER_NEW_DEVICE = "on_newdevice"
    RECENTLY_ADDED = "on_created"
    PLEX_SERVER_DOWN = "on_intdown"
    PLEX_SERVER_UP = "on_intup"
    PLEX_REMOTE_ACCESS_DOWN = "on_extdown"
    PLEX_REMOTE_ACCESS_UP = "on_extup"
    PLEX_UPDATE_AVAILABLE = "on_pmsupdate"
    TAUTULLI_UPDATE_AVAILABLE = "on_plexpyupdate"
    TAUTULLI_DATABASE_CORRUPT = "on_plexpydbcorrupt"

    @classmethod
    def from_string(cls, trigger: str) -> Union["TautulliWebhookTrigger", None]:
        """
        Get a Tautulli webhook trigger from a string.
        """
        for t in cls:
            if t.value == trigger:
                return t
        return None

    def __str__(self):
        return self.value


class TautulliWebhook(BaseModel, ABC):
    """
    A webhook from Tautulli
    """
    _trigger: Optional[TautulliWebhookTrigger] = None

    def __init__(self, /, **data):
        super().__init__(**data)

    @property
    def trigger(self) -> Union[TautulliWebhookTrigger, None]:
        if not self._trigger:
            self._trigger = self._determine_trigger()

        return self._trigger

    @abstractmethod
    def _determine_trigger(self, **kwargs: dict) -> Union[TautulliWebhookTrigger, None]:
        """
        Determine the trigger of a Tautulli webhook.
        """
        raise NotImplementedError
