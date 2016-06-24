# BGP_Route

![BGP_Route_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuIf8JCvEJ4zLK0hApozH24bCoaajLbAevb80WkISnE9Y1IVtWFYW_DAIL0KR6mMD49sSpFICalIYrDGyJGKxEwvQBYw4Eh_KYfAC_0BiAY7AmeBSi4jp8IpIrRK3gKCJGRA0YyiXDIy5v7u0)

BGP local RIB.

## 1. BGP Routes group

### 1.1 origin column

Origin of the BGP route. Allowed values are
<mark>egp</mark>,<mark>igp</mark>,<mark>incomplete</mark> igp origin code
specifies whether route entry originated from an Interior Gateway Protocol (IGP)
and was advertised with a network router configuration command. egp origin code
specifies whether route entry originated from an Exterior Gateway Protocol
(EGP). incomplete origin code is assigned to redistributed routes. Default value
is igp.

### 1.2 weight column

Weight of the BGP route. Default value is 32768

### 1.3 metric column

This is the BGP Multi Exit Discriminator (MED) attribute used in best path
selection. Default value is 0

### 1.4 creation_time column

Time in seconds, at which the route arrived from the neighbor. Value is the
number of seconds elapsed since epoch. Default value is 0.

### 1.5 community column

Space delimited list of community names for the route. No value means that no
community names are associated with the route.

### 1.6 prefix column

IPv4 or IPv6 destination prefix and mask in the address/mask format. Example
192.168.0.0/16

### 1.7 address_family column

Represents the address family for this entry. Default value is `ipv4`.

### 1.8 aggregator column

IP address of the BGP node responsible for route aggregation. Value is empty if
route is not aggregated.

### 1.9 aspath column

Aspath for a BGP route. Aspath is the list of autonomous system numbers of the
BGP nodes traversed by the route before reaching local node. Aspath contains
key-value pairs with keys corresponding to the position of the autonomous system
number in the list of autonomous system numbers and values corresponding to
autonomous system numbers.

### 1.10 sub_address_family column

Represents subsequent address family identifier such as unicast, multicast or
MPLS VPN. Default is `unicast`.

### 1.11 aggregator_as column

Originating AS number of the aggregate route. Default value is 0.

### 1.12 ecommunity column

Space delimited list of extended community names for the route. No value means
that no extended community names are associated with the route.

### 1.13 vrf column

Reference to the VRF to which this route belongs.

### 1.14 protocol_iBGP column

Specifies whether the route was learned through iBGP session. Default value is
false.

### 1.15 aggregate column

True if notification is sent to upstream routers that the route is aggregated.
Default value is false.

### 1.16 protocol_internal column

Specifies whether the route originated locally on the BGP peer. Default value is
false.

### 1.17 distance column

Administrative distance for the route entry. Default value is 0.

### 1.18 flags column

Flags attibute of the BGP route.

1. <mark>DAMPED</mark> - Suppress routes from being advertised due to flapping.
1. <mark>HISTORY</mark> - Router does not have a best path for the route based
on historical information.
1. <mark>STALE</mark> - Used with nonstop forwarding to indicate that the route
is stale and needs to be refreshed when the peer is reestablished.
1. <mark>VALID</mark> - Route has a valid next-hop.
1. <mark>DMED_CHECK</mark> - Route is evaluated as part of an effort to identify
preferred entry point into local AS from neighboring autonomous system.
1. <mark>DMED_SELECTED</mark> - Route is selected as preferred entry point into
local AS from neighboring autonomous system.
1. <mark>REMOVED</mark> - Route has been removed from list of advertised routes
to neighboring autonomous system.
1. <mark>SELECTED</mark> - Route had been selected as best path to destination
prefix.
1. <mark>COUNTED</mark> - Route has been included in internal prefix list count.
1. <mark>MULTIPATH</mark> -Route has been included as part of multipath route
selection to destination prefix.
1. <mark>IGP_CHANGED</mark> - Set for routes exhanged over iBGP intradomain
autonomous system networks.

### 1.19 local_pref column

Local preference of the BGP route. Default value is 0.

### 1.20 bgp_nexthops column

Represents nexthops for this entry. Each entry in the [BGP_Route](bgp_route.html) can
have a reference to one or many(for ECMP) nexthop entries.

## 2. Path attributes group

The `path_attributes` column contains key-value pairs that represent route
attributes.

### 2.1 path_attributes : bgp_loc_pref key

Local preference path attribute. Used by BGP to influence in the best path
selection. Default value is 0.

### 2.2 path_attributes : bgp_origin key

Indicates whether a route is `IGP`, `EGP` or `incomplete`. Default is
incomplete.

### 2.3 path_attributes : bgp_flags key

Route status flags. Allowed values are `history`, `damped`,`multipath`,`valid`,
`selected` Default value is 0.

### 2.4 path_attributes : bgp_as_path key

List of AS path number for a route. Default is 0. Example: 200,300,400

