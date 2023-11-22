from fastapi import FastAPI
from app.src.api.bookings_router import router as router_booking
from app.src.api.auth_router import router as router_users
from app.src.api.hotels_router import router as router_hotels
from app.src.api.rooms_router import router as rooms_router
from app.src.api.pages_router import router as pages_router

app = FastAPI()
app.include_router(router=router_users)
app.include_router(router=router_booking)
app.include_router(router=router_hotels)
app.include_router(router=rooms_router)
app.include_router(router=pages_router)


@app.get("/health", tags=["Health check"])
async def get_health() -> str:
    return "Ok"
