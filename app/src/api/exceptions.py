from fastapi import HTTPException, status

USER_ALREADY_EXIST = "Пользователь уже существует"
INVALID_USER_DATA = "Неверная почта или пароль"
ACCESS_DENIED = "Доступ запрещен"
TOKEN_NOT_FOUND = "Токен отсутствует"
BAD_JWT_TOKEN = "Данные неверны, либо срок действия токена истек"


UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail=USER_ALREADY_EXIST
)

IncorrectUserDataException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=INVALID_USER_DATA
)

TokenNotFoundException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=TOKEN_NOT_FOUND
)

BadTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=BAD_JWT_TOKEN
)

AccessDeniedException = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail=ACCESS_DENIED
)
