import httplib
import json

from glusterapi.common import BaseAPI
from glusterapi.exceptions import GlusterApiInvalidInputs


class PeerApis(BaseAPI):
    def peer_add(self, host, metadata=None, zone=""):
        """
        Gluster Peer Add

        :param host: (string) Hostname or IP
        :raises: GlusterApiError on failure
        """
        if not host:
            raise GlusterApiInvalidInputs("Hostname cannot be empty")
        req = dict()
        req['addresses'] = []
        req['addresses'].append(host)
        if metadata is None:
            metadata = dict()
        req['metadata'] = metadata
        req['zone'] = zone
        return self._handle_request(self._post, httplib.CREATED, "/v1/peers",
                                    json.dumps(req))

    def peer_remove(self, peerid):
        """
        Gluster Peer Remove

        :param host: (string) Hostname or IP
        :raises: GlusterApiError on failure
        """
        if not peerid:
            raise GlusterApiInvalidInputs("Peer ID cannot be empty")
        url = "/v1/peers" + peerid
        return self._handle_request(self._delete, httplib.NO_CONTENT, url, None)

    def peer_status(self):
        """
        Gluster Peer Status

        :raises: GlusterApiError on failure
        """
        return self._handle_request(self._get, httplib.OK, "/v1/peers")
