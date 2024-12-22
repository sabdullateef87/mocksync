class BadRequestException(Exception):
    def __init__(self, name: str):
        self.name = name


class NotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name


class UnauthorizedException(Exception):
    def __init__(self, name: str):
        self.name = name


class ProjectException:
    @staticmethod
    def project_not_found(project_id: int):
        return NotFoundException(f"Project with id {project_id} not found")

    @staticmethod
    def invalid_project_data():
        return BadRequestException("Invalid project data provided")

    @staticmethod
    def unauthorized_project_access():
        return UnauthorizedException("Unauthorized access to project")
