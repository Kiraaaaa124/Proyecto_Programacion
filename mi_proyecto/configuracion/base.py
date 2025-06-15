from pathlib import Path
import json 

import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_FILE_PATH = BASE_DIR / 'secret.json'

if not SECRET_FILE_PATH.exists():
    raise Exception(f"El archivo secret.json no se encontró en {SECRET_FILE_PATH}. Asegúrate de que esté en la raíz de tu proyecto.")

try:
    with open(SECRET_FILE_PATH) as f:
        secrets = json.loads(f.read())
except json.JSONDecodeError:
    raise Exception("Error al decodificar secret.json. Asegúrate de que sea un JSON válido.")

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f"La variable '{setting}' no está definida en secret.json."
        raise Exception(error_msg)

DEBUG = get_secret('DEBUG')
ALLOWED_HOSTS = get_secret('ALLOWED_HOSTS')
SECRET_KEY = get_secret('SECRET_KEY')
LOGIN_URL = get_secret('LOGIN_URL') 
STATIC_URL = get_secret('STATIC_URL')

DATABASES = {
    'default': {
        'ENGINE': get_secret('DB_ENGINE'),
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('DB_USER'),
        'PASSWORD': get_secret('DB_PASSWORD'),
        'HOST': get_secret('DB_HOST'),
        'PORT': get_secret('DB_PORT'),
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #apps de terceros 
    'django_ckeditor_5',
    #local apps
    'apps.departamento',
    'apps.empleado',
]
MEDIA_URL='/media/'
MEDIA_ROOT = BASE_DIR / 'media'
CKEDITOR_5_UPLOADS_PATH="uploads/"

CKEDITOR_5_CONFIGS={
    'default':{
        'toolbar': [
            'heading', '|',
            'bold', 'italic', 'link', 'bulletedList', 'numberedList', '|', 
            'blockQuote', 'insertTable',
            'mediaEmbed', '|',
            'undo', 'redo'
        ],
        'language':'es',
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mi_proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mi_proyecto.wsgi.application'

LANGUAGE_CODE='es-AR'

