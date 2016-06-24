# Recursive_Nexthop

![Recursive_Nexthop_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuIf8JCvEJ4zLK0hApozH24bCoaajLbAevb80WkISnE9YXQ3KvDAYuioor7Y_r8gIZFm21HiR1OqGdPpCz8oIzABKr3nD1JixhbekYFAm83Vi2Y3I0Vb59TZbCUtHrRK36OT31cGIbqDgNWhG6m00)

Recursive next hop resolution. When a protocol has a new recursive next hop and
its reachability is unknown, the protocol requests the recursive next hop to be
resolved. The result is represented as nh_ips, nh_metric, and nh_ports.

## 1. Next hop resolution group

### 1.1 rnh_ip column

IPv4 or IPv6 recursive next hop address to be resolved. Example 192.168.0.2

### 1.2 rnh_from column

This indicates from which protocol the request comes.

### 1.3 nh_metric column

The cost to reach the forwarding next hops that the recursive next hop is
resolved to.

### 1.4 vrf column

Reference to the VRF to which this entry belongs to.

### 1.5 nh_ips column

The IPv4 or IPv6 addresses of the forwarding next hops that the recursive next
hop is resolved to. It is possible that the recursive next hop is resolved to a
single forwarding next hop or a ECMP which consists a list of forwarding next
hops. Example 12.1.0.2

### 1.6 nh_ports column

The ports of the forwarding next hops that the recursive next hop is resolved
to. It is possible that the recursive next hop is resolved to a single
forwarding next hop or a ECMP which consists a list of next hops.

