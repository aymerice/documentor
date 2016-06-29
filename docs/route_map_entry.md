# Route_Map_Entry

![Route_Map_Entry_table_img](http://www.plantuml.com/plantuml/img/0S81FVv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWGaTGNq5JK65qQ5z6QMnqPN8AOsnXStCWGaTGNqDlRMrrRcbqULz6QMnqPN8AOsnXStCWK79bPcbuNqnfStGAVGfqRsTbT6XbSY1x2cDiONDp859lTNHbNqrXS5z5RdHoUGfz2b9lTNHbNqrXS5z5RdHoUI0kTIu-851oPMPfU5zCQNDq2b9lTNHbNqrXS5z5RdHoUI0yBNKj859lTNHbNqrXS5z5RdHoUGfIRtLqPLzDON1VHMvqSdaWBdKkFY12Hr1VGLDGONHeNqPfR7HbSWfIRtLqPLzDON1VHMvqSdaWBdKkFY12Hr1VGszjRNLkQNHvNqPfR7HbSWfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. Status

### 1.1 status

**Type**: _string->string_

## 2. Global Route Map Entries Configuration

### 2.1 set

**Type**: _string->string_

The set rule for route map.

### 2.2 set : origin

**Type**: _string_

Sets the origin attribute of a local BGP route. The allowed values are below.

1. <mark>EGP</mark> - Indicates that the route is learned through EBGP.
1. <mark>IGP</mark> - Indicates that the route is learned through IBGP.
1. <mark>incomplete</mark> - Indicates that the origin of route is unknown. This
occurs when a route is redistributed into BGP.

### 2.3 set : extcommunity_soo

**Type**: _string_

Sets the site-of-origin extended community of a BGP route. The value is the
community attribute in the form AA:NN where AA can be either AS number or IP
address and NN is the community identifier.

### 2.4 set : weight

**Type**: _integer_

Sets the weight of a BGP route.

### 2.5 set : metric

**Type**: _integer_

Sets the metric which is used with BGP route advertisement.

### 2.6 set : atomic-aggregate

**Type**: _boolean_

If set to 'true', upstream routers will be notified that route is aggregated.
Default is false.

### 2.7 set : community

**Type**: _string_

Sets the community list of the route.The value is community list name.

### 2.8 set : as_path_exclude

**Type**: _string_

Excludes AS numbers from the AS path. The value is a comma delimited list of
autonomous system numbers to be excluded for incoming routes.

### 2.9 set : local_preference

**Type**: _integer_

Sets the BGP local preference and the local preference value of an IBGP route.

### 2.10 set : aggregator_as

**Type**: _integer_

Sets the originating AS of an aggregated route. The value is the Autonomous
System  number.

### 2.11 set : ipv6_next_hop_global

**Type**: _string_

+ Sets the BGP-4
+ global IPv6 next hop address. The value is the IPv6 address.

### 2.12 set : as_path_prepend

**Type**: _string_

Prepends AS numbers to the AS path. The value is a list of AS numbers seperated
by a space.

### 2.13 set : extcommunity_rt

**Type**: _string_

Sets the route target extended community of a BGP route. The value is the
community attribute in the form AA:NN where AA can be either AS number or IP
address and NN is the community identifier.

### 2.14 exitpolicy

**Type**: _string_

Rather than normal exiting, route map can continue on processing next route map,
or goto N route map and continue on processing.

### 2.15 description

**Type**: _string_

### 2.16 call

**Type**: _uuid_ **refTable**: [Route_Map_Entry](route_map_entry.html) **refType**: _strong_



If call command is used, nextrm indicate which route map to goto.

### 2.17 match_community_list

**Type**: _uuid_ **refTable**: [BGP_Community_Filter](bgp_community_filter.html) **refType**: _weak_



Match routes based on community list.

### 2.18 set_community_list_delete

**Type**: _uuid_ **refTable**: [BGP_Community_Filter](bgp_community_filter.html) **refType**: _weak_



Removes communities from the specified community list for BGP route
advertisements.

### 2.19 match_extcommunity_list

**Type**: _uuid_ **refTable**: [BGP_Community_Filter](bgp_community_filter.html) **refType**: _weak_



Match routes based on extended community list.

### 2.20 goto_target

**Type**: _uuid_ **refTable**: [Route_Map_Entry](route_map_entry.html) **refType**: _strong_



If exitpolicy is goto, nextpref is the route map to jump to.

### 2.21 match_ipv4_prefix_list

**Type**: _uuid_ **refTable**: [Prefix_List](prefix_list.html) **refType**: _weak_



Match routes based on IPv4 prefix list.

### 2.22 action

**Type**: _string_

There are three types, permit, deny, and any.

### 2.23 match_as_path

**Type**: _uuid_ **refTable**: [BGP_ASPath_Filter](bgp_aspath_filter.html) **refType**: _weak_



Match routes based on AS path.

### 2.24 match

**Type**: _string->string_

The match rule for route map. Default is deny.

### 2.25 match : origin

**Type**: _string_

Matches BGP routes based on the origin of the specified route. The allowed
values are below.

1. <mark>EGP</mark> - Indicates that the route is learned through EBGP.
1. <mark>IGP</mark> - Indicates that the route is learned through IBGP.
1. <mark>incomplete</mark> - Indicates that the origin of route is unknown. This
occurs when a route is redistributed into BGP.

### 2.26 match : ipv6_next_hop

**Type**: _string_

Matches routes based on next hop IPv6 address.

### 2.27 match : metric

**Type**: _integer_

Matches routes with the specific metric value.

### 2.28 match : probability

**Type**: _integer_

Randomly match specified percentage of the routes.

### 2.29 match_ipv6_prefix_list

**Type**: _uuid_ **refTable**: [Prefix_List](prefix_list.html) **refType**: _weak_



Match routes based on IPv6 prefix list.

## 3. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 3.1 other_config

**Type**: _string->string_

### 3.2 external_ids

**Type**: _string->string_

