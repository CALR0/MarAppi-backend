class Config:
    """Application configuration.

    Uses a local SQLite database `marappi.db` by default.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///marappi.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
