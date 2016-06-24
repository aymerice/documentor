# MSTP_Instance

![MSTP_Instance_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuKhEIImkLl0D3Wc8zym3YkObfyO7v1ULADZOA6Y4wEHafcUKf1UbfkPfAjZPGLM7-JZwuPD7CGsxGYvKDRgwTbZSW4KHo6ekBeVKl1IGum40)

This represents information regarding a Bridge's Bridge Protocol entity for the
specified Spanning Tree instance.

## 1. Configurations group

### 1.1 mstp_instance_ports column

MSTP configuration for port.

### 1.2 vlans column

VLANs included in the MSTP instance.

### 1.3 priority column

Set this value to specify the priority value, configured as a multiple of 4096
The lower a priority value, the higher the priority. Default value is 32768.

### 1.4 bridge_identifier column

+ The root bridge ID for CIST. Default value 64 bit string(4 bit priority
+ 12 bit Instance ID
+ 48bit system MAC address)

## 2. Status group

These are status parameters for a particular MSTP instance. These values will be
calculated at the time of protocol initialization.

### 2.1 time_since_top_change column

The time last topology change happened for this instance. The format for this is
number of seconds from epoch.

### 2.2 hardware_grp_id column

The hardware spanning tree group ID. Default value is 0.

### 2.3 designated_root column

The root bridge name for a MSTP instance.

### 2.4 topology_change_count column

The total number of topology changes that have occurred for this instance.

### 2.5 topology_unstable column

This is set to `true` when a topology change has occurred. Once topology
stabilizes it will be set back to `false`. Default is `false`.

### 2.6 root_path_cost column

The path cost from the transmitting Bridge to the Root Bridge for the MSTI.

### 2.7 root_port column

Specifies the root port name for a MSTP instance.

### 2.8 root_priority column

The root bridge priority. The lower a priority value, the higher the priority.
Default value is 32768.

