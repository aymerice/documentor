# VLAN

![VLAN_table_img](http://www.plantuml.com/plantuml/img/0NS1YFv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo12ScbaPsKAOsnXStCWJLDKK5z9RdDqOMvZPGfZR65pSo1MJ45E2cDiONDp8453J0fZR65pSo1GRt9q2cDiONDp84rJL51VGszjRMzkNqbkStHXRcDb2dqALan1JY0kP2u-8453J0fMJ45E83mkTIuWK6zoT0fMJ45E83mjTIqWGd9fP6Tb2bPCGKuWF2vrBY1DKrHGNqbkStHXRcDb2bPCGKuWF2vrBY1DKrHGNqDlRMrlRbz9RdDqOMvZPGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. MACs Validity

### 1.1 macs_invalid

**Type**: _boolean_

If `true`, indicates that MACs on this VLAN are invalid. This might be set by
any agent of the system that decides that MACs are indeed invalid. Eventually
those MACs will be cleared from the system and macs_invalid will revert to
`false`.

## 2. Configuration

### 2.1 description

**Type**: _string_

User provided description of this VLAN.

### 2.2 admin

**Type**: _string_

Administratively configured state of this VLAN. Default is down if not
specified.

### 2.3 id

**Type**: _integer_

The ID of this VLAN.

### 2.4 name

**Type**: _string_

VLAN name.  Should be alphanumeric and no more than about 8 bytes long.

## 3. ACL Configuration

ACL applied to VLANs.

### 3.1 aclv4_in_cfg_version

**Type**: _integer_

The version of the 'aclv4_in_cfg' column. This value is incremented by the
management interface each- CLI/REST/Web UI, etc. every time it changes the
'aclv4_in_cfg' value. An empty value means no ACL has been configured for the
VLAN.

### 3.2 aclv4_in_cfg

**Type**: _uuid_ **refTable**: [ACL](acl.html) **refType**: _weak_



ACL, potentially in flight, desired to be applied to this VLAN, as identified in
the [ACL](acl.html).

### 3.3 aclv4_in_statistics_clear_requested

**Type**: _integer_

The number of times a request was made to clear the ACL statistics for this
VLAN.

## 4. ACL Status

Status of applied ACLs and ACL statistics per VLAN.

### 4.1 aclv4_in_status

**Type**: _string->string_

The status of the last version of 'aclv4_in_cfg' column, that has been processed
by switchd.

### 4.2 aclv4_in_status : state

**Type**: _string_

### 4.3 aclv4_in_status : code

**Type**: _integer_

Numeric error code.  Expected to be 0 when state is 'applied'

### 4.4 aclv4_in_status : message

**Type**: _string_

Detailed reason for error state.  Expected empty when state is 'applied'

### 4.5 aclv4_in_status : version

**Type**: _integer_

The version of aclv4_in_cfg that corresponds to this status.

### 4.6 aclv4_in_statistics

**Type**: _integer->integer_

### 4.7 aclv4_in_statistics : sequence_number

**Type**: _integer_

Statistics for the ACL applied to this port for ACEs that have the 'count'
keyword specified.  Statistics are key/value pairs of ACL sequence number and
integer representing the statistics for that entry.

### 4.8 aclv4_in_statistics_clear_performed

**Type**: _integer_

The number of times that ACL statistics for this VLAN have been cleared..

### 4.9 aclv4_in_applied

**Type**: _uuid_ **refTable**: [ACL](acl.html) **refType**: _weak_



Current, successfully applied ACL to this VLAN, as identified in the [ACL](acl.html)

## 5. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 5.1 other_config

**Type**: _string->string_

### 5.2 external_ids

**Type**: _string->string_

## 6. Hardware VLAN Configuration

### 6.1 hw_vlan_config

**Type**: _string->string_

Key-value pairs that represent the configuration passed down to hardware.

### 6.2 hw_vlan_config : enable

**Type**: _string_

The possible values are "true" and "false".

## 7. VLAN Status

### 7.1 oper_state

**Type**: _string_

Operational state of this VLAN.

### 7.2 oper_state_reason

**Type**: _string_

Human readable reason for the operational state of this VLAN.

## 8. Internal VLAN Config

Information about how this VLAN is used internally by the system. VLAN could be
used for L3 interface, sflow, etc.

### 8.1 internal_usage

**Type**: _string->string_

Key-value pairs that represent how this VLAN is used internally by the system.

### 8.2 internal_usage : l3port

**Type**: _string_

VLAN is used internally by ASIC to configure L3 behavior of the port. The value
is the port name that uses this VLAN.

