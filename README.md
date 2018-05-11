# glusterapi-python

Python bindings for gluster management APIs

## Quick Start

    from glusterapi import Client

    client = Client("node1")

    print(client.peer_status())
