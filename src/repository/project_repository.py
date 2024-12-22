from src.exceptions.exception import ProjectException
from sqlmodel import select
from src.models.model import Project
from src.config.datasource_config import SessionDep


class ProjectRepository:
    def __init__(self, session: SessionDep):  # type: ignore
        self.session = session

    def create_project(self, project: Project) -> Project:
        try:
            self.session.add(project)
            self.session.commit()
            self.session.refresh(project)
            return project
        except Exception:
            raise ProjectException.invalid_project_data()

    def update_project(self, project_id: int, project_data: dict) -> Project:
        db_project = self.session.get(Project, project_id)
        if not db_project:
            raise ProjectException.project_not_found(project_id)

        try:
            for key, value in project_data.items():
                if value is not None:
                    setattr(db_project, key, value)

            self.session.commit()
            self.session.refresh(db_project)
            return db_project
        except Exception:
            raise ProjectException.invalid_project_data()

    def get_user_projects(
        self, user_id: int, skip: int = 0, limit: int = 100
    ) -> list[Project]:
        query = (
            select(Project).where(Project.user_id == user_id).offset(skip).limit(limit)
        )
        return self.session.exec(query).all()

    def get_all_user_projects(self, user_id: int) -> list[Project]:
        query = select(Project).where(Project.user_id == user_id)
        return self.session.exec(query).all()

    def get_project_by_id(self, project_id: int) -> Project:
        project = self.session.get(Project, project_id)
        if not project:
            raise ProjectException.project_not_found(project_id)
        return project

    def delete_project(self, project_id: int) -> bool:
        project = self.session.get(Project, project_id)
        if not project:
            raise ProjectException.project_not_found(project_id)

        try:
            self.session.delete(project)
            self.session.commit()
            return True
        except Exception:
            raise ProjectException.invalid_project_data()
