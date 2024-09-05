import os
from pathlib import Path

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "drf_yasg",
    "rest_framework",
    "dj_metersphere",
    "django_filters"
]

BASE_DIR = Path(__file__).resolve().parent
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "dj_metersphere.urls"
SECRET_KEY = "1234567890poiuytrewq"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "dj_metersphere/templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "dj_metersphere/static"),)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "metersphere",
        "USER": os.getenv("MYSQL_ROOT_USER", ""),
        "PASSWORD": os.getenv("MYSQL_ROOT_PASSWORD", ""),
        "HOST": os.getenv("MYSQL_HOST", ""),
        "PORT": os.getenv("MYSQL_PORT", ""),
        "OPTIONS": {
            "init_command": "SET foreign_key_checks = 0;",
        },
    },
}

# celery setting for "MySQL backend does not support timezone-aware datetimes when USE_TZ is False" error.
# DJANGO_CELERY_BEAT_TZ_AWARE = True
USE_TZ = True

DEBUG = True

REST_FRAMEWORK = {
    "UNAUTHENTICATED_USER": None,
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
}
