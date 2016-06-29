# MSTP_Common_Instance

![MSTP_Common_Instance_table_img](http://www.plantuml.com/plantuml/img/0Nq1Wlv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo12ScbaPsKAOsnXStCWLan1JWfZR65pSo1DKrHGNqDlRMrlRbz9RdDqOMvZPLzGRt9q2cDiONDp84rJL51VGszjRMzkNqbkStHXRcDb2dqAJLDKK5z3RsrjRsvVIMvpT65kOsKWF2rrBI12ScbaPsKAJLDKK5z3RsrjRsvVIMvpT65kOsKWBMGjFY1DKrHGNqDlRMrlRbz9RdDqOMvZPLzGRt9q2arJL51VGszjRMzkNqbkStHXRcDb82vaBZuWLan1JWfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

This represents information regarding a Bridge's Bridge Protocol entity for the
CIST..

## 1. Status

### 1.1 remaining_hops

**Type**: _integer_

The hop count after which this instance MSTP BPDU will be discarded. Default
value is 20

### 1.2 topology_change_count

**Type**: _integer_

The total number of topology changes that have occurred for this instance.

### 1.3 forward_delay_expiry_time

**Type**: _integer_

The epoch time in seconds when forward delay will expire.

### 1.4 oper_tx_hold_count

**Type**: _integer_

The value used by the MSTP transmit state machine to limit the maximum
transmission rate of MST BPDUs within the hello interval.

### 1.5 designated_root

**Type**: _string_

The root bridge name for a CIST instance.

### 1.6 topology_unstable

**Type**: _boolean_

This is set to `true` when a topology change has occurred. Once topology
stabilizes it will be set back to `false`. Default is `false`.

### 1.7 root_path_cost

**Type**: _integer_

The path cost from the transmitting Bridge to the Root Bridge for the MSTI.

### 1.8 root_port

**Type**: _string_

The root port name for a CIST instance.

### 1.9 root_priority

**Type**: _integer_

The root bridge priority. The lower a priority value, the higher the priority.
Default value is 32768.

### 1.10 cist_path_cost

**Type**: _integer_

The path cost from the transmitting bridge to the CIST regional root.

### 1.11 oper_max_age

**Type**: _integer_

Set this value to specify the maximum-aging time(The time a device waits without
receiving spanning tree configuration messages before attempting a
reconfiguration) for all MST instances.

### 1.12 oper_hello_time

**Type**: _integer_

The operating hello timer value for this instance.

### 1.13 regional_root

**Type**: _string_

The regional root for the CIST.

### 1.14 time_since_top_change

**Type**: _integer_

The time last topology change happened for this instance. The format for this is
number of seconds from epoch.

### 1.15 hardware_grp_id

**Type**: _integer_

The hardware spanning tree group ID. Default value is 0.

### 1.16 hello_expiry_time

**Type**: _integer_

The epoch time in seconds after which a hello packet will be sent.

### 1.17 oper_forward_delay

**Type**: _integer_

The forward delay timer value for this instance.

## 2. Configurations

### 2.1 mstp_common_instance_ports

**Type**: _uuid_ **refTable**: [MSTP_Common_Instance_Port](mstp_common_instance_port.html) **refType**: _strong_



CIST configurations for port.

### 2.2 max_age

**Type**: _integer_

Set this value to specify the maximum-aging time(The time a device waits without
receiving spanning tree configuration messages before attempting a
reconfiguration) for all MST instances. Default value is 20.

### 2.3 priority

**Type**: _integer_

Set this value to specify the priority value, configured as a multiple of 4096
The lower a priority value, the higher the priority. Default value is 32768.

### 2.4 hello_time

**Type**: _integer_

The hello time value for this instance. Default value is 2.

### 2.5 bridge_identifier

**Type**: _string_

+ The root bridge ID for CIST. Default value 64 bit string(4 bit priority
+ 12 bit Instance ID
+ 48bit system MAC address)

### 2.6 tx_hold_count

**Type**: _integer_

The value used by the MSTP transmit state machine to limit the maximum
transmission rate of MST BPDUs within the hello interval. Default value is 6.

### 2.7 vlans

**Type**: _uuid_ **refTable**: [VLAN](vlan.html) **refType**: _weak_



VLANs included in the CIST instance.

### 2.8 forward_delay

**Type**: _integer_

The forward delay time value for this instance. Default value is 15.

## 3. Ungrouped

### 3.1 max_hop_count

**Type**: _integer_

