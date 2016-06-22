# Nexthop

Global list of all the nexthops as used by the [Route](route.html) table. Each entry
in the [Route](route.html) can have a reference to one or many(for ECMP) entries in
this table.

## 1. Status group

Status information to indicate the current state of the nexthop.

### 1.1 status : arp_resolved key

Indicate if ARP is resolved for this entry. If the ARP entry is missing, this
value is `false`

### 1.2 status : error key

Human readable error string.

### 1.3 status : hw_configured key

Indicate if nexthop programmed in the asic. If the ARP entry is missing, this
value is `false`

## 2. Configuration group

### 2.1 selected column

Indicates if this nexthop is actively participating in forwarding. Multiple
nexthops can exist for each route entry but the routing protocol can indicate if
a particular nexthop should not be used in forwarding. Default is `true`.

### 2.2 weight column

Weight is used to differentially balance the packets. Example: For a route if
there are 2 nexthops nh1 with weight 5 and nh2 with weight 1, then for every 5
packets that uses nh1, one packet will use nh2. In the first release, the above
case is not supported. Only ECMP is supported. Default is 0 (for static routes).

### 2.3 type column

Type of the nexthop. Default is `unicast`.

### 2.4 ip_address column

IP address of the nexthop device.

### 2.5 ports column

List of outgoing ports. Nexthop entries of type `unicast` can have atmost 1
port.

