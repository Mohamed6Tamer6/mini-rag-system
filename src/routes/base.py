from fastapi import FastAPI , APIRouter
import os
from helpers.config import get_settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)


@base_router.get("/")
async def welcome_message():

    settings = get_settings()
    
    app_name = settings.APP_NAME
    app_version = settings.VERSION_NAME

    return {
        "welcome": f"Hello Mohamed, welcome to {app_name} v : {app_version}!"
    }
