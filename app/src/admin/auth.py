from sqladmin.authentication import AuthenticationBackend
from fastapi.requests import Request
from fastapi.responses import RedirectResponse

from app.src.api.dependencies import get_current_admin_user, get_current_user
from app.src.services.users_service import users_service
from fastapi import status


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]

        access_token = await users_service.login_user(email=email, password=password)
        request.session.update({"token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> RedirectResponse | bool:
        token = request.session.get("token")
        if not token:
            return RedirectResponse(
                request.url_for("admin:login"), status_code=status.HTTP_302_FOUND
            )

        user = await get_current_admin_user(
            current_user=(await get_current_user(token=token))
        )
        if not user:
            return RedirectResponse(
                request.url_for("admin:login"), status_code=status.HTTP_302_FOUND
            )
        return True


authentication_backend = AdminAuth(secret_key="...")
