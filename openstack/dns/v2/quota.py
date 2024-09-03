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


class Quota(_base.Resource):
    """DNS Quota Resource"""

    base_path = "/quotas"

    # capabilities
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True
    commit_method = "PATCH"

    # Properties
    #: The ID of the project.
    project = resource.URI("project", alternate_id=True)
    #: The maximum amount of recordsets allowed in a zone export. *Type: int*
    api_export_size = resource.Body("api_export_size", type=int)
    #: The maximum amount of records allowed per recordset. *Type: int*
    recordset_records = resource.Body("recordset_records", type=int)
    #: The maximum amount of records allowed per zone. *Type: int*
    zone_records = resource.Body("zone_records", type=int)
    #: The maximum amount of zones allowed per project. *Type: int*
    zones = resource.Body("zones", type=int)

    def _prepare_request(
        self, requires_id=True, base_path=None, prepend_key=False, **kwargs
    ):
        _request = super()._prepare_request(
            requires_id, prepend_key, base_path=base_path
        )
        if self.resource_key in _request.body:
            _body = _request.body[self.resource_key]
        else:
            _body = _request.body
        if 'id' in _body:
            del _body['id']
        return _request
