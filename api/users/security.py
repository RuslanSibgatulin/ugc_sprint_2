import jwt
from core.config import config
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

BEARER = HTTPBearer()


async def get_user(user_credentials: HTTPAuthorizationCredentials = Security(BEARER)) -> str:
    payload = jwt.decode(
        jwt=user_credentials.credentials,
        key=config.SECRET_KEY,
        algorithms=[config.HASH_ALGORITHM],
        options={"verify_signature": False},
    )
    user_data = payload.get("sub")
    user_id = user_data.get("user_id")
    return user_id
