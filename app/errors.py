class APIError(Exception):
    """Base class for API exceptions with a status code and payload."""

    status_code = 400

    def __init__(self, message=None, status_code=None, payload=None):
        super().__init__(message)
        if status_code is not None:
            self.status_code = status_code
        self.message = message or ''
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or {})
        rv['error'] = self.message
        return rv


class NotFoundError(APIError):
    def __init__(self, message='Not found', payload=None):
        super().__init__(message=message, status_code=404, payload=payload)


class BadRequestError(APIError):
    def __init__(self, message='Bad request', payload=None):
        super().__init__(message=message, status_code=400, payload=payload)
