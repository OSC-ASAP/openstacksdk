# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.dns.v2 import _base
from openstack import resource


class BlackList(_base.Resource):
    """DNS ZONE BLACKLIST RESOURCE"""

    resources_key = 'blacklists'
    base_path = '/blacklists'

    # capabilities
    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True

    commit_method = "PATCH"

    #: Properties
    #: Blacklist description
    #: Timestamp when the blacklist was created
    created_at = resource.Body('created_at')
    #: *Type: str*
    description = resource.Body('description')
    #: Links contains a `self` pertaining to this blacklist or a `next` pertaining
    #: to next page
    links = resource.Body('links', type=dict)
    # Pattern for this blacklist
    pattern = resource.Body('pattern')
    #: Timestamp when the blacklist was last updated
    updated_at = resource.Body('updated_at')
