from fastapi import FastAPI
from app.src.api.bookings_router import router as router_booking

app = FastAPI(debug=True)
app.include_router(router=router_booking)


@app.get("/health", tags=["Health check"])
async def get_health() -> str:
    return "Ok"
