import os
from pathlib import Path

try:
    # python-dotenv is optional; loading .env in development is convenient
    from dotenv import load_dotenv
    _has_dotenv = True
except Exception:
    _has_dotenv = False


BASE_DIR = Path(__file__).resolve().parent.parent
if _has_dotenv:
    # load .env from project root if present
    load_dotenv(BASE_DIR / ".env")


class Config:
    """Application configuration.

    Values are read from environment variables with sensible defaults for
    local development.
    """
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

    # DATABASE_URL or fallback to SQLite file in `instance/marappi.db`
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{str(BASE_DIR / 'instance' / 'marappi.db')}",
    )

    # Track modifications: default False
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        "SQLALCHEMY_TRACK_MODIFICATIONS", "False"
    ).lower() in ("1", "true", "yes")

    # Debug flag
    DEBUG = os.getenv("FLASK_DEBUG", "0").lower() in ("1", "true", "yes")
