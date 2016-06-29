# VRF

![VRF_table_img](http://www.plantuml.com/plantuml/img/0Rm3G_n0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJKDCGKSAOsnXStCWKcLZTN9pQNPbNqvbU7HeRt0AOsnXStCWKczrT6KAOsnXStCWKtbpT6Lj2cDiONDp84vKK5z1StDlOsbXT6blRWfZR65pSo1LH51VGcDXStHVHczoTs5oP6LoNrDbSdPbSWfZR65pSo14I4DGNr9bR65v2cDiONDp84vbQMTeOczo2cDiONDp8497K5zIRtLqPGfz2dHlPsLqQ6Lo87iAOsnXStCWH4X3K5zJPN9sPN8AOsnXStCWLb962cDiONDp851lSdGAVGfMKaOWF2raBI1EL51VGNDpRsDfONHfRsuALb9683mjP2qWKtbpT6Lj2bPIHY0yBcGk85L4K5z2Os5pT5z6Rt9tON9aPN9VKsLoTcLo2bPIHY0yBMGj84vbQMTeOczo2bPIHY0yBcGk84H8Gr1VKcLiONaALb9683mjP2qWGaTGNr9lTNHb2bPIHY0jP2q-851lSdGALb9683mjP2qWKczrT6KALb9682raBJuWH4X3K5zJPN9sPN8ALb9683mkP2uWJKDCGKSALb9683mjP2qWKcLZTN9pQNPbNqvbU7HeRt0AJKDCGKSWBLjeQMHaPMvTBI1IPMDrSdDfTcLVJcLuT6XlS0fIPMDrSdDfTcLVJcLuT6XlS20jMsXfP6HbRbqj859lTNHb2b9lTNHb82rRQ6baP6LkNIqWJKDCGKSAKtbpT6Lj82rRQ6baP6LkNIqWJbHGNq5pSszZQM5qQMzk2avKK5z1StDlOsbXT6blRY0jMsXfP6HbRbqj85L4K5z2Os5pT5z6Rt9tON9aPN9VKsLoTcLo2bL4K5z2Os5pT5z6Rt9tON9aPN9VKsLoTcLo82rRQ6baP6LkNIqWKtbpT6Lj2aH8Gr1VKcLiONaWBLjeQMHaPMvTBI1EPMbdQ69lSWfEPMbdQ69lSY0jMsXfP6HbRbqj8497K5zIRtLqPGf2Hr1VKczrT6KWBLjeQMHaPMvTBI14I4DGNr9bR65v2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Each entry in this table represents a single routing domain, commonly known as
Virtual Routing and Forwarding.

## 1. Status

### 1.1 status

**Type**: _string->string_

### 1.2 status : namespace_ready

**Type**: _boolean_

Indicates whether Linux namespace exists for this VRF. If not set, the assumed
value is false.

## 2. Configuration

### 2.1 ospf_routers

**Type**: _integer->uuid_ **refTable**: [OSPF_Router](ospf_router.html) **refType**: _strong_



The list of all the OSPFv2 Router instances.

### 2.2 name

**Type**: _string_

VRF identifier. Should be alphanumeric. VRF names must be unique.

### 2.3 active_router_id

**Type**: _string_

Router-ID (in IPv4 format) that is currently used in the system, unless
overridden by protocol specific one.

### 2.4 ports

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _strong_



Ports included in the VRF.

### 2.5 table_id

**Type**: _integer_

Kernel table_id assigned for routing table of this VRF.

### 2.6 bgp_routers

**Type**: _integer->uuid_ **refTable**: [BGP_Router](bgp_router.html) **refType**: _strong_



BGP routers keyed by ASN value.

### 2.7 dhcp_server

**Type**: _uuid_ **refTable**: [DHCP_Server](dhcp_server.html) **refType**: _strong_



DHCP Server in the VRF.

## 3. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 3.1 other_config

**Type**: _string->string_

### 3.2 external_ids

**Type**: _string->string_

