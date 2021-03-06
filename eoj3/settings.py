"""
Django settings for eoj3 project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.humanize',
  'django.contrib.sites',

  'api',
  'home',
  'account',
  'dispatcher',
  'problem',
  'backstage',
  'submission',
  'contest',
  'utils',
  'tests',
  'blog',
  'migrate',
  'polygon',
  'filemanager',
  'paste',

  # third-party packages
  'widget_tweaks',
  'django_jinja',
  'django_jinja.contrib._humanize',
  'tagging',
  'debug_toolbar',
  'captcha',
  'rest_framework',
  'django_extensions',
  'django_comments_xtd',
  'django_comments',
  'notifications',

  'django_q',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'utils.middleware.close_site_middleware.CloseSiteMiddleware',
  'debug_toolbar.middleware.DebugToolbarMiddleware',
  'utils.middleware.globalrequestmiddleware.GlobalRequestMiddleware',
  'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'eoj3.urls'

TEMPLATES = [
  {
    'BACKEND': 'django_jinja.backend.Jinja2',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    # 'OPTIONS': {'environment': 'eoj3.jinja2.environment'},
    'APP_DIRS': True,
    'OPTIONS': {
      "undefined": None,
      "match_extension": ".jinja2",
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        "django.template.context_processors.i18n",
        'notification.context_processors.notification_processor.notification_processor',
      ],
      "globals": {
        "myGlobal": "utils.jinja2.globals.is_active",
        "myGlobal2": "utils.jinja2.globals.paginator",
        "myGlobal3": "utils.jinja2.globals.render_field",
        "myGlobal4": "utils.jinja2.globals.url_replace",
        "myGlobal5": "utils.jinja2.globals.static_file_modify",
        "myGlobal6": "utils.jinja2.globals.render_comment_tree",
        "myGlobal7": "utils.jinja2.globals.url_encode",
        "myGlobal8": "utils.jinja2.globals.username_display",
        "myGlobal9": "utils.jinja2.globals.get_current_language",
      },
      "filters": {
        "myFilter": "utils.jinja2.filters.status_choice",
        "myFilter2": "utils.jinja2.filters.timedelta_format",
        "myFilter3": "utils.jinja2.filters.markdown_format",
        "myFilter4": "utils.jinja2.filters.sample_format",
        "myFilter5": "utils.jinja2.filters.minute_format",
        "myFilter6": "utils.jinja2.filters.get_intro",
        "myFilter7": "utils.jinja2.filters.n2br",
        "myFilter8": "utils.jinja2.filters.xss_filter",
        "myFilter9": "utils.jinja2.filters.natural_duration",
      },
      "tests": {
        "myTest": "utils.jinja2.tests.is_admin",
      },
      "extensions": [
        "jinja2.ext.do",
        "jinja2.ext.loopcontrols",
        "jinja2.ext.with_",
        "jinja2.ext.i18n",
        "jinja2.ext.autoescape",
        "django_jinja.builtins.extensions.CsrfExtension",
        "django_jinja.builtins.extensions.CacheExtension",
        "django_jinja.builtins.extensions.TimezoneExtension",
        "django_jinja.builtins.extensions.UrlsExtension",
        "django_jinja.builtins.extensions.StaticFilesExtension",
        "django_jinja.builtins.extensions.DjangoFiltersExtension",
      ],
      "translation_engine": "django.utils.translation",
    },
  },
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        "django.template.context_processors.i18n",
      ]
    },
  },
]

WSGI_APPLICATION = 'eoj3.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    'OPTIONS': {
      'min_length': 6
    }
  },
  {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
  }
]

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'
LANGUAGES = (
  ('zh-Hans', '简体中文'),
)
LOCALE_PATHS = (
  os.path.join(BASE_DIR, 'locale', 'humanize'),
)
USE_I18N = True
TIME_ZONE = 'Asia/Shanghai'
# TIME_ZONE = 'UTC'
USE_L10N = True
USE_TZ = False

# settings

MEDIA_URL = '/media/'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
DATETIME_FORMAT = 'Y-m-d H:i'  # only for django templates
DATETIME_FORMAT_TEMPLATE = '%Y-%m-%d %H:%M:%S'

STATIC_ROOT = STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/fake/static/'
STATICFILES_DIRS = []

AUTH_USER_MODEL = 'account.User'
SESSION_COOKIE_AGE = 1209600  # default 2 weeks

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    'utils.authentication.UnsafeSessionAuthentication',
  ),
  'DEFAULT_THROTTLE_CLASSES': (
    'rest_framework.throttling.UserRateThrottle',
  ),
  'DEFAULT_THROTTLE_RATES': {
    'user': '60/minute'
  }
}

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_PANELS = [
  'debug_toolbar.panels.versions.VersionsPanel',
  'debug_toolbar.panels.timer.TimerPanel',
  'debug_toolbar.panels.settings.SettingsPanel',
  'debug_toolbar.panels.headers.HeadersPanel',
  'debug_toolbar.panels.request.RequestPanel',
  'debug_toolbar.panels.sql.SQLPanel',
  'debug_toolbar.panels.staticfiles.StaticFilesPanel',
  # original broken by django-jinja, remove this whole block later
  'utils.debug.TemplatesPanel',
  'debug_toolbar.panels.cache.CachePanel',
  'debug_toolbar.panels.signals.SignalsPanel',
  'debug_toolbar.panels.logging.LoggingPanel',
  'debug_toolbar.panels.redirects.RedirectsPanel',
]

# captcha
CAPTCHA_FOREGROUND_COLOR = "#001100"
CAPTCHA_FILTER_FUNCTIONS = []
CAPTCHA_CHALLENGE_FUNCT = 'eoj3.captcha.random_math_challenge'

AUTHENTICATION_BACKENDS = ['account.permissions.UsernameOrEmailModelBackend']

# comment
COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL = 5
COMMENTS_XTD_CONFIRM_EMAIL = False

COMMENTS_XTD_APP_MODEL_OPTIONS = {
  'default': {
    'allow_flagging': True,
    'allow_feedback': True,
    'show_feedback': False,
  },
  'contest.contest': {
    'allow_flagging': False,
    'allow_feedback': False,
    'show_feedback': False,
  }
}

COMMENT_MAX_LENGTH = 3000

# notification
NOTIFICATIONS_SOFT_DELETE = True

Q_CLUSTER = {
  'name': 'eoj_cluster',
  'workers': 24,
  'recycle': 20,
  'timeout': 14400,  # 4 hours
  'retry': None,
  'cached': 3600,
  'queue_limit': 3000,
  'cpu_affinity': 1,
  'django_redis': 'default',
  'log_level': 'WARNING',
}

SUBMISSION_INTERVAL_LIMIT = 5
SUBMISSION_ATTEMPT_LIMIT = 100

# configurable settings

# host & ip

ALLOWED_HOSTS = ['*']
IPWARE_PRIVATE_IP_PREFIX = ()
WHITE_LIST_HOST = []

# path

REPO_DIR = os.path.join(BASE_DIR, 'repo')
TESTDATA_DIR = os.path.join(BASE_DIR, 'testdata')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

UPLOAD_DIR = os.path.join(BASE_DIR, "upload")
MIRROR_DIR = os.path.join(BASE_DIR, "upload", "mirror")
GENERATE_DIR = os.path.join(BASE_DIR, "generate")
LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

# database

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'eoj',
    'CONN_MAX_AGE': 2,
    'HOST': '127.0.0.1',
    'PORT': 3306,
    'USER': 'eoj',
    'PASSWORD': 'eoj'
  }
}

# cache

CACHES = {
  "default": {
    "BACKEND": "django_redis.cache.RedisCache",
    "LOCATION": "redis://127.0.0.1:6379/1",
    "OPTIONS": {
      "CLIENT_CLASS": "django_redis.client.DefaultClient",
      "MAX_ENTRIES": 65536,
    }
  },
  "judge": {
    "BACKEND": "django_redis.cache.RedisCache",
    "LOCATION": "redis://127.0.0.1:6379/2",
    "OPTIONS": {
      "CLIENT_CLASS": "django_redis.client.DefaultClient",
      "MAX_ENTRIES": 65536,
    }
  }
}

# security

SECRET_KEY = 'secret_key'
DEBUG = False

# email

EMAIL_HOST = "mail.server.fake"
EMAIL_HOST_USER = "noreply@server.fake"
EMAIL_HOST_PASSWORD = ""
SERVER_EMAIL = "noreply@server.fake"
DEFAULT_FROM_EMAIL = "noreply@server.fake"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
ADMINS = [('support', 'support@server.fake')]
ADMIN_EMAIL_LIST = []

# logging

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'verbose': {
      'format': '{levelname} {asctime} ({module}) {message}',
      'style': '{',
    },
    'simple': {
      'format': '{levelname} {message}',
      'style': '{',
    },
  },
  'handlers': {
    'file': {
      'level': 'WARNING',
      'formatter': 'verbose',
      'class': 'logging.FileHandler',
      'filename': os.path.join(LOG_DIR, 'django.log'),
    },
  },
  'loggers': {
    'django': {
      'handlers': ['file'],
      'level': 'WARNING',
      'propagate': True,
    },
  },
}

# recommendation service

RECOMMENDATION_SERVICE_URL = "127.0.0.1:20019"


# local settings override

if "USE_ENV" in os.environ:
  from .env_settings import * # pylint: disable=unused-import,unused-wildcard-import,wildcard-import,wrong-import-position

try:
  from .local_settings import * # pylint: disable=unused-import,unused-wildcard-import,wildcard-import,wrong-import-position
except ImportError:
  pass
