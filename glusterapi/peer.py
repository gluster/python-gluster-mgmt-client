from common import BaseAPI

class PeerApis(BaseAPI):
    def peer_probe(self, host):
        """
        Gluster Peer Probe

        :param host: (string) Hostname or IP
        :raises: GlusterApiError on failure
        """
        pass

    def peer_attach(self, host):
        """
        Gluster Peer Attach

        :param host: (string) Hostname or IP
        :raises: GlusterApiError on failure
        """
        return self.peer_probe(host)

    def peer_detach(self, host):
        """
        Gluster Peer Detach

        :param host: (string) Hostname or IP
        :raises: GlusterApiError on failure
        """
        pass

    def peer_status(self):
        """
        Gluster Peer Status

        :raises: GlusterApiError on failure
        """
        return self._handle_request(self._get, 200, "/v1/peers")
