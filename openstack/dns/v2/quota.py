from openstack.dns.v2 import _base


class Quota(_base.Resource):  # _base.Resource is a class from openstack/dns/v2/_base.py
    """DNS Quota Resource"""

    base_path = "/quotas"

    # capabilities
    allow_list = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True

    # Properties
    zones = _base.resource.Body("zones", type=int)
