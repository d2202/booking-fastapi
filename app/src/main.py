from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from sqladmin import Admin

from app.src.admin.auth import authentication_backend
from app.src.api.bookings_router import router as router_booking
from app.src.api.auth_router import router as router_users
from app.src.api.hotels_router import router as router_hotels
from app.src.api.rooms_router import router as rooms_router
from app.src.api.pages_router import router as pages_router
from app.src.api.images_router import router as images_router

from redis import asyncio as aioredis
from app.config import settings
from app.src.admin.admin import UsersAdmin, BookingsAdmin, HotelsAdmin, RoomsAdmin
from app.src.models.db import engine


# Redis behaviour
@asynccontextmanager
async def redis_on_startup(app: FastAPI):
    redis = aioredis.from_url(f"{settings.REDIS_URL}:{settings.REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield


app = FastAPI(lifespan=redis_on_startup)

# main routes config
app.include_router(router=router_users)
app.include_router(router=router_booking)
app.include_router(router=router_hotels)
app.include_router(router=rooms_router)
app.include_router(router=pages_router)
app.include_router(router=images_router)

app.mount("/static", StaticFiles(directory=settings.PATH_TO_STATIC), "static")


# Middlewares
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

# Admin config
admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(UsersAdmin)
admin.add_view(BookingsAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)


# app health endpoint
@app.get("/health", tags=["Health check"])
async def get_health() -> str:
    return "Ok"
