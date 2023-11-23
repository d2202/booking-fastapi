from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from app.src.api.bookings_router import router as router_booking
from app.src.api.auth_router import router as router_users
from app.src.api.hotels_router import router as router_hotels
from app.src.api.rooms_router import router as rooms_router
from app.src.api.pages_router import router as pages_router
from app.src.api.images_router import router as images_router

from redis import asyncio as aioredis

app = FastAPI()
app.include_router(router=router_users)
app.include_router(router=router_booking)
app.include_router(router=router_hotels)
app.include_router(router=rooms_router)
app.include_router(router=pages_router)
app.include_router(router=images_router)

app.mount("/static", StaticFiles(directory="app/src/static"), "static")

origins = ["http://localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost:6379")
    FastAPICache.init(RedisBackend(redis), prefix="cache")


@app.get("/health", tags=["Health check"])
async def get_health() -> str:
    return "Ok"
