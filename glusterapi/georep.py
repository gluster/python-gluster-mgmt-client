from common import BaseAPI

class GeorepApis(BaseAPI):
    def georep_create(self, mastervol, remotehost,
                      remotevol, remoteuser="root"):
        """
        Create Geo-replication Session

        :param mastervol: (string) Master Volume Name
        :param remotehost: (string) Remote Host
        :param remotevol: (string) Remote Volume
        :param remoteuser: (string) Remote User
        :raises: GlusterAPIError or failure
        """
        pass

    def georep_start(self, mastervol, remotehost, remotevol,
                     remoteuser="root"):
        """
        Create Geo-replication Session

        :param mastervol: (string) Master Volume Name
        :param remotehost: (string) Remote Host
        :param remotevol: (string) Remote Volume
        :param remoteuser: (string) Remote User
        :raises: GlusterAPIError or failure
        """
        pass

    def georep_stop(self, mastervol, remotehost, remotevol,
                    remoteuser="root"):
        """
        Create Geo-replication Session

        :param mastervol: (string) Master Volume Name
        :param remotehost: (string) Remote Host
        :param remotevol: (string) Remote Volume
        :param remoteuser: (string) Remote User
        :raises: GlusterAPIError or failure
        """
        pass

    def georep_delete(self, mastervol, remotehost,
                      remotevol, remoteuser="root"):
        """
        Create Geo-replication Session

        :param mastervol: (string) Master Volume Name
        :param remotehost: (string) Remote Host
        :param remotevol: (string) Remote Volume
        :param remoteuser: (string) Remote User
        :raises: GlusterAPIError or failure
        """
        pass

    def georep_set(self, mastervol, remotehost, remotevol,
                   optname, optvalue, remoteuser="root"):
        """
        Set Geo-replication Session Option

        :param mastervol: (string) Master Volume Name
        :param remotehost: (string) Remote Host
        :param remotevol: (string) Remote Volume
        :param remoteuser: (string) Remote User
        :param optname: (string) Option Name
        :param optvalue: (string) Option Value
        :raises: GlusterAPIError or failure
        """
        pass

    def georep_get(self, mastervol, remotehost, remotevol,
                   remoteuser="root", optname=None):
        """
        Get Geo-replication Session Option

        :param mastervol: (string) Master Volume Name
        :param remotehost: (string) Remote Host
        :param remotevol: (string) Remote Volume
        :param remoteuser: (string) Remote User
        :param optname: (string) Option name
        :raises: GlusterAPIError or failure
        """
        pass

    def georep_reset(self, mastervol, remotehost,
                     remotevol, optname, remoteuser="root"):
        """
        Reset Geo-replication Session Option

        :param mastervol: (string) Master Volume Name
        :param remotehost: (string) Remote Host
        :param remotevol: (string) Remote Volume
        :param optname: (string) Option name
        :param remoteuser: (string) Remote User
        :raises: GlusterAPIError or failure
        """
        pass

    def georep_checkpoint(self, mastervol, remotehost,
                          remotevol, remoteuser="root"):
        """
        Set Geo-replication Session Checkpoint

        :param mastervol: (string) Master Volume Name
        :param remotehost: (string) Remote Host
        :param remotevol: (string) Remote Volume
        :param remoteuser: (string) Remote User
        :raises: GlusterAPIError or failure
        """
        return self.georep_set(mastervol, remotehost, remotevol,
                               "checkpoint", "now", remoteuser)

    def georep_status(self, mastervol=None, remotehost=None,
                      remotevol=None, remoteuser=None):
        """
        Geo-replication Session Status

        :param mastervol: (string) Master Volume Name
        :param remotehost: (string) Remote Host
        :param remotevol: (string) Remote Volume
        :param remoteuser: (string) Remote User
        :raises: GlusterAPIError or failure
        """
        pass

