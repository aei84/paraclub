"""
API регистрации пилотов.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/registration",
    tags=["Регистрация"],
)


@router.get("/")
def test():

    return {
        "status": "ok",
    }