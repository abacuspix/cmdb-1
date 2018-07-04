"""
Django settings for mico project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xxr%x@-u5r(p6shkn+n)uv+h+@l61k8&8t-yonli9!y9h6h!%6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = '/login/'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cmdb',
    'asset',
    'logs',
    'winservices',
    'cache',
    'www',
    'djcelery',
    'subversion',
    'web',
    'kettle',
    'workflow',
    'alert',
    'users',
    'config_center',
    'command_job',
    'consul_kv',
    'disque',
    'project_crontab',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cmdb.http.SetRemoteAddrFromForwardedFor',
]

ROOT_URLCONF = 'mico.urls'
BROKER_URL = 'redis://127.0.0.1:6379/3'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/4'

TEMPLATES = [
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
            ],
        },
    },
]

WSGI_APPLICATION = 'mico.wsgi.application'

SESSION_COOKIE_AGE = 1800
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cmdb',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = '/django/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

#salt api info
salt_api_url = 'https://192.168.199.61:18080/'
salt_api_url2 = 'https://192.168.199.61:18080/'
salt_user = 'saltapis'
salt_password = 'saltapis'
salt_location = 'slq'

##dingding notification
dingding_api = 'http://dlog.abc.me/dlog'

##project_crontab api
crontab_api = 'http://192.168.199.64:5000'
crontab_flask_port = '5001'

##kettle setting
kettle_host = 't-slq-web-1'
kettle_install_dir = '/srv/kettle/data-integration/'
kettle_svn_path = '/srv/kettle/bi/kettle/'
kettle_log_path = '/tmp/'
kettle_log_url = 'http://127.0.0.1/'

##dingding_robo
dingding_robo_url = "https://oapi.dingtalk.com/robot/send?access_token=6e710e17889d16a722064d6679c487781547ad9d2e804e474553992361f4563d"
wechat_robo_url = "http://wechat.abc.com/robot/send?access_token=0222b995f38172ddf"

##go info
svn_username = '123456'
svn_password = '123456'
go_local_path = '/srv/'
go_move_path = '/tmp/'
go_revert_path = '/srv/revert'
svn_gotemplate_repo = 'http://svn.abc.com/svn/gotemplate/'
svn_gotemplate_local_path = '/srv/gotemplate/'
svn_host = 't-slq-jen-1'
svn_repo_url = 'http://svn.abc.com/svn/'

##webpage
webpage_host = 't-slq-web-1'
m_webpage_host = 't-slq-web-1'

##gitlab
gitlab_url = 'http://abc.com'
gitlab_private_token = 'sdadasdadwwe'

##jenkins
jenkins_url = {
    'uat': ['http://abc.com/job/uat/', 'http://abc.com/job/uat2/'],
    'uat_aws': ['http://abc.com/job/uat_aws/'],
    'deploy': 'http://abc.com/job/deploy/'
}
jenkins_webhook_url = {
    'uat': ['http://abc.com/project/uat', 'http://abc.com/project/uat2'],
    'uat_aws': ['http://abc.com/project/uat_aws'],
    'deploy': 'http://abc.com/project/deploy'
}
jenkins_username = 'abc'
jenkins_password = 'abc'

graphite_api = 'http://192.168.199.61:8080'
aac_api = 'http://192.168.199.178:9090/api/v1.0'
aac_headers = {'X-AUTH-TOKEN': 'd14b7042a2af18a9ffe15a0da343497f'}

##consul
consul_api = {
    'hsg': 'http://192.168.199.64:8500/v1/kv/',
    'aws': 'http://192.168.199.64:8500/v1/kv/'
}

##nginx api
nginx_api = ['http://192.168.199.63:8081']

##zabbix api
zabbix_url = "http://192.168.199.96/api_jsonrpc.php"
zabbix_user = "public"
zabbix_password = "public"
zabbix_userId = 1

##cloudapi
qcloud_region = 'ap-shanghai'
qcloud_secretId = '123456'
qcloud_secretKey = '123456'

qingcloud_secretId = '123456'
qingcloud_secretKey = '123456'

## command
cmd_host_aws = '127.0.0.1'
cmd_host_qcd = '127.0.0.1'


# consul_kv
CONSUL_AGENT = {
    'hsg': '127.0.0.1',
    'aws': '127.0.0.1',
    'qcd': '127.0.0.1',
}

ZABBIX_INFO = [
    ('https://zabbix.localhost', 'admin', 'admin', '13'),
]
GRAFANA_URL = 'https://<user>:<pass>@grafana.localhost'
SENTRY_URL = 'https://sentry.localhost'
