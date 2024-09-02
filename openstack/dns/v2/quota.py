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

    # Properties
    #: The ID of the project.
    project = resource.URI("project")

    api_export_size = resource.Body("api_export_size", type=int)

    recordset_records = resource.Body("recordset_records", type=int)

    zone_records = resource.Body("zone_records", type=int)

    zones = resource.Body("zones", type=int)
