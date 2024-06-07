from config.settings.base import *  # NOQA

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

STATIC_ROOT = BASE_DIR / "static/"  # NOQA

STATIC_URL = "static/"

MEDIA_ROOT = BASE_DIR / "user_content/"  # NOQA

MEDIA_URL = "user_content/"
