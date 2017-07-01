
#lembrar de botar local_settings no gitignore caso seja feito igual
import os
import dj_database_url #CONFIG DEPLOY HEROKU

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#CONFIG DE DEPLOY NO HEROKU
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


SECRET_KEY = '-uhpfb-=5&l!s0h5sn8*(3a^slvqng24z7b$0yt!a8w+2*$m9#'


DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #lib
    'widget_tweaks',
    #apps
    'util',
    'catalogo',
    'accounts',
    'checkout',

]

MIDDLEWARE= [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',#serve arquivos estaticos #só add ela aki e pronto e no requirements
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'checkout.middleware.cart_item_middleware'
]

ROOT_URLCONF = 'ecommercedjango01.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #APP processor responsavel pelo carregamento das categorias
                'catalogo.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommercedjango01.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

##-CONFIG DE DEPLOY NO HEROKU-TEM UMA PARTE LA EM CIMA##
STATIC_URL = '/static/'

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
###########################-------##############################

##-CONFIG DE ENVIO DE EMAIL-##

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT=587
EMAIL_USE_TLS = True


##-------procfile e runtime sao arquivos necessarios para  rodar no heroku  juntamente com o requirements


############################------##############################

##CONFIG DO USUARIO##

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL_REGISTER='util:index'
LOGIN_REDIRECT_URL = 'accounts:index'
UPDATE_REDIRECT_URL = 'accounts:UpdateUser'
AUTH_USER_MODEL = 'accounts.User'
#Backends de autenticação normal,customizado login com email
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.ModelBackend',
)
#####################################


##pagseguro
PAGSEGURO_TOKEN= '' #TOKEN DA CONTA DO COMERCIO
PAGSEGURO_EMAIL = '' #EMAIL DA CONTA DO COMERCIO
PAGSEGURO_SANDBOX = True #SANDBOX PLATAFORMA DE TESTES DE TRANSAÇÃO DO PAGSEGURO
