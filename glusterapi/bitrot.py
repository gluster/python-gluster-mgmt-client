import httplib

from glusterapi.common import BaseAPI, validate_volume_name


class BitrotApis(BaseAPI):
    def bitrot_enable(self, volume):
        """
        Gluster enable bitrot for a volume.

        :param volume: (string) volume name
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        validate_volume_name(volume)

        return self._handle_request(self._post, httplib.OK,
                                    "/v1/volumes/%s/bitrot/enable" % volume,
                                    None)

    def bitrot_disable(self, volume):
        """
        Gluster disable bitrot for a volume.

        :param volume: (string) volume name
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        validate_volume_name(volume)

        return self._handle_request(self._post, httplib.OK,
                                    "/v1/volumes/%s/bitrot/disable" % volume,
                                    None)

    def bitrot_scrub(self, volume):
        """
        Gluster starts bitrot scrubber on demand for a volume.

        :param volume: (string) volume name
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        validate_volume_name(volume)

        return self._handle_request(self._post, httplib.OK,
                                    "/v1/volumes/%s/bitrot/scrubondemand" %
                                    volume, None)

    def bitrot_scrub_status(self, volume):
        """
        Gluster get bitrot scrub status of a volume.

        :param volume: (string) volume name
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        validate_volume_name(volume)

        return self._handle_request(self._post, httplib.OK,
                                    "/v1/volumes/%s/bitrot/scrubstatus" %
                                    volume, None)
