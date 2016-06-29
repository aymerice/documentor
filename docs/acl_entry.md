# ACL_Entry

![ACL_Entry_table_img](http://www.plantuml.com/plantuml/img/0Qm0K_z0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo11GqnVHMvqSdaAVGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. Ungrouped group

### 1.1 comment column

Comment to associate with the specified ACE. Optional parameter.

### 1.2 count column

Count Action: enable hit counts in hardware for packets that match this ACL
entry Optional parameter for IPv4 ACL entries The following value is accepted:
true

### 1.3 protocol column

IPv4 Protocol Optional parameter.  If no protocol is specified the ACE will not
match on protocol.

### 1.4 log column

Log Action: enable ACL logging for packets that match this ACL entry Optional
parameter for IPv4 ACL entries The following value is accepted: true

### 1.5 other_config column

### 1.6 src_ip column

Source IPv4 Address: Optional parameter.  If no IP address is specified the ACE
will not match on source IP address.  The following IPv4 address formats are
accepted: X.X.X.X/X.X.X.X

### 1.7 action column

Match Action: Optional parameter for IPv4 ACL entries. There are two types:
"permit" and "deny" If no action is specified the ACE will not be programmed in
hw.

### 1.8 dst_ip column

Destination IPv4 Address: Optional parameter.  If no IP address is specified the
ACE will not match on destination IP address  The following IPv4 address formats
are accepted: X.X.X.X/X.X.X.X

### 1.9 external_ids column

## 2. ACL L4 Port Configuration group

L4 Port: specifies the IPv4 L4 port to be used as the minimum value.  It is used
in conjunction with src/dst_l4_port_max and src/dst_l4_port_range_reverse to
determine the desired L4 port functionality:  Applicable to TCP and UDP
protocols.

### 2.1 src_l4_port_range_reverse column

Specifies if the values in src_l4_port_min and src_l4_port_max should be treated
as specifying values not to be matched. Optional parameter for IPv4 ACL entries.
Applicable to TCP and UDP protocols.

### 2.2 dst_l4_port_max column

Destination L4 Port Max: specifies the maximum value It is used in conjunction
with dst_l4_port_min and dst_l4_port_range_reverse to determine the desired
destination L4 port functionality.  Optional parameter for IPv4 ACL entries.

### 2.3 src_l4_port_max column

Source L4 Port Max: specifies the maximum value It is used in conjunction with
src_l4_port_min and src_l4_port_range_reverse to determine the desired source L4
port functionality.  Optional parameter for IPv4 ACL entries.

### 2.4 dst_l4_port_range_reverse column

Specifies if the values in dst_l4_port_min and dst_l4_port_max should be treated
as specifying values not to be matched. Optional parameter for IPv4 ACL entries.
Applicable to TCP and UDP protocols.

### 2.5 src_l4_port_min column

Source L4 Port: specifies the IPv4 L4 source port to be used as the minimum
value.  It is used in conjunction with src_l4_port_max and
src_l4_port_range_reverse to determine the desired source L4 port functionality.
Optional parameter for IPv4 ACL entries.

### 2.6 dst_l4_port_min column

Source L4 Port: specifies the IPv4 L4 source port to be used as the minimum
value.  It is used in conjunction with dst_l4_port_max and
dst_l4_port_range_reverse to determine the desired destination L4 port
functionality.  Optional parameter for IPv4 ACL entries.

