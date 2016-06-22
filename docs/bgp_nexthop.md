# BGP_Nexthop

List of all nexthops used by BGP. Each entry in the BGP RIB can have a reference
to one or many (for ECMP) nexthop entries.

## 1. Status group

### 1.1 ip_address column

IP address of the nexthop device.

### 1.2 type column

Type of the nexthop. Default is `unicast`.

