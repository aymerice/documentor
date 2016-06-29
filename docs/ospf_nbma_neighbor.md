# OSPF_NBMA_Neighbor

![OSPF_NBMA_Neighbor_table_img](http://www.plantuml.com/plantuml/img/0Ga1zlv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16NqvbQMTeOczo2cDiONDp84zJK4PVJa9DGLzEPMbdQ69lSWfz2azJK4PVJa9DGLzEPMbdQ69lSY0yBdKk84zJK4PVJcLfPsXYRt8AQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. Configuration

### 1.1 nbr_address

**Type**: _integer_

The IP address of the NMBA neighbor. The default value is 0, which is invalid.

### 1.2 other_config

**Type**: _string->string_

### 1.3 other_config : priority

**Type**: _integer_

The priority of the NMBA neighbor. The default value is 0.

### 1.4 other_config : poll_interval

**Type**: _integer_

The poll interval (in seconds) of the NMBA neighbor. Default is 60 seconds.

## 2. status

### 2.1 status

**Type**: _string->string_

### 2.2 status : poll_timer_due

**Type**: _integer_

The poll timer due in seconds for the NMBA neighbor. The default value is
poll_interval.

### 2.3 status : state_changes_count

**Type**: _integer_

The total number of state change events. The default value is 0.

### 2.4 interface_name

**Type**: _string_

The name of the interface on which the NBMA Neighbor is adjacent.

### 2.5 nbr_router_id

**Type**: _integer_

The router ID of the neighbor. The default value is 0, which is invalid
router_id.

