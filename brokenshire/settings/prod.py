# Copyright 2020 Jack Brokenshire

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Local imports
import os

# Third-party imports
import django_heroku
import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = [
    'brokenshire.herokuapp.com',
    'www.brokenshire.herokuapp.com',
]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd8brjb1q368gku',
        'USER': 'oapsvgfvggziaq',
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': 'ec2-54-236-122-55.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


# Activate Django-Heroku.
django_heroku.settings(locals())