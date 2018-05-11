from volume import VolumeApis
from georep import GeorepApis
from peer import PeerApis


class Client(VolumeApis, PeerApis, GeorepApis):
    pass
