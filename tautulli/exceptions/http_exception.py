from logging import Logger

import objectrest

from tautulli.exceptions.base_exception import TautulliException


class HttpException(TautulliException):
    def __init__(self, message: str, status_code: int = None):
        super().__init__(message=message)
        self.status_code = status_code

    def __str__(self):
        return f"{self.message} (status code: {self.status_code})"

    def __repr__(self):
        return f"<{self.__class__.__name__}(message={self.message}, status_code={self.status_code})>"

    @classmethod
    def from_response(cls, response: objectrest.Response, logger: Logger) -> 'HttpException':
        tautulli_error = None

        try:
            data = response.json()
            tautulli_error = data.get('response', {}).get('message', None)
        except:
            logger.error(f"Could not parse JSON from API error response: {response.text}")

        if not tautulli_error:
            return HttpException(status_code=response.status_code, message="No error reason provided by Tautulli.")

        raise HttpException(status_code=response.status_code, message=tautulli_error)
