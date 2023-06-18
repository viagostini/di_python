from fastapi import FastAPI

from dependencies import bootstrap_dependencies
from router import router

app = FastAPI()

bootstrap_dependencies()

app.include_router(router)