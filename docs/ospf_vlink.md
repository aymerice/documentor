# OSPF_Vlink

![OSPF_Vlink_table_img](http://www.plantuml.com/plantuml/img/0U407lz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16NrPiQMvh2cDiONDp84zJK4PVIMvqPN9cOMDb2dqAJrDGHbzMR6bkQo0yBdKk84zJK4PVIMvqPN9cOMDb2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. Configuration group

### 1.1 area_id column

The area ID of the virtual link. Backbone area cannot have virtual link.

### 1.2 peer_router_id column

The peer router ID.

### 1.3 other_config : retransmit_interval key

The estimated time, in seconds, between successive LSAs. The default value is 5
seconds.

### 1.4 other_config : dead_interval key

The time, in seconds, that a neighbor waits for a Hello packet before tearing
down adjacency with local router. The default value is 4 times the hello
interval.

### 1.5 other_config : transmit_delay key

The estimated time, in seconds, to transmit an LSA to a neighbor. The default
value is 1 second.

### 1.6 other_config : hello_interval key

The time, in seconds, between successive Hello packets. The default value is 10
seconds.

### 1.7 ospf_auth_text_key column

The authentication key for OSPFv2 authentication type "text".

### 1.8 ospf_auth_type column

The type of OSPFv2 authentication. If not set, then the area level
authentication of the transit area, holds for the port.

### 1.9 ospf_auth_md5_keys column

The authentication keys for OSPFv2 authentication type "md5" message-digest.

## 2. status group

### 2.1 name column

The virtual link identifier.

