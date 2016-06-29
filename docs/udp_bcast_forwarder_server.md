# UDP_Bcast_Forwarder_Server

![UDP_Bcast_Forwarder_Server_table_img](http://www.plantuml.com/plantuml/img/0Ky1iFv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWLKHGNq9ZONDqNqPlSdTXScHbSbzJPN9sPN8AVGfqRsTbT6XbSY1x2cDiONDp85PIHWfZR65pSo1GRt9q2dqALKHGNq9ZONDqNqPlSdTXScHbSbzJPN9sPN8WBcGkFY1MKaOALKHGNq9ZONDqNqPlSdTXScHbSbzJPN9sPN8WBcGkFY1GRt9q2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Each entry represents the match and forward criteria for UDP broadcast packets
received on the port. UDP-Broadcast-Forwarder feature uses these entries to
forward selective UDP broadcast packets received on the routed Port to the
configured server(s).

## 1. UDP Broadcast Forwarder Configuration

### 1.1 udp_dport

**Type**: _integer_

UDP broadcast packets with this destination udp port are forwarded to the
configured server(s).

### 1.2 dest_vrf

**Type**: _uuid_ **refTable**: [VRF](vrf.html) **refType**: _weak_



VRF through which server is reachable.

### 1.3 src_port

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



Reference to the routed port on which packets are receive.

### 1.4 ipv4_ucast_server

**Type**: _string_

List of IPv4 unicast server destinations to which matching UDP broadcast packets
received on the port are duplicated and forwarded.

