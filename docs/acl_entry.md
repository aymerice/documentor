# ACL_Entry

## 1. ACL L4 Port Configuration group

L4 Port: specifies the IPv4 L4 port to be used as the minimum value.  It is used
in conjunction with src/dst_l4_port_max and src/dst_l4_port_range_reverse to
determine the desired L4 port functionality:  Applicable to TCP and UDP
protocols.

### 1.1 src_l4_port_range_reverse column

Specifies if the values in src_l4_port_min and src_l4_port_max should be treated
as specifying values not to be matched. Optional parameter for IPv4 ACL entries.
Applicable to TCP and UDP protocols.

### 1.2 dst_l4_port_max column

Destination L4 Port Max: specifies the maximum value It is used in conjunction
with dst_l4_port_min and dst_l4_port_range_reverse to determine the desired
destination L4 port functionality.  Optional parameter for IPv4 ACL entries.

### 1.3 src_l4_port_max column

Source L4 Port Max: specifies the maximum value It is used in conjunction with
src_l4_port_min and src_l4_port_range_reverse to determine the desired source L4
port functionality.  Optional parameter for IPv4 ACL entries.

### 1.4 dst_l4_port_range_reverse column

Specifies if the values in dst_l4_port_min and dst_l4_port_max should be treated
as specifying values not to be matched. Optional parameter for IPv4 ACL entries.
Applicable to TCP and UDP protocols.

### 1.5 src_l4_port_min column

Source L4 Port: specifies the IPv4 L4 source port to be used as the minimum
value.  It is used in conjunction with src_l4_port_max and
src_l4_port_range_reverse to determine the desired source L4 port functionality.
Optional parameter for IPv4 ACL entries.

### 1.6 dst_l4_port_min column

Source L4 Port: specifies the IPv4 L4 source port to be used as the minimum
value.  It is used in conjunction with dst_l4_port_max and
dst_l4_port_range_reverse to determine the desired destination L4 port
functionality.  Optional parameter for IPv4 ACL entries.

