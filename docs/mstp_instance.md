# MSTP_Instance

![MSTP_Instance_table_img](http://www.plantuml.com/plantuml/img/0Im1q_v0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1DKrHGNqbkStHXRcDbNr1lSdGAOsnXStCWLan1JWfZR65pSo1DKrHGNqbkStHXRcDb2dqAJLDKK5z9RdDqOMvZPI0jP2q-84rJL51VIMvpT65kOsLVK6zoT0fDKrHGNqbkStHXRcDb82vaBZuWLan1JWfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

This represents information regarding a Bridge's Bridge Protocol entity for the
specified Spanning Tree instance.

## 1. Configurations

### 1.1 mstp_instance_ports

**Type**: _uuid_ **refTable**: [MSTP_Instance_Port](mstp_instance_port.html) **refType**: _strong_



MSTP configuration for port.

### 1.2 vlans

**Type**: _uuid_ **refTable**: [VLAN](vlan.html) **refType**: _weak_



VLANs included in the MSTP instance.

### 1.3 priority

**Type**: _integer_

Set this value to specify the priority value, configured as a multiple of 4096
The lower a priority value, the higher the priority. Default value is 32768.

### 1.4 bridge_identifier

**Type**: _string_

+ The root bridge ID for CIST. Default value 64 bit string(4 bit priority
+ 12 bit Instance ID
+ 48bit system MAC address)

## 2. Status

These are status parameters for a particular MSTP instance. These values will be
calculated at the time of protocol initialization.

### 2.1 time_since_top_change

**Type**: _integer_

The time last topology change happened for this instance. The format for this is
number of seconds from epoch.

### 2.2 hardware_grp_id

**Type**: _integer_

The hardware spanning tree group ID. Default value is 0.

### 2.3 designated_root

**Type**: _string_

The root bridge name for a MSTP instance.

### 2.4 topology_change_count

**Type**: _integer_

The total number of topology changes that have occurred for this instance.

### 2.5 topology_unstable

**Type**: _boolean_

This is set to `true` when a topology change has occurred. Once topology
stabilizes it will be set back to `false`. Default is `false`.

### 2.6 root_path_cost

**Type**: _integer_

The path cost from the transmitting Bridge to the Root Bridge for the MSTI.

### 2.7 root_port

**Type**: _string_

Specifies the root port name for a MSTP instance.

### 2.8 root_priority

**Type**: _integer_

The root bridge priority. The lower a priority value, the higher the priority.
Default value is 32768.

