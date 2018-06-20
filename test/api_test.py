"""
Test module.

The module tests for peer functionalities.
"""
from urlparse import urlparse
import json
import pytest

from glusterapi import Client


class GlusterdConfig(object):
    """GlusterdConfig Class to test the bindings."""

    hostname = ''
    node_list = []
    node_peerid_map = {}

    @classmethod
    def set_node_list(cls, node):
        """Set the node list."""
        cls.node_list.append(node)

    @classmethod
    def set_peer_id(cls, node, resp_id):
        """Set the peer id."""
        cls.node_peerid_map[node] = resp_id

    @classmethod
    def get_peer_id(cls, node):
        """Retrieve the peer id."""
        return cls.node_peerid_map.get(node, "")

    @property
    def get_node_list(self):
        """Retrieve the node list."""
        return self.node_list


Peer = GlusterdConfig()


@pytest.fixture(scope='module')
def gd2client():
    """Initialise all the class member variables."""
    config = json.loads(open('config.json').read())
    endpoint = config["glusterd2"]["endpoint"]
    user = config["glusterd2"]["user"]
    secret = config["glusterd2"]["secret"]
    verify = config["glusterd2"]["verify"]
    # Check for controller node and skip it for probing.
    for node in config["peer"]:
        if node["hostname"].split(':')[0] == urlparse(endpoint).netloc.split(':')[0]:
            continue
        Peer.set_node_list(node["hostname"])
    return Client(endpoint=endpoint, user=user, secret=secret, verify=verify)


def test_peer_add(gd2client):
    """Test for peer addition."""
    node_list = Peer.get_node_list
    for node in node_list:
        _, resp = gd2client.peer_add(host=node)
        # store  peerID of nodes in class variable
        Peer.set_peer_id(node, resp['id'])
        assert bool(resp)


def test_peer_status(gd2client):
    """Test for peer status."""
    status, _ = gd2client.peer_status()
    # assert resp[0]['id'] == Peer.get_peer_id)
    assert status == 200


def test_peer_remove(gd2client):
    """Test for peer removal."""
    node_list = Peer.get_node_list
    for node in node_list:
        _, resp = gd2client.peer_remove(peerid=Peer.get_peer_id(node))
        assert not bool(resp)
