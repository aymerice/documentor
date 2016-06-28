# VRF

![VRF_table_img](http://www.plantuml.com/plantuml/img/0Q83NVn0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJKDCGKSAOsnXStCWKcLZTN9pQNPbNqvbU7HeRt0AOsnXStCWKczrT6KAOsnXStCWKtbpT6Lj2cDiONDp84vKK5z1StDlOsbXT6blRWfZR65pSo1LH51VGcDXStHVHczoTs5oP6LoNrDbSdPbSWfZR65pSo14I4DGNr9bR65v2cDiONDp84vbQMTeOczo2cDiONDp8497K5zIRtLqPGfz2dHlPsLqQ6Lo87iAOsnXStCWH4X3K5zJPN9sPN8AOsnXStCWLb962cDiONDp851lSdGAVGfMKaOWF2raBI1EL51VGNDpRsDfONHfRsuALb9683mjP2qWKtbpT6Lj2bPIHY0yBcGk85L4K5z2Os5pT5z6Rt9tON9aPN9VKsLoTcLo2bPIHY0yBMGj84vbQMTeOczo2bPIHY0yBcGk84H8Gr1VKcLiONaALb9683mjP2qWGaTGNr9lTNHb2bPIHY0jP2q-851lSdGALb9683mjP2qWKczrT6KALb9682raBJuWH4X3K5zJPN9sPN8ALb9683mkP2uWJKDCGKSALb9683mjP2qWKcLZTN9pQNPbNqvbU7HeRt0AJKDCGKSWBLjeQMHaPMvTBI1IPMDrSdDfTcLVJcLuT6XlS0fIPMDrSdDfTcLVJcLuT6XlS20jMsXfP6HbRbqj859lTNHb2b9lTNHb82rRQ6baP6LkNIqWJKDCGKSAKtbpT6Lj82rRQ6baP6LkNIqWJbHGNq5pSszZQM5qQMzk2avKK5z1StDlOsbXT6blRY0jMsXfP6HbRbqj85L4K5z2Os5pT5z6Rt9tON9aPN9VKsLoTcLo2bL4K5z2Os5pT5z6Rt9tON9aPN9VKsLoTcLo82rRQ6baP6LkNIqWKtbpT6Lj2aH8Gr1VKcLiONaWBLjeQMHaPMvTBI1EPMbdQ69lSWfEPMbdQ69lSY0jMsXfP6HbRbqj8497K5zIRtLqPGf2Hr1VKczrT6KWBLjeQMHaPMvTBI14I4DGNr9bR65v2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Each entry in this table represents a single routing domain, commonly known as
Virtual Routing and Forwarding.

## 1. Status group

### 1.1 status : namespace_ready key

Indicates whether Linux namespace exists for this VRF. If not set, the assumed
value is false.

## 2. Configuration group

### 2.1 ospf_routers column

The list of all the OSPFv2 Router instances.

### 2.2 name column

VRF identifier. Should be alphanumeric. VRF names must be unique.

### 2.3 active_router_id column

Router-ID (in IPv4 format) that is currently used in the system, unless
overridden by protocol specific one.

### 2.4 ports column

Ports included in the VRF.

### 2.5 table_id column

Kernel table_id assigned for routing table of this VRF.

### 2.6 bgp_routers column

BGP routers keyed by ASN value.

### 2.7 dhcp_server column

DHCP Server in the VRF.

