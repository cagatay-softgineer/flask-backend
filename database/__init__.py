# database/__init__.py
import importlib
from config.settings import settings

_backends = {"postgres", "sqlite", "mysql", "mongodb", "firebase"}
if settings.DB_TYPE not in _backends:
    raise RuntimeError(f"Unsupported DB_TYPE={settings.DB_TYPE!r}, must be one of {_backends}")

_mod = importlib.import_module(f"database.{settings.DB_TYPE}")
get_connection = _mod.get_connection