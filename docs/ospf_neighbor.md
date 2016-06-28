# OSPF_Neighbor

![OSPF_Neighbor_table_img](http://www.plantuml.com/plantuml/img/0IO1sVv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16NqvbQMTeOczo2cDiONDp84zJK4PVJa9DGLzEPMbdQ69lSWfZR65pSo1FKr16NqbkT6LoPc5ZPGfz2azJK4PVJcLfPsXYRt8WF2rrBI1FKr16NqbkT6LoPc5ZPGfFKr16NqvbQMTeOczo82vaBZuWJrDGHbzEGar1NqvbQMTeOczo2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. status group

### 1.1 status : last_up_timestamp key

The duration since when the state of the neighbor is seen. The default value is
0.

### 1.2 status : dead_timer_due key

The time left for the dead timer of the neighbor to expire. The default value is
the dead_interval for the interface.

### 1.3 nbr_priority column

The priority of the neighbor. The default value is 255.

### 1.4 nfsm_state column

OSPFv2 Neighbor FSM states. The default value is "down".

### 1.5 nbr_if_addr column

The interface address of the OSPFv2 Neighbor on which the neighbor relationship
is established. The default value is 0, which is invalid if_address.

### 1.6 nbr_options column

The neighbor options or capabilities such as Opaque LSA capability, Demand
Circuit, External Attribute LSA capability, and so on.

### 1.7 bdr column

The router ID of the Backup Designated Router, as reported by the neighbor. The
default value is 0.

### 1.8 dr column

The router ID of the Designated Router, as reported by the neighbor. The default
value is 0.

### 1.9 nbr_router_id column

The Neighbor Router ID is used to identify the neighbor. The default value is 0,
which is invalid router_id.

## 2. statistics group

### 2.1 statistics : ls_request_count key

The total number of link state request packets.

### 2.2 statistics : ls_retransmit_count key

The total number of link state packets retransmitted.

### 2.3 statistics : db_summary_count key

The total number of DataBase summary reports.

### 2.4 statistics : state_changes_count key

The total number of state change events on this interface.

## 3. Configuration group

### 3.1 nbma_nbr column

The NBMA Neighbor related configurations, and statuses. This is valid in case of
NBMA Neighbor only.

