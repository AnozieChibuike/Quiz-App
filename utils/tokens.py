from datetime import datetime, timedelta
import jwt
from dotenv import load_dotenv
import os
import typing

load_dotenv()

ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
SECRET_KEY: str | None = os.getenv("SECRET_KEY", None)

if not SECRET_KEY:
    raise NotImplementedError(
        "SECRET KEY missing in config, set one now with <SECRET_KEY>"
    )


def generate_token(email: str) -> str:
    payload = {
        "email": email,
        "exp": datetime.utcnow() + timedelta(minutes=10),  # Token expires in 10 minutes
    }
    token: str = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM) # type: ignore[arg-type]
    return token


def verify_token(token: str) -> tuple[dict[str, typing.Any], int, bool]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # type: ignore[arg-type]
        return {"status": "success", "payload": payload}, 200, True
    except jwt.ExpiredSignatureError:
        return {"status": "error", "reason": "code expired"}, 400, False
    except jwt.InvalidTokenError:
        return {"status": "error", "reason": "Invalid token"}, 400, False
    except:
        return {"status": "error", "reason": "Unable to decode the token"}, 400, False
