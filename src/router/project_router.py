from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.models.request.project_requests import CreateProject, UpdateProject
from src.service.project_service import ProjectService
from src.models.model import Project
from src.exceptions.exception import (
    BadRequestException,
    NotFoundException,
    UnauthorizedException,
)

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("/", response_model=Project)
async def create_project(
    project: CreateProject, user_id: int, project_service: ProjectService = Depends()
):
    try:
        return project_service.create_project(project, user_id)
    except BadRequestException as e:
        raise HTTPException(status_code=400, detail=str(e.name))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/{project_id}", response_model=Project)
async def update_project(
    project_id: int, project: UpdateProject, project_service: ProjectService = Depends()
):
    try:
        return project_service.update_project(project_id, project)
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e.name))
    except BadRequestException as e:
        raise HTTPException(status_code=400, detail=str(e.name))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/user/{user_id}/paginated", response_model=List[Project])
async def get_user_projects_paginated(
    user_id: int,
    skip: int = 0,
    limit: int = 10,
    project_service: ProjectService = Depends(),
):
    try:
        return project_service.get_user_projects(user_id, skip, limit)
    except UnauthorizedException as e:
        raise HTTPException(status_code=401, detail=str(e.name))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/user/{user_id}/all", response_model=List[Project])
async def get_all_user_projects(
    user_id: int, project_service: ProjectService = Depends()
):
    try:
        return project_service.get_all_user_projects(user_id)
    except UnauthorizedException as e:
        raise HTTPException(status_code=401, detail=str(e.name))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{project_id}", response_model=Project)
async def get_project_by_id(
    project_id: int, project_service: ProjectService = Depends()
):
    try:
        return project_service.get_project_by_id(project_id)
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e.name))
    except UnauthorizedException as e:
        raise HTTPException(status_code=401, detail=str(e.name))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/{project_id}")
async def delete_project(project_id: int, project_service: ProjectService = Depends()):
    try:
        project_service.delete_project(project_id)
        return {"message": "Project deleted successfully"}
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e.name))
    except UnauthorizedException as e:
        raise HTTPException(status_code=401, detail=str(e.name))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
