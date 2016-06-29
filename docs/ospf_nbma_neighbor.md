# OSPF_NBMA_Neighbor

![OSPF_NBMA_Neighbor_table_img](http://www.plantuml.com/plantuml/img/0Uy04Fz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16NqvbQMTeOczo2cDiONDp84zJK4PVJa9DGLzEPMbdQ69lSWfz2azJK4PVJa9DGLzEPMbdQ69lSY0yBdKk84zJK4PVJcLfPsXYRt8AQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

## 1. Configuration group

### 1.1 nbr_address column

The IP address of the NMBA neighbor. The default value is 0, which is invalid.

### 1.2 other_config column

### 1.3 other_config : priority key

The priority of the NMBA neighbor. The default value is 0.

### 1.4 other_config : poll_interval key

The poll interval (in seconds) of the NMBA neighbor. Default is 60 seconds.

## 2. status group

### 2.1 status column

### 2.2 status : poll_timer_due key

The poll timer due in seconds for the NMBA neighbor. The default value is
poll_interval.

### 2.3 status : state_changes_count key

The total number of state change events. The default value is 0.

### 2.4 interface_name column

The name of the interface on which the NBMA Neighbor is adjacent.

### 2.5 nbr_router_id column

The router ID of the neighbor. The default value is 0, which is invalid
router_id.

