# database/firebase.py
from contextlib import contextmanager
import os
import google.cloud.firestore as firestore
from config.settings import FirebaseSettings

_fb = FirebaseSettings()

@contextmanager
def get_connection():
    if not _fb.project_id or not _fb.creds_path:
        raise RuntimeError("FIREBASE_PROJECT_ID and GOOGLE_APPLICATION_CREDENTIALS are required")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = _fb.creds_path
    db = firestore.Client(project=_fb.project_id)
    try:
        yield db
    finally:
        pass
