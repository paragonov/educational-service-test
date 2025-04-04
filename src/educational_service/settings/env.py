import dj_database_url
from decouple import config
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = config("SECRET_KEY", default="")

DEBUG = config("DEBUG", default="")

DATABASES = {
    "default": dj_database_url.config(
        default=f"postgres://{config("POSTGRES_USER", default="")}:{config("POSTGRES_PASSWORD", default="")}@{config("POSTGRES_HOST", default="")}:5432/{config("POSTGRES_DB", default="")}",
    ),
    'test': {
        'NAME': f"test_{config('POSTGRES_DB')}",
    }
}
