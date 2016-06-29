# OSPF_Vlink

![OSPF_Vlink_table_img](http://www.plantuml.com/plantuml/img/0Vi01Fz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16NrPiQMvh2cDiONDp84zJK4PVIMvqPN9cOMDb2dqAJrDGHbzMR6bkQo0yBdKk84zJK4PVIMvqPN9cOMDb2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

## 1. Configuration

### 1.1 area_id

**Type**: _integer_

The area ID of the virtual link. Backbone area cannot have virtual link.

### 1.2 peer_router_id

**Type**: _integer_

The peer router ID.

### 1.3 other_config

**Type**: _string->string_

### 1.4 other_config : retransmit_interval

**Type**: _integer_

The estimated time, in seconds, between successive LSAs. The default value is 5
seconds.

### 1.5 other_config : dead_interval

**Type**: _integer_

The time, in seconds, that a neighbor waits for a Hello packet before tearing
down adjacency with local router. The default value is 4 times the hello
interval.

### 1.6 other_config : transmit_delay

**Type**: _integer_

The estimated time, in seconds, to transmit an LSA to a neighbor. The default
value is 1 second.

### 1.7 other_config : hello_interval

**Type**: _integer_

The time, in seconds, between successive Hello packets. The default value is 10
seconds.

### 1.8 ospf_auth_text_key

**Type**: _string_

The authentication key for OSPFv2 authentication type "text".

### 1.9 ospf_auth_type

**Type**: _string_

The type of OSPFv2 authentication. If not set, then the area level
authentication of the transit area, holds for the port.

### 1.10 ospf_auth_md5_keys

**Type**: _integer->string_

The authentication keys for OSPFv2 authentication type "md5" message-digest.

## 2. status

### 2.1 name

**Type**: _string_

The virtual link identifier.

