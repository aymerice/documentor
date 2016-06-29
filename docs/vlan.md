# VLAN

![VLAN_table_img](http://www.plantuml.com/plantuml/img/0Lq1elv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo12ScbaPsKAOsnXStCWJLDKK5z9RdDqOMvZPGfZR65pSo1MJ45E2cDiONDp8453J0fZR65pSo1GRt9q2cDiONDp84rJL51VGszjRMzkNqbkStHXRcDb2dqALan1JY0kP2u-8453J0fMJ45E83mkTIuWK6zoT0fMJ45E83mjTIqWGd9fP6Tb2bPCGKuWF2vrBY1DKrHGNqbkStHXRcDb2bPCGKuWF2vrBY1DKrHGNqDlRMrlRbz9RdDqOMvZPGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. MACs Validity group

### 1.1 macs_invalid column

If `true`, indicates that MACs on this VLAN are invalid. This might be set by
any agent of the system that decides that MACs are indeed invalid. Eventually
those MACs will be cleared from the system and macs_invalid will revert to
`false`.

## 2. Configuration group

### 2.1 description column

User provided description of this VLAN.

### 2.2 admin column

Administratively configured state of this VLAN. Default is down if not
specified.

### 2.3 id column

The ID of this VLAN.

### 2.4 name column

VLAN name.  Should be alphanumeric and no more than about 8 bytes long.

## 3. ACL Configuration group

ACL applied to VLANs.

### 3.1 aclv4_in_cfg_version column

The version of the 'aclv4_in_cfg' column. This value is incremented by the
management interface each- CLI/REST/Web UI, etc. every time it changes the
'aclv4_in_cfg' value. An empty value means no ACL has been configured for the
VLAN.

### 3.2 aclv4_in_cfg column

ACL, potentially in flight, desired to be applied to this VLAN, as identified in
the [ACL](acl.html).

### 3.3 aclv4_in_statistics_clear_requested column

The number of times a request was made to clear the ACL statistics for this
VLAN.

## 4. ACL Status group

Status of applied ACLs and ACL statistics per VLAN.

### 4.1 aclv4_in_status column

The status of the last version of 'aclv4_in_cfg' column, that has been processed
by switchd.

### 4.2 aclv4_in_status : state key

### 4.3 aclv4_in_status : code key

Numeric error code.  Expected to be 0 when state is 'applied'

### 4.4 aclv4_in_status : message key

Detailed reason for error state.  Expected empty when state is 'applied'

### 4.5 aclv4_in_status : version key

The version of aclv4_in_cfg that corresponds to this status.

### 4.6 aclv4_in_statistics column

### 4.7 aclv4_in_statistics : sequence_number key

Statistics for the ACL applied to this port for ACEs that have the 'count'
keyword specified.  Statistics are key/value pairs of ACL sequence number and
integer representing the statistics for that entry.

### 4.8 aclv4_in_statistics_clear_performed column

The number of times that ACL statistics for this VLAN have been cleared..

### 4.9 aclv4_in_applied column

Current, successfully applied ACL to this VLAN, as identified in the [ACL](acl.html)

## 5. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 5.1 other_config column

### 5.2 external_ids column

## 6. Hardware VLAN Configuration group

### 6.1 hw_vlan_config column

Key-value pairs that represent the configuration passed down to hardware.

### 6.2 hw_vlan_config : enable key

The possible values are "true" and "false".

## 7. VLAN Status group

### 7.1 oper_state column

Operational state of this VLAN.

### 7.2 oper_state_reason column

Human readable reason for the operational state of this VLAN.

## 8. Internal VLAN Config group

Information about how this VLAN is used internally by the system. VLAN could be
used for L3 interface, sflow, etc.

### 8.1 internal_usage column

Key-value pairs that represent how this VLAN is used internally by the system.

### 8.2 internal_usage : l3port key

VLAN is used internally by ASIC to configure L3 behavior of the port. The value
is the port name that uses this VLAN.

