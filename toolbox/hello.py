from fastapi import APIRouter

router = APIRouter()


@router.get("/fruit/pineapple")
async def pineapple():
    return {"fruit": "thorny"}


@router.get("/fruit/cherry")
async def cherry():
    return {"fruit": "sweet"}


@router.get("/fruit/grapes")
async def grapes():
    return {"fruit": "juicy"}
