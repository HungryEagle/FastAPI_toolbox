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


@router.get("/fruit/watermelon")
async def watermelon():
    return {"fruit": "watery"}


@router.get("/fruit/blueberry")
async def blueberry():
    return {"fruit": "sour"}
