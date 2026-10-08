from pathlib import Path
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qsl

load_dotenv()

# BASE_DIR representa el directorio raiz del proyecto y se puede construir rutas relacionadas.
BASE_DIR = Path(__file__).resolve().parent.parent

# 06_Django_Architectura_y_Configuracion.ipynb
# powershell  >>>  python manage.py runserver

# Quick-start development settings - unsuitable for production
# See ...

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n*4s9vs50)o(=g=4zkm7!sjc#c!nsoizob_)3(xd62c!#%9=+l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not bool(os.getenv("VERCEL"))

# Estos hostes estan permitidos para desarrollo local y para que despliegue en Vercel
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "kai-3-d2dfatbr3-kai-3-d.vercel.app", 
    "kai-3-d.vercel.app"]

# Definicion de aplicacion
# 06_Django_Architectura_y_Configuracion.ipynb

INSTALLED_APPS = [
    # Cosas que Django trae preinstaladas de fabrica (Seguridad, Admin...)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # TU APP PROPIA VA AQUI!!!!!! 
    'kai3d_app', # Esto es la aplicacion
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kai3d_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kai3d_core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

# tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.1/howto/static-files/


# Configura las rutas de estaticos para produccion
# URL para acceder a los archivos estaticos
STATIC_URL = '/static/'

LOGIN_URL = 'login'

# Carpeta donde Django recopilara los archivos estaticos para produccion
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

ES_VERCEL = bool(os.getenv("VERCEL"))

# Registro de eventos de KAI 3D
LOGGING ={
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "INFO",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "kai3d.log",
            "formatter": "simple",
            "level": "INFO",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "kai3d_app": {
            "handlers": ["console"] if os.getenv("VERCEL") else ["file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

# En Vercel no se puede escribir en la carpeta del proyecto.
# Eliminamos el manejador de archivo antes de configurar Django.
if ES_VERCEL:
    LOGGING["handlers"].pop("file", None)

