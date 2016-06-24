# MSTP_Instance_Port

![MSTP_Instance_Port_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuKhEIImkLl0D3Wc8zym3YkObfyO7v1ULADZOA6Y4wEHafcUKf1UbfkPfAjZPOLEDJo5kWr2DqDMrm-84BYok0ga4opcavgK0tGy0)

This represents information regarding a specific Port within the bridge's bridge
protocol entity, for a given MSTI.

## 1. Status group

These are status parameters for the port. These values will be calculated at the
time of protocol initialization.

### 1.1 designated_bridge column

The designated bridge for this port.

### 1.2 port_role column

The role of port in the active MSTP topology

### 1.3 designated_root column

The root bridge name for a MSTP instance.

### 1.4 designated_bridge_priority column

The designated bridge priority at this port.

### 1.5 port_state column

The state of the port in the active topology Default value is Blocking.

### 1.6 designated_root_priority column

The priority value for designated port. Default value is 32768.

### 1.7 designated_cost column

The path cost for designated bridge.

### 1.8 designated_port column

The designated port ID.

## 2. Configurations group

### 2.1 port_priority column

Set this value to specify the priority value used along with the switch MAC
address to determine which device is root. Configured as a multiple of 16. The
lower a priority value, the higher the priority. Default value is 128.

### 2.2 admin_path_cost column

The cost to reach root port. Default value is determined from the interface
speed. Bandwidth           Port cost 10 Mbps             2,000,000 100 Mbps
200,000 1 Gigabit Ethernet  20,000 10 Gigabit Ethernet 2,000

### 2.3 port column

Specifies port for the MSTP instance.

