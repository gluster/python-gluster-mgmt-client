# Quick Start User Guide

This guide demonstrates how to consume the python bindings for GlusterD-2.0 APIs.
We create a two-node GlusterFS cluster using these bindings.

## Setup
This guide takes the following as an example of IPs for the two nodes:
 * **Node 1**: `192.168.56.101`
 * **Node 2**: `192.168.56.102`
 
 Please follow the GD2 [user-guide](https://github.com/gluster/glusterd2/blob/master/doc/quick-start-user-guide.md)
 to set up GlusterD-2.0 on both the nodes.
 
## Example Usage

    from glusterapi import Client

    client = Client("node1")

    client.peer_add("node2")

    print(client.peer_status())