from fastapi import Depends
from src.models.model import Project
from src.repository.project_repository import ProjectRepository
from src.models.request.project_requests import CreateProject, UpdateProject
from src.exceptions.exception import ProjectException

class ProjectService:
    def __init__(self, project_repo: ProjectRepository = Depends()):
        self.project_repo = project_repo
        
    def create_project(self, project_data: CreateProject, user_id: int) -> Project:
        try:
            project = Project(
                name=project_data.name,
                description=project_data.description,
                user_id=user_id
            )
            return self.project_repo.create_project(project)
        except Exception as e:
            raise ProjectException.invalid_project_data()
    
    def update_project(self, project_id: int, project_data: UpdateProject) -> Project:
        update_dict = project_data.model_dump(exclude_unset=True)
        return self.project_repo.update_project(project_id, update_dict)
    
    def get_user_projects(self, user_id: int, skip: int = 0, limit: int = 100) -> list[Project]:
        return self.project_repo.get_user_projects(user_id, skip, limit)
    
    def get_all_user_projects(self, user_id: int) -> list[Project]:
        return self.project_repo.get_all_user_projects(user_id)
    
    def get_project_by_id(self, project_id: int) -> Project:
        return self.project_repo.get_project_by_id(project_id)
    
    def delete_project(self, project_id: int) -> bool:
        return self.project_repo.delete_project(project_id)
        
    def validate_project_ownership(self, project_id: int, user_id: int) -> bool:
        project = self.get_project_by_id(project_id)
        if project.user_id != user_id:
            raise ProjectException.unauthorized_project_access()
        return True