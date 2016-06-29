# DHCP_Relay

![DHCP_Relay_table_img](http://www.plantuml.com/plantuml/img/0Hy1uFv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWH4X3K5zIPMnXUGfz2dHlPsLqQ6Lo87iAOsnXStCWLb962cDiONDp851lSdGAVGf4I4DGNr9bR65v82vaBZuWK6zoT0f4I4DGNr9bR65v82vaBZuWLb962cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Placeholder for a set of server configuration entries. DHCP-Relay feature uses
these entries to forward matching DHCP broadcast packets received on the layer3
Port.

## 1. DHCP-Relay Configuration

### 1.1 ipv6_mcast_server

**Type**: _string->uuid_ **refTable**: [Port](port.html) **refType**: _weak_



List of IPv6 multicast or link local server destinations to which matching DHCP
broadcast packets received on the port are duplciated and forwarded. Value of
this key referenes a Port table entry, packets matching the criteria are
forwarded to the server through this port. A maximum of 8 IPv6 server
configurations are allowed. This count includes IPv6 unicast server
configurations from the column "ipv6_ucast_server".

### 1.2 other_config

**Type**: _string->string_

### 1.3 other_config : bootp_gateway

**Type**: _string_

Provides a way to configure a gateway address for the DHCP relay agent to use
for DHCP requests, rather than the DHCP relay agent automatically assigning the
lowest-numbered IP address.

### 1.4 ipv6_ucast_server

**Type**: _string_

List of IPv6 unicast server destinations to which DHCP broadcast packets
received on the port are dulicated and forwarded. A maximum of 8 IPv6 server
configurations are allowed. The count includes IPv6 multicast and link local
server configuration from the column "ipv6_mcast_server".

### 1.5 vrf

**Type**: _uuid_ **refTable**: [VRF](vrf.html) **refType**: _weak_



VRF through which DHCP server is reachable.

### 1.6 ipv4_ucast_server

**Type**: _string_

List of IPv4 unicast server destinations to which DHCP broadcast packets
received on the port are duplicated and forwarded. A maximum of 8 ipv4 unicast
server configurations are allowed.

### 1.7 port

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



Layer 3 Port on which the configuration is made.

