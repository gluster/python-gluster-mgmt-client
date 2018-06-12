from glusterapi.bitrot import BitrotApis
from glusterapi.device import DeviceApis
from glusterapi.events import EventsApis
from glusterapi.georep import GeorepApis
from glusterapi.peer import PeerApis
from glusterapi.snapshot import SnapshotsApis
from glusterapi.volume import VolumeApis


class Client(VolumeApis, PeerApis, GeorepApis, BitrotApis, DeviceApis,
             EventsApis, SnapshotsApis):
    pass
