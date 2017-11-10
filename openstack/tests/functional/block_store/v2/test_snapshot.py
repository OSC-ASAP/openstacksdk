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


from openstack.block_store.v2 import snapshot as _snapshot
from openstack.block_store.v2 import volume as _volume
from openstack.tests.functional import base


class TestSnapshot(base.BaseFunctionalTest):

    def setUp(self):
        super(TestSnapshot, self).setUp()

        self.SNAPSHOT_NAME = self.getUniqueString()
        self.SNAPSHOT_ID = None
        self.VOLUME_NAME = self.getUniqueString()
        self.VOLUME_ID = None

        volume = self.conn.block_store.create_volume(
            name=self.VOLUME_NAME,
            size=1)
        self.conn.block_store.wait_for_status(
            volume,
            status='available',
            failures=['error'],
            interval=2,
            wait=120)
        assert isinstance(volume, _volume.Volume)
        self.assertEqual(self.VOLUME_NAME, volume.name)
        self.VOLUME_ID = volume.id
        snapshot = self.conn.block_store.create_snapshot(
            name=self.SNAPSHOT_NAME,
            volume_id=self.VOLUME_ID)
        self.conn.block_store.wait_for_status(
            snapshot,
            status='available',
            failures=['error'],
            interval=2,
            wait=120)
        assert isinstance(snapshot, _snapshot.Snapshot)
        self.assertEqual(self.SNAPSHOT_NAME, snapshot.name)
        self.SNAPSHOT_ID = snapshot.id

    def tearDown(self):
        snapshot = self.conn.block_store.get_snapshot(self.SNAPSHOT_ID)
        sot = self.conn.block_store.delete_snapshot(
            snapshot, ignore_missing=False)
        self.conn.block_store.wait_for_delete(
            snapshot, interval=2, wait=120)
        self.assertIsNone(sot)
        sot = self.conn.block_store.delete_volume(
            self.VOLUME_ID, ignore_missing=False)
        self.assertIsNone(sot)
        super(TestSnapshot, self).tearDown()

    def test_get(self):
        sot = self.conn.block_store.get_snapshot(self.SNAPSHOT_ID)
        self.assertEqual(self.SNAPSHOT_NAME, sot.name)
