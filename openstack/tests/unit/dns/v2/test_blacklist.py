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

from openstack.dns.v2 import blacklist
from openstack.tests.unit import base

IDENTIFIER = 'af91edb5-ede8-453f-af13-feabdd088f9c'
EXAMPLE = {
    'id': IDENTIFIER,
    'description': 'This is a blacklisted domain.',
    'pattern': '^([A-Za-z0-9_\\-]+\\.)*example\\.com\\.$',
}


class TestBlacklist(base.TestCase):
    def test_basic(self):
        sot = blacklist.BlackList
        self.assertEqual(None, sot.resource_key)
        self.assertEqual('blacklists', sot.resources_key)
        self.assertEqual('/blacklists', sot.base_path)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_fetch)
        self.assertTrue(sot.allow_commit)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

        self.assertEqual('PATCH', sot.commit_method)

    def test_make_it(self):
        sot = blacklist.BlackList(**EXAMPLE)
        self.assertEqual(IDENTIFIER, sot.id)
        self.assertEqual(EXAMPLE['created_at'], sot.created_at)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['links'], sot.links)
        self.assertEqual(EXAMPLE['pattern'], sot.pattern)
        self.assertEqual(EXAMPLE['updated_at'], sot.updated_at)
