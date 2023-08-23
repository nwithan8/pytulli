class TautulliException(Exception):
    def __init__(self, message: str):
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        return f"{self.message}"

    def __repr__(self):
        return f"<{self.__class__.__name__}(message={self.message})>"
