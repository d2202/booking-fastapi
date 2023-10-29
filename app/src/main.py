from fastapi import FastAPI, Depends
from .schemas.hotels import GetHotelsRequestArgs

app = FastAPI(debug=True)


@app.get("/health")
async def health() -> str:
    return "Ok"


@app.get("/hotels")
async def get_hotels(request_args: GetHotelsRequestArgs = Depends()) -> str:
    return "Get hotels"
