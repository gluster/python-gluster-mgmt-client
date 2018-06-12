import httplib
import json

from glusterapi.common import BaseAPI
from glusterapi.exceptions import GlusterApiInvalidInputs


class SnapshotsApis(BaseAPI):
    def snapshot_create(self, volume_name="", snap_name="", timestamp=False,
                        description="", force=False):
        """
        Gluster snapshot create.

        :param volume_name: (string) volume name
        :param snap_name: (string) snapshot name
        :param timestamp: (bool)  timestamp for snapshot
        :param description: (string) snapshot description
         :param force: (bool)  force create snapshot
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        volume_name = volume_name.strip()
        if not volume_name:
            raise GlusterApiInvalidInputs("Volume name cannot be empty")

        snap_name = snap_name.strip()
        if not snap_name:
            raise GlusterApiInvalidInputs("snapshot name cannot be empty")
        req = {
            "volname": volume_name,
            "snapname": snap_name,
            "timestamp": timestamp,
            "description": description,
            "force": force
        }
        return self._handle_request(self._post, httplib.CREATED,
                                    "/v1/snapshot", json.dumps(req))

    def snapshot_activate(self, snap_name="", force=False):
        """
        Gluster activate snapshot.

        :param snap_name: (string) snapshot name
        :param force: (bool)  force create snapshot
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        snap_name = snap_name.strip()
        if not snap_name:
            raise GlusterApiInvalidInputs("snapshot name cannot be empty")
        req = {
            "force": force
        }
        return self._handle_request(self._post, httplib.OK,
                                    "/v1/snapshot/%s/activate" % snap_name,
                                    json.dumps(
                                        req))

    def snapshot_deactivate(self, snap_name=""):
        """
        Gluster activate  snapshot.
        
        :param snap_name: (string) snapshot name
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        snap_name = snap_name.strip()
        if not snap_name:
            raise GlusterApiInvalidInputs("snapshot name cannot be empty")

        return self._handle_request(self._post, httplib.OK,
                                    "/v1/snapshot/%s/deactivate" % snap_name,
                                    None)

    def snapshot_list(self, vol_name=""):
        """
        Gluster list snapshot.

        :param vol_name: (string) volume  name
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        vol_name = vol_name.strip()
        if not vol_name:
            raise GlusterApiInvalidInputs("volname name cannot be empty")

        pass

    def snapshot_info(self, snap_name=""):
        """
        Gluster snapshot info.

        :param snap_name: (string) snapshot  name
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        snap_name = snap_name.strip()
        if not snap_name:
            raise GlusterApiInvalidInputs("snapshot name cannot be empty")

        return self._handle_request(self._get, httplib.OK,
                                    "/v1/snapshot/%s" % snap_name)
