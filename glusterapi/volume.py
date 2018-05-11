from common import BaseAPI
from exceptions import GlusterApiInvalidInputs


class TransportType:
    TCP = "tcp"
    RDMA = "rdma"
    Both = "tcp,rdma"


class VolumeApis(BaseAPI):
    def volume_create(self, volname, size=0, bricks=[],
                      transport=TransportType.TCP,
                      replica=None,
                      disperse=None,
                      arbiter=None,
                      force=False):
        """
        Create Gluster Volume

        :param volname: (string) Volume Name
        :raises: GlusterAPIError or failure
        """
        if size > 0 and len(bricks) > 0:
            raise GlusterApiInvalidInputs()

        data={
            "name": volname
        }
        self._handle_request(self._post, 201, "/v1/volumes", data=data)

    def volume_start(self, volname, force=False):
        """
        Start Gluster Volume

        :param volname: (string) Volume Name
        :param force: (bool) Start Volume with Force
        :raises: GlusterAPIError or failure
        """
        data = {
            "force": force
        }
        self._handle_request(self._post, 200,
                             "/v1/volumes/%s/start" % volname, data=data)

    def volume_stop(self, volname, force=False):
        """
        Start Gluster Volume

        :param volname: (string) Volume Name
        :param force: (bool) Stop Volume with Force
        :raises: GlusterAPIError or failure
        """
        data = {
            "force": force
        }
        self._handle_request(self._post, 200,
                             "/v1/volumes/%s/stop" % volname, data=data)

    def volume_restart(self, volname, force=False):
        """
        Restart Gluster Volume

        :param volname: (string) Volume Name
        :param force: (bool) Restart the Volume with Force
        :raises: GlusterAPIError or failure
        """
        data = {
            "force": force
        }
        self.volume_stop(volname, force)
        self.volume_start(volname, force)

    def volume_delete(self, volname, force=False):
        """
        Start Gluster Volume

        :param volname: (string) Volume Name
        :param force: (bool) Stop Volume with Force
        :raises: GlusterAPIError or failure
        """
        data = {
            "force": force
        }
        self._handle_request(self._delete, 200,
                             "/v1/volumes/%s" % volname, data=data)

    def volume_set(self, volname, optname, optvalue):
        """
        Start Gluster Volume

        :param volname: (string) Volume Name
        :param force: (bool) Stop Volume with Force
        :raises: GlusterAPIError or failure
        """
        pass

    def volume_reset(self, volname, optnames=[]):
        """
        Start Gluster Volume

        :param volname: (string) Volume Name
        :param force: (bool) Stop Volume with Force
        :raises: GlusterAPIError or failure
        """
        pass

    def volume_info(self, volname=None):
        """
        Gluster Volume Info

        :param volname: (string) Volume Name
        :param force: (bool) Stop Volume with Force
        :raises: GlusterAPIError or failure
        """
        pass

    def volume_status(self, volname=None):
        """
        Gluster Volume Status

        :param volname: (string) Volume Name
        :raises: GlusterAPIError or failure
        """
        pass

    def volume_get(self, volname, optnames=[]):
        """
        Get Gluster Volume Options

        :param volname: (string) Volume Name
        :param force: (bool) Stop Volume with Force
        :raises: GlusterAPIError or failure
        """
        pass
