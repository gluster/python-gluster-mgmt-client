"""This module contains the python  glusterd2 volume api's implementation."""
import httplib
import json

from glusterapi.common import BaseAPI, validate_uuid, validate_volume_name
from glusterapi.exceptions import GlusterApiInvalidInputs


class TransportType(object):
    TCP = "tcp"
    RDMA = "rdma"
    Both = "tcp,rdma"

    def check(self, transport_type):
        if transport_type not in (self.TCP, self.RDMA, self.Both):
            raise GlusterApiInvalidInputs(
                "Transport type %s not supported" % transport_type)


def validate_brick(bricks=None):
    """
    Validate brick pattern.

    :param bricks: (list) in the form of ["nodeid:brickpath"]
    :return brick_req: (list) list of bricks
    """
    brick_req = []
    if bricks is None:
        return None
    for brick in bricks:
        brk = brick.split(":")
        if len(brk) != 2:
            return None
        if validate_uuid(brk[0]) is False:
            return None
        req = dict()
        req['peerid'] = brk[0]
        req['path'] = brk[1]
        brick_req.append(req)
    return brick_req


class VolumeApis(BaseAPI):
    def volume_create(self, bricks, volume_name="",
                      transport=TransportType.TCP, replica=0, disperse=0,
                      disperse_data=0, disperse_redundancy=0,
                      arbiter=0, force=False, options=None, metadata=None,
                      ):
        """
        Create Gluster Volume.

        :param volume_name: (string) Volume Name
        :param bricks:  (list)  list of bricks
        :param transport (string) brick transport
        :param replica  (int) replica count
        :param disperse (int) disperse count
        :param disperse_data (int) disperse_data count
        :param disperse_redundancy (int) disperse_redundancy count
        :param arbiter  (int) arbiter count
        :param force  (bool)  force flag
        :param options (dict) volume options
        :param metadata (dict) volume metadata
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        if bricks is None or len(bricks) <= 0:
            raise GlusterApiInvalidInputs()
        req_bricks = validate_brick(bricks)

        if req_bricks is None:
            raise GlusterApiInvalidInputs("Invalid Brick details, bricks "
                                          "should be in form of "
                                          "<peerid>:<path>")

        t = TransportType()
        t.check(transport)

        num_bricks = len(bricks)
        sub_volume = []

        if replica > 0:
            if num_bricks % replica != 0:
                raise GlusterApiInvalidInputs(
                    "Invalid number of bricks specified")

            num_subvol = num_bricks / replica
            for i in range(0, num_subvol):
                idx = i * replica
                # If Arbiter is set, set it as Brick Type for last brick
                if arbiter > 0:
                    req_bricks[idx * replica - 1]['type'] = 'arbiter'
                subvol_req = dict()
                subvol_req['type'] = 'replicate'
                subvol_req['bricks'] = req_bricks[idx:idx + replica]
                subvol_req['replica'] = replica
                subvol_req['arbiter'] = arbiter
                sub_volume.append(subvol_req)
        elif disperse > 0:
            subvol_size = disperse
            if num_bricks % subvol_size != 0:
                raise GlusterApiInvalidInputs(
                    "Invalid number of bricks specified")

            num_subvols = num_bricks / subvol_size
            for i in range(0, num_subvols):
                idx = i * subvol_size
                subvol_req = dict()
                subvol_req['type'] = 'disperse'
                subvol_req['bricks'] = req_bricks[idx:idx + subvol_size]
                subvol_req['disperse-count'] = disperse
                subvol_req['disperse-data'] = disperse_data
                subvol_req['disperse-redundancy'] = disperse_redundancy
                sub_volume.append(subvol_req)
        else:
            subvol_req = dict()
            subvol_req['type'] = 'distrubute'
            subvol_req['bricks'] = req_bricks
            sub_volume.append(subvol_req)

        if options is None:
            options = dict()

        data = {
            "name": volume_name,
            "subvols": sub_volume,
            "transport": transport,
            "options": options,
            "force": force,
            "metadata": metadata,

        }

        return self._handle_request(self._post, httplib.CREATED,
                                    "/v1/volumes", data=json.dumps(data))

    def volume_start(self, vol_name, force=False):
        """
        Start Gluster Volume.

        :param vol_name: (string) Volume Name
        :param force: (bool) Start Volume with Force
        :raises: GlusterAPIError or failure
        """
        validate_volume_name(vol_name)

        data = {
            "force-start-bricks": force
        }
        return self._handle_request(self._post, httplib.OK,
                                    "/v1/volumes/%s/start" % vol_name,
                                    data=json.dumps(data))

    def volume_stop(self, vol_name):
        """
        Start Gluster Volume.

        :param vol_name: (string) Volume Name
        :raises: GlusterAPIError or failure
        """
        validate_volume_name(vol_name)

        return self._handle_request(self._post, httplib.OK,
                                    "/v1/volumes/%s/stop" % vol_name, None)

    def volume_restart(self, vol_name, force=False):
        """
        Restart Gluster Volume.

        :param vol_name: (string) Volume Name
        :param force: (bool) Restart the Volume with Force
        :raises: GlusterAPIError or failure
        """
        validate_volume_name(vol_name)

        self.volume_stop(vol_name)
        return self.volume_start(vol_name, force)

    def volume_delete(self, vol_name):
        """
        Start Gluster Volume.

        :param vol_name: (string) Volume Name
        :raises: GlusterAPIError or failure
        """
        validate_volume_name(vol_name)

        return self._handle_request(self._delete, httplib.NO_CONTENT,
                                    "/v1/volumes/%s" % vol_name, None)

    def volume_set(self, vol_name, options=None,
                   advance=False,
                   experimental=False,
                   deprecated=False):
        """
        Start Gluster Volume.

        :param vol_name: (string) Volume Name
        :param options: (dict) options to set on volume
        :param advance: (bool) advance flag to set options
        :param experimental: (bool) experimental flag to set options
        :param deprecated: (bool) deprecated flag to set options
        :raises: GlusterApiError or GlusterApiInvalidInputs on failure
        """
        validate_volume_name(vol_name)

        if options is None:
            raise GlusterApiInvalidInputs("cannot set empty options")

        vol_options = dict()
        req = dict()
        for key in options:
            vol_options[key] = options[key]
        req['options'] = vol_options
        req['advanced'] = advance
        req['experimental'] = experimental
        req['deprecated'] = deprecated
        return self._handle_request(self._post, httplib.OK,
                                    "/v1/volumes/%s/options" % vol_name,
                                    json.dumps(req))

    def volume_reset(self, vol_name, options=None):
        """
        Start Gluster Volume.

        :param vol_name: (string) Volume Name
        :param options: (dict) options to set on volume
        :raises: GlusterAPIError or failure
        """
        validate_volume_name(vol_name)

        # TODO need to be implemented

    def volume_info(self, vol_name):
        """
        Gluster Volume Info.

        :param vol_name: (string) Volume Name
        :raises: GlusterAPIError on failure
        """
        validate_volume_name(vol_name)

        return self._handle_request(self._get, httplib.OK,
                                    '/v1/volumes/%s/bricks' % vol_name)

    def volume_status(self, vol_name):
        """
        Gluster Volume Status.

        :param vol_name: (string) Volume Name
        :raises: GlusterAPIError on failure
        """
        validate_volume_name(vol_name)

        return self._handle_request(self._get, httplib.OK,
                                    '/v1/volumes/%s/status' % vol_name)

    def volume_get(self, vol_name, options=None):
        """
        Get Gluster Volume Options.

        :param vol_name: (string) Volume Name
        :param options: (dict) get volumes based on options
        :raises: GlusterAPIError on failure
        """
        validate_volume_name(vol_name)

        # TODO need to be implemented

    def volume_list(self, vol_name=None, key=None, value=None):
        """
        Get Volume list.

        :param vol_name: (string) volume name
        :param key: (string) key to filter volumes
        :param value: (string) value to filter volumes
        :raises: GlusterAPIError on failure
        """
        url = "/v1/volumes"
        param = {}
        if vol_name is None:
            if key:
                param['key'] = key
            if value:
                param['value'] = value
        else:
            validate_volume_name(vol_name)
            url = url + "/" + vol_name

        return self._handle_request(self._get, httplib.OK, url, param=param)
