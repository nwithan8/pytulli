from tautulli.exceptions.base_exception import TautulliException


class JsonException(TautulliException):
    def __init__(self, message: str, body = None):
        super().__init__(message=message)
        self.body = body

    def __str__(self):
        if self.body:
            return f"{self.message} (body: {self.body})"
        return f"{self.message}"

    def __repr__(self):
        if self.body:
            return f"<{self.__class__.__name__}(message={self.message}, body={self.body})>"
        return f"<{self.__class__.__name__}(message={self.message})>"
