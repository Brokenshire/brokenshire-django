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

# Third-party imports
from django.views.generic import TemplateView


# Class HomePageView which displays home.html
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


# Class AboutPageView which displays home.html
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'