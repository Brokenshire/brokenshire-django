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

# Local import
from .base import *

# Third-party imports
from dotenv import load_dotenv


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Load .env file codes
load_dotenv()


ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0',
    'localhost',
]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'brokenshire',
        'USER': 'postgres',
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')