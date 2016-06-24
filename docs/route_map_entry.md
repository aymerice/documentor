# Route_Map_Entry

![Route_Map_Entry_table_img](http://www.plantuml.com/plantuml/img/ZT312i8m30RWUvyYxAIWRp36LDIBmfYxbpZZLkpQqMRW4D_TWHUf5Smn-Nv2adj6nqEdHO_r3Hk2fBIMeSAp9f_0Gy1KjKRlORqlvEfK8BTofpIJWpI5MRNGgccvSKHc3baM13QswmQZUFmpKpYwghiyACzn-XHlMDg1IHwnbrl3RepZ42sNsUU6wFphp9ygl2qAWvx8oLocVxy0)

## 1. Global Route Map Entries Configuration group

### 1.1 set column

The set rule for route map.

### 1.2 set : origin key

Sets the origin attribute of a local BGP route. The allowed values are below.

1. <mark>EGP</mark> - Indicates that the route is learned through EBGP.
1. <mark>IGP</mark> - Indicates that the route is learned through IBGP.
1. <mark>incomplete</mark> - Indicates that the origin of route is unknown. This
occurs when a route is redistributed into BGP.

### 1.3 set : extcommunity_soo key

Sets the site-of-origin extended community of a BGP route. The value is the
community attribute in the form AA:NN where AA can be either AS number or IP
address and NN is the community identifier.

### 1.4 set : weight key

Sets the weight of a BGP route.

### 1.5 set : metric key

Sets the metric which is used with BGP route advertisement.

### 1.6 set : atomic-aggregate key

If set to 'true', upstream routers will be notified that route is aggregated.
Default is false.

### 1.7 set : community key

Sets the community list of the route.The value is community list name.

### 1.8 set : as_path_exclude key

Excludes AS numbers from the AS path. The value is a comma delimited list of
autonomous system numbers to be excluded for incoming routes.

### 1.9 set : local_preference key

Sets the BGP local preference and the local preference value of an IBGP route.

### 1.10 set : aggregator_as key

Sets the originating AS of an aggregated route. The value is the Autonomous
System  number.

### 1.11 set : ipv6_next_hop_global key

+ Sets the BGP-4
+ global IPv6 next hop address. The value is the IPv6 address.

### 1.12 set : as_path_prepend key

Prepends AS numbers to the AS path. The value is a list of AS numbers seperated
by a space.

### 1.13 set : extcommunity_rt key

Sets the route target extended community of a BGP route. The value is the
community attribute in the form AA:NN where AA can be either AS number or IP
address and NN is the community identifier.

### 1.14 exitpolicy column

Rather than normal exiting, route map can continue on processing next route map,
or goto N route map and continue on processing.

### 1.15 call column

If call command is used, nextrm indicate which route map to goto.

### 1.16 match_community_list column

Match routes based on community list.

### 1.17 set_community_list_delete column

Removes communities from the specified community list for BGP route
advertisements.

### 1.18 match_extcommunity_list column

Match routes based on extended community list.

### 1.19 goto_target column

If exitpolicy is goto, nextpref is the route map to jump to.

### 1.20 match_ipv4_prefix_list column

Match routes based on IPv4 prefix list.

### 1.21 action column

There are three types, permit, deny, and any.

### 1.22 match_as_path column

Match routes based on AS path.

### 1.23 match column

The match rule for route map. Default is deny.

### 1.24 match : origin key

Matches BGP routes based on the origin of the specified route. The allowed
values are below.

1. <mark>EGP</mark> - Indicates that the route is learned through EBGP.
1. <mark>IGP</mark> - Indicates that the route is learned through IBGP.
1. <mark>incomplete</mark> - Indicates that the origin of route is unknown. This
occurs when a route is redistributed into BGP.

### 1.25 match : ipv6_next_hop key

Matches routes based on next hop IPv6 address.

### 1.26 match : metric key

Matches routes with the specific metric value.

### 1.27 match : probability key

Randomly match specified percentage of the routes.

### 1.28 match_ipv6_prefix_list column

Match routes based on IPv6 prefix list.

