from fastapi import FastAPI
from app.src.api.bookings_router import router as router_booking
from app.src.api.auth_router import router as router_users

app = FastAPI()
app.include_router(router=router_users)
app.include_router(router=router_booking)


@app.get("/health", tags=["Health check"])
async def get_health() -> str:
    return "Ok"
