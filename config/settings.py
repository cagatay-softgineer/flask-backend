# config/settings.py
import secrets
from typing       import Optional
from pydantic     import BaseSettings, Field


# ── Per‐backend config classes ────────────────────────────────────────────────

class PostgresSettings(BaseSettings):
    host:     str = Field("localhost", env="POSTGRES_HOST")
    port:     int = Field(5432,        env="POSTGRES_PORT")
    user:     str = Field(...,         env="POSTGRES_USER")
    password: str = Field(...,         env="POSTGRES_PASSWORD")
    db:       str = Field(...,         env="POSTGRES_DB")

    @property
    def url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class SQLiteSettings(BaseSettings):
    path: str = Field("sqlite.db", env="SQLITE_PATH")

    @property
    def url(self) -> str:
        return f"sqlite:///{self.path}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class MySQLSettings(BaseSettings):
    uri: str = Field(..., env="MYSQL_URI",
                    description="e.g. mysql://user:pw@host:3306/dbname")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class MongoSettings(BaseSettings):
    uri: Optional[str] = Field(
        None, env="MONGODB_URI",
        description="e.g. mongodb+srv://user:pw@cluster0.mongodb.net/dbname"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class FirebaseSettings(BaseSettings):
    project_id: str = Field(..., env="FIREBASE_PROJECT_ID")
    creds_path: str = Field(
        ..., env="GOOGLE_APPLICATION_CREDENTIALS",
        description="Path to service-account JSON file"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# ── Core app settings (only these get read on startup) ───────────────────────

class AppSettings(BaseSettings):
    # Select which backend to load; everything else is lazy
    DB_TYPE:       str                = Field("postgres", env="DB_TYPE")
    DATABASE_URL:  Optional[str]      = Field(
        None, env="DATABASE_URL",
        description="One-URL fallback for SQL or Mongo"
    )

    # Your other app‐wide secrets
    JWT_SECRET_KEY: str               = Field(..., env="JWT_SECRET_KEY")
    SALT:           str               = Field(..., env="SALT")
    SECRET_KEY:     str               = Field(default_factory=lambda: secrets.token_hex(16))

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Single entry point for generic settings
settings = AppSettings()
