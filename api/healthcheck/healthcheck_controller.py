from fastapi import FastAPI
from core.configs.env import get_settings
from core.utils.response import response_success
from core.utils.application import create_fastapi

settings = get_settings()

healthcheck_route: str = f"{settings.api_prefix}/healthcheck"
healthcheck_app = FastAPI(root_path=healthcheck_route)


@healthcheck_app.get("/")
def health_check():
    
    return response_success("Health check is good")
