import httplib
import json

from glusterapi.common import BaseAPI, validate_peer_id
from glusterapi.exceptions import GlusterApiInvalidInputs


class DeviceApis(BaseAPI):
    def device_add(self, peerid, device):
        """
        Gluster device add.

        :param peerid: (string) Peer UUID
        :param device: (string) device name
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        validate_peer_id(peerid)
        device = device.strip()
        if not device:
            raise GlusterApiInvalidInputs("Invalid device specified")
        req = {
            "device": device
        }
        return self._handle_request(self._post, httplib.CREATED,
                                    "/v1/devices/%s" % peerid, json.dumps(req))

    def device_status(self, peerid):
        """
        Gluster get devices in peer.

        :param peerid: (string) peerid returned from peer_add
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        validate_peer_id(peerid)
        url = "/v1/devices/" + peerid
        return self._handle_request(self._get, httplib.OK, url)

    def devices(self):
        """
        Gluster list all devices.

        :raises: GlusterApiError on failure
        """
        return self._handle_request(self._get, httplib.OK, "/devices")
