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
from .base import *

# Third-party imports
from dotenv import load_dotenv

# Load the .env file containing local environment variables
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
if os.getenv('DEVELOPMENT') == 'true':
    from .dev import *
else:
    from .prod import *