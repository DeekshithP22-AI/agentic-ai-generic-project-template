class AppException(Exception):
    """Base application exception"""
    pass


class AuthorizationError(AppException):
    pass


class ConfigurationError(AppException):
    pass
