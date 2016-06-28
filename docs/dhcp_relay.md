# DHCP_Relay

![DHCP_Relay_table_img](http://www.plantuml.com/plantuml/img/0GK1-lv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWH4X3K5zIPMnXUGfz2dHlPsLqQ6Lo87iAOsnXStCWLb962cDiONDp851lSdGAVGf4I4DGNr9bR65v82vaBZuWK6zoT0f4I4DGNr9bR65v82vaBZuWLb962cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Placeholder for a set of server configuration entries. DHCP-Relay feature uses
these entries to forward matching DHCP broadcast packets received on the layer3
Port.

## 1. DHCP-Relay Configuration group

### 1.1 ipv6_mcast_server column

List of IPv6 multicast or link local server destinations to which matching DHCP
broadcast packets received on the port are duplciated and forwarded. Value of
this key referenes a Port table entry, packets matching the criteria are
forwarded to the server through this port. A maximum of 8 IPv6 server
configurations are allowed. This count includes IPv6 unicast server
configurations from the column "ipv6_ucast_server".

### 1.2 other_config : bootp_gateway key

Provides a way to configure a gateway address for the DHCP relay agent to use
for DHCP requests, rather than the DHCP relay agent automatically assigning the
lowest-numbered IP address.

### 1.3 ipv6_ucast_server column

List of IPv6 unicast server destinations to which DHCP broadcast packets
received on the port are dulicated and forwarded. A maximum of 8 IPv6 server
configurations are allowed. The count includes IPv6 multicast and link local
server configuration from the column "ipv6_mcast_server".

### 1.4 vrf column

VRF through which DHCP server is reachable.

### 1.5 ipv4_ucast_server column

List of IPv4 unicast server destinations to which DHCP broadcast packets
received on the port are duplicated and forwarded. A maximum of 8 ipv4 unicast
server configurations are allowed.

### 1.6 port column

Layer 3 Port on which the configuration is made.

