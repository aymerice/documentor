# Route

Global routes information base within an [System](system.html).

A [Route](route.html) record represents a route. This is a unique record per (vrf,
prefix, protocol) set.

## 1. Global Routes Configuration group

### 1.1 distance column

Administrative distance for the route entry. This value is populated every time
a protocol or a user adds a new entry. The default value is 1 which is the
default distance for static routes.

### 1.2 from column

Protocol that is responsible for this entry. The value is `bgp` if BGP created
this entry, `static` when the user configures a static route, `connected` if it
is a directly connected device and `ospf` if OSPF created this entry.

### 1.3 address_family column

Represents the address family for this entry. Default value is `ipv4`.

### 1.4 metric column

This is the BGP Multi Exit Discriminator (MED) attribute used in best path
selection. The MED provides a dynamic way to influence another AS in the way to
reach a certain route when there are multiple entry points for that AS.  BGP
decision process takes weight, local preference, AS path, Origin and MED into
account.  For selection, if all other factors are equal, the exit point with the
lowest MED is preferred. Default value is 0

### 1.5 selected column

Route table can have entries which may not be selected for forwarding. This flag
indicates if this entry is selected as an active route for forwarding. Default
is `false`.

### 1.6 sub_address_family column

Represents more information regarding this entry. Default is `unicast`.

### 1.7 prefix column

IPv4 or IPv6 destination prefix and mask in the address/mask format. Example
192.168.0.0/16

### 1.8 vrf column

Reference to the VRF table, to which this route belongs.

### 1.9 protocol_private column

Indicates that this row is a protocol specific route entry. The entries which
have this value set, should not participate in routing. Example: BGP can store
routes for reference and future selection but should not currently be used for
forwarding. Default is `false`.

### 1.10 nexthops column

List of all the nexthops for this entry. This will be empty in case of
blackhole.

## 2. Protocol Specific group

The `protocol_specific` column contains key-value pairs that are used by the
owner of the entry. Example: If BGP created an entry BGP can populate these key-
value pairs for its internal use. These values may not add value to other
daemons

### 2.1 protocol_specific : bgp_loc_pref key

Local preference path attribute. Used by BGP to influence in the best path
selectionUsed by BGP to influence in the best path selection..

### 2.2 protocol_specific : bgp_origin key

Indicates whether a route is `IGP`, `EGP` or `incomplete`.

### 2.3 protocol_specific : bgp_flags key

Route status flags. Allowed values are `history`, `damped`,`multipath`

### 2.4 protocol_specific : bgp_as_path key

List of AS path number for a route. Example: 200,300,400

