# OSPF_Neighbor

![OSPF_Neighbor_table_img](http://www.plantuml.com/plantuml/img/0K01l_v0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16NqvbQMTeOczo2cDiONDp84zJK4PVJa9DGLzEPMbdQ69lSWfZR65pSo1FKr16NqbkT6LoPc5ZPGfz2azJK4PVJcLfPsXYRt8WF2rrBI1FKr16NqbkT6LoPc5ZPGfFKr16NqvbQMTeOczo82vaBZuWJrDGHbzEGar1NqvbQMTeOczo2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

## 1. status

### 1.1 status

**Type**: _string->string_

### 1.2 status : last_up_timestamp

**Type**: _integer_

The duration since when the state of the neighbor is seen. The default value is
0.

### 1.3 status : dead_timer_due

**Type**: _integer_

The time left for the dead timer of the neighbor to expire. The default value is
the dead_interval for the interface.

### 1.4 nbr_priority

**Type**: _integer_

The priority of the neighbor. The default value is 255.

### 1.5 nfsm_state

**Type**: _string_

OSPFv2 Neighbor FSM states. The default value is "down".

### 1.6 nbr_if_addr

**Type**: _integer_

The interface address of the OSPFv2 Neighbor on which the neighbor relationship
is established. The default value is 0, which is invalid if_address.

### 1.7 nbr_options

**Type**: _string_

The neighbor options or capabilities such as Opaque LSA capability, Demand
Circuit, External Attribute LSA capability, and so on.

### 1.8 bdr

**Type**: _integer_

The router ID of the Backup Designated Router, as reported by the neighbor. The
default value is 0.

### 1.9 dr

**Type**: _integer_

The router ID of the Designated Router, as reported by the neighbor. The default
value is 0.

### 1.10 nbr_router_id

**Type**: _integer_

The Neighbor Router ID is used to identify the neighbor. The default value is 0,
which is invalid router_id.

## 2. statistics

### 2.1 statistics

**Type**: _string->integer_

### 2.2 statistics : ls_request_count

**Type**: _integer_

The total number of link state request packets.

### 2.3 statistics : ls_retransmit_count

**Type**: _integer_

The total number of link state packets retransmitted.

### 2.4 statistics : db_summary_count

**Type**: _integer_

The total number of DataBase summary reports.

### 2.5 statistics : state_changes_count

**Type**: _integer_

The total number of state change events on this interface.

## 3. Configuration

### 3.1 nbma_nbr

**Type**: _uuid_ **refTable**: [OSPF_NBMA_Neighbor](ospf_nbma_neighbor.html) **refType**: _weak_



The NBMA Neighbor related configurations, and statuses. This is valid in case of
NBMA Neighbor only.

