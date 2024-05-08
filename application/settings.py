"""
Django settings for application project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os.path
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.


BASE_DIR = Path(__file__).resolve().parent.parent

from config import env
from config.env import *

# 自定义
sys.path.insert(0, BASE_DIR)
sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!kjxf&e0pn4nrl%0&9sqp7n!ld)(gtw7v@i3fwf3sqcsh4ymat'

# SECURITY WARNING: don't run with debugreport turned on in production!
DEBUG = True

# 跨域处理配置
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     'http://127.0.0.1:8080',
# )
CORS_ALLOWED_ORIGINS_REGEXES = [
    r'^http://.*?$',
]
# CORS_ORIGIN_REGEXES_WHITELIST = (
#         r'^http://.*?$',
# )
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

# 使用*通配符默认所有IP均可
ALLOWED_HOSTS = ['*']

# 设置项是否开启URL访问地址后面不为/跳转至带有/的路径
APPEND_SLASH = True

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 创建表、字段注释依赖包
    'addcomments',
    'application',
    # 添加子应用名称
    "captcha",
    'application.login',
    'application.level',
    'application.position',
    'application.dept',
    'application.role',
    'application.role_menu',
    'application.city',
    'application.item',
    'application.item_cate',
    'application.link',
    'application.ad_sort',
    'application.ad',
    'application.notice',
    'application.user',
    'application.user_role',
    'application.member_level',
    'application.member',
    'application.dict',
    'application.dict_data',
    'application.config',
    'application.config_data',
    'application.menu',
    'application.config_web',
    'application.upload',
    'application.supplier',
    'application.repairreport',
    'application.suggestion',
    'application.inspectreport',
    'application.burning',
    'application.debugreport',
    'application.weldingreport',
    'application.debugdata',
    'application.debugdata_teststep',
    'application.testdata',
    'application.testdata_teststep',
    'application.softwarerelease',
    'application.shipmentreport',
    'application.mac',
    'application.workplace',
    'application.comprehensive',
    'application.safety',
    'application.analysis',
    'application.packing',
    'application.product_handover',
    'application.statistic',
    'application.followup',
    'application.rework',
    'application.bind.product',
    'application.bind.module',
]

MIDDLEWARE = [
    # 跨域处理中间件
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 此配置用于解决弹窗被浏览器劫持问题
X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 其中的BASE_DIR为项目根目录路径
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {  # Adding this section should work around the issue.
            },
        },
    },
]

WSGI_APPLICATION = 'application.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    "default": {
        "ENGINE": env.DATABASE_ENGINE,
        "NAME": env.DATABASE_NAME,
        "USER": env.DATABASE_USER,
        "PASSWORD": env.DATABASE_PASSWORD,
        "HOST": env.DATABASE_HOST,
        "PORT": env.DATABASE_PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "public/static"),
    os.path.join(BASE_DIR, "public/uploads"),
    os.path.join(BASE_DIR, "public/uploads/temp"),
    os.path.join(BASE_DIR, "public/uploads/images"),
]
UPLOADS_URL = '/uploads/'
TEMP_URL = '/temp/'
IMAGES_URL = '/images/'



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['api.extensions.auth.JwtQueryParamsAuthentication']
}

# 数据表前缀
TABLE_PREFIX = locals().get('TABLE_PREFIX', "")

# ======================== 验证码相关配置 ===========================
CAPTCHA_IMAGE_SIZE = (200, 60)  # 设置 captcha 图片大小
CAPTCHA_LENGTH = 2  # 字符个数
CAPTCHA_TIMEOUT = 1  # 超时(minutes)
CAPTCHA_OUTPUT_FORMAT = "%(image)s %(text_field)s %(hidden_field)s "
CAPTCHA_FONT_SIZE = 40  # 字体大小
CAPTCHA_FOREGROUND_COLOR = "#1d953f"  # 前景色
CAPTCHA_BACKGROUND_COLOR = "#ffffff"  # 背景色
CAPTCHA_NOISE_FUNCTIONS = (
    'captcha.helpers.noise_null',
    "captcha.helpers.noise_arcs",  # 线
    "captcha.helpers.noise_dots",  # 点
)
# 随机字符验证码
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'  # 字母验证码
# CAPTCHA_CHALLENGE_FUNCT = "captcha.helpers.math_challenge"  # 加减乘除验证码

