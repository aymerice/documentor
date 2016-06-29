# ACL_Entry

![ACL_Entry_table_img](http://www.plantuml.com/plantuml/img/0SO0EVz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo11GqnVHMvqSdaAVGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. Ungrouped

### 1.1 comment

**Type**: _string_

Comment to associate with the specified ACE. Optional parameter.

### 1.2 count

**Type**: _boolean_

Count Action: enable hit counts in hardware for packets that match this ACL
entry Optional parameter for IPv4 ACL entries The following value is accepted:
true

### 1.3 protocol

**Type**: _integer_

IPv4 Protocol Optional parameter.  If no protocol is specified the ACE will not
match on protocol.

### 1.4 log

**Type**: _boolean_

Log Action: enable ACL logging for packets that match this ACL entry Optional
parameter for IPv4 ACL entries The following value is accepted: true

### 1.5 other_config

**Type**: _string->string_

### 1.6 src_ip

**Type**: _string_

Source IPv4 Address: Optional parameter.  If no IP address is specified the ACE
will not match on source IP address.  The following IPv4 address formats are
accepted: X.X.X.X/X.X.X.X

### 1.7 action

**Type**: _string_

Match Action: Optional parameter for IPv4 ACL entries. There are two types:
"permit" and "deny" If no action is specified the ACE will not be programmed in
hw.

### 1.8 dst_ip

**Type**: _string_

Destination IPv4 Address: Optional parameter.  If no IP address is specified the
ACE will not match on destination IP address  The following IPv4 address formats
are accepted: X.X.X.X/X.X.X.X

### 1.9 external_ids

**Type**: _string->string_

## 2. ACL L4 Port Configuration

L4 Port: specifies the IPv4 L4 port to be used as the minimum value.  It is used
in conjunction with src/dst_l4_port_max and src/dst_l4_port_range_reverse to
determine the desired L4 port functionality:  Applicable to TCP and UDP
protocols.

### 2.1 src_l4_port_range_reverse

**Type**: _boolean_

Specifies if the values in src_l4_port_min and src_l4_port_max should be treated
as specifying values not to be matched. Optional parameter for IPv4 ACL entries.
Applicable to TCP and UDP protocols.

### 2.2 dst_l4_port_max

**Type**: _integer_

Destination L4 Port Max: specifies the maximum value It is used in conjunction
with dst_l4_port_min and dst_l4_port_range_reverse to determine the desired
destination L4 port functionality.  Optional parameter for IPv4 ACL entries.

### 2.3 src_l4_port_max

**Type**: _integer_

Source L4 Port Max: specifies the maximum value It is used in conjunction with
src_l4_port_min and src_l4_port_range_reverse to determine the desired source L4
port functionality.  Optional parameter for IPv4 ACL entries.

### 2.4 dst_l4_port_range_reverse

**Type**: _boolean_

Specifies if the values in dst_l4_port_min and dst_l4_port_max should be treated
as specifying values not to be matched. Optional parameter for IPv4 ACL entries.
Applicable to TCP and UDP protocols.

### 2.5 src_l4_port_min

**Type**: _integer_

Source L4 Port: specifies the IPv4 L4 source port to be used as the minimum
value.  It is used in conjunction with src_l4_port_max and
src_l4_port_range_reverse to determine the desired source L4 port functionality.
Optional parameter for IPv4 ACL entries.

### 2.6 dst_l4_port_min

**Type**: _integer_

Source L4 Port: specifies the IPv4 L4 source port to be used as the minimum
value.  It is used in conjunction with dst_l4_port_max and
dst_l4_port_range_reverse to determine the desired destination L4 port
functionality.  Optional parameter for IPv4 ACL entries.

