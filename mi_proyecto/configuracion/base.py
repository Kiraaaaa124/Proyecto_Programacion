from pathlib import Path
import json 

BASE_DIR = Path(__file__).resolve().parent.parent.parent

secrets_path = BASE_DIR /"secret.json"

with open("secret.json") as s:
    secrets = json.load(s)

SECRET_KEY = secrets["SECRET_KEY"]

LOGIN_URL= secrets["LOGIN_URL"]

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

