from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.datasource_config import create_db_and_table
from src.router import user_router, auth_router
from src.exception.global_exception_handler import setup_exception_handlers

app = FastAPI()
setup_exception_handlers(app)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router.router)
app.include_router(auth_router.router)

if __name__ == "__main__":
    create_db_and_table()