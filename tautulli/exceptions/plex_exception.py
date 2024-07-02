from tautulli.exceptions.base_exception import TautulliException


class PlexException(TautulliException):
    def __init__(self, message: str):
        super().__init__(message=message)
