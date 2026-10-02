import bcrypt

from app.config.config import BCRYPT_SALT_ROUNDS


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=BCRYPT_SALT_ROUNDS)
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
