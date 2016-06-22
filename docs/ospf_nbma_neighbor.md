# OSPF_NBMA_Neighbor

## 1. Configuration group

### 1.1 nbr_address column

The IP address of the NMBA neighbor. The default value is 0, which is invalid.

### 1.2 other_config : priority key

The priority of the NMBA neighbor. The default value is 0.

### 1.3 other_config : poll_interval key

The poll interval (in seconds) of the NMBA neighbor. Default is 60 seconds.

## 2. status group

### 2.1 status : poll_timer_due key

The poll timer due in seconds for the NMBA neighbor. The default value is
poll_interval.

### 2.2 status : state_changes_count key

The total number of state change events. The default value is 0.

### 2.3 interface_name column

The name of the interface on which the NBMA Neighbor is adjacent.

### 2.4 nbr_router_id column

The router ID of the neighbor. The default value is 0, which is invalid
router_id.

