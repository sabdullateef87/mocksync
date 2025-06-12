from typing import Any, Dict

class BaseCustomException(Exception):
    def __init__(self, message: str, status_code: int = 500, details: Dict[str, Any] = None):
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)

# Example custom exceptions
class UserNotFoundException(BaseCustomException):
    def __init__(self, user_id: str):
        super().__init__(
            message=f"User with ID {user_id} not found",
            status_code=404,
            details={"user_id": user_id}
        )

class InsufficientPermissionsException(BaseCustomException):
    def __init__(self, required_role: str):
        super().__init__(
            message="Insufficient permissions",
            status_code=403,
            details={"required_role": required_role}
        )

class ValidationException(BaseCustomException):
    def __init__(self, validation_errors: Dict[str, str]):
        super().__init__(
            message="Validation failed",
            status_code=422,
            details={"errors": validation_errors}
        )
        
class DuplicateException(BaseCustomException):
    def __init__(self, validation_errors: Dict[str, str]):
        super().__init__(
            message="Duplicate failed",
            status_code=409,
            details={"errors": validation_errors}
        )

class BadRequestException(BaseCustomException):
    def __init__(self, message: str, status_code: int, validation_errors: Dict[str, str]):
        super().__init__(
            message=message or "Bad Request",
            status_code=status_code or 400,
            details={"errors": validation_errors}
        )
        
        
