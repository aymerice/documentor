# MSTP_Instance_Port

![MSTP_Instance_Port_table_img](http://www.plantuml.com/plantuml/img/0J41plv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1DKrHGNqbkStHXRcDbNr1lSdGAOsnXStCWJLDKK5z9RdDqOMvZPGfZR65pSo1GRt9q2dqAJLDKK5z9RdDqOMvZPLzGRt9q83mjTIqWJLDKK5z9RdDqOMvZPGfDKrHGNqbkStHXRcDbNr1lSdGWBcGkFY1GRt9q2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

This represents information regarding a specific Port within the bridge's bridge
protocol entity, for a given MSTI.

## 1. Status

These are status parameters for the port. These values will be calculated at the
time of protocol initialization.

### 1.1 designated_bridge

**Type**: _string_

The designated bridge for this port.

### 1.2 port_role

**Type**: _string_

The role of port in the active MSTP topology

### 1.3 designated_root

**Type**: _string_

The root bridge name for a MSTP instance.

### 1.4 designated_bridge_priority

**Type**: _integer_

The designated bridge priority at this port.

### 1.5 port_state

**Type**: _string_

The state of the port in the active topology Default value is Blocking.

### 1.6 designated_root_priority

**Type**: _integer_

The priority value for designated port. Default value is 32768.

### 1.7 designated_cost

**Type**: _integer_

The path cost for designated bridge.

### 1.8 designated_port

**Type**: _string_

The designated port ID.

## 2. Configurations

### 2.1 port_priority

**Type**: _integer_

Set this value to specify the priority value used along with the switch MAC
address to determine which device is root. Configured as a multiple of 16. The
lower a priority value, the higher the priority. Default value is 128.

### 2.2 admin_path_cost

**Type**: _integer_

The cost to reach root port. Default value is determined from the interface
speed. Bandwidth           Port cost 10 Mbps             2,000,000 100 Mbps
200,000 1 Gigabit Ethernet  20,000 10 Gigabit Ethernet 2,000

### 2.3 port

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



Specifies port for the MSTP instance.

