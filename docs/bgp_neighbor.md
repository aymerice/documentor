# BGP_Neighbor

![BGP_Neighbor_table_img](http://www.plantuml.com/plantuml/img/0HG1w_v0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo19RdHbScPXOsKAOsnXStCWGaTGNqvbQMTeOczo2dqAGaTGNqvbQMTeOczo82raBJuWIMvqPN9cOMDb2a97K5zEPMbdQ69lSY0yBNKj8497K5zEPMbdQ69lSWfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

This table holds both BGP neighbors and BGP peer groups.  A boolean named
is_peer_group identifies whether a specific entry is a bgp neighbor or a peer
group.

## 1. Neighbor Configuration

### 1.1 update_source

**Type**: _string_

Specifies the source-address to establish BGP connections to neighbors.

### 1.2 weight

**Type**: _integer_

This is the weight for routes from this neighbor.

### 1.3 local_interface

**Type**: _uuid_ **refTable**: [Interface](interface.html) **refType**: _strong_



Reference to the corresponding interface.  This is used only for ipv6. Default
is none.

### 1.4 bgp_peer_group

**Type**: _uuid_ **refTable**: [BGP_Neighbor](bgp_neighbor.html) **refType**: _strong_



This column is used only if the entry is a BGP neighbor.  It represents the peer
group this BGP neighbor is a member of.  Default is none.

### 1.5 shutdown

**Type**: _boolean_

Specifies whether the neighbor has been administratively shut down. If not
specified, the default is false.

### 1.6 aspath_filters

**Type**: _string->uuid_ **refTable**: [BGP_ASPath_Filter](bgp_aspath_filter.html) **refType**: _strong_



Name and direction of the as-path filters.

### 1.7 aspath_filters : out

**Type**: _uuid_ **refTable**: [unknown](unknown.html) **refType**: _strong_



AS Path filter associated with outbound routes.

### 1.8 aspath_filters : in

**Type**: _uuid_ **refTable**: [unknown](unknown.html) **refType**: _strong_



AS Path filter associated with incoming routes.

### 1.9 route_maps

**Type**: _string->uuid_ **refTable**: [Route_Map](route_map.html) **refType**: _strong_



Name and direction of the route maps.

### 1.10 route_maps : out

**Type**: _uuid_ **refTable**: [unknown](unknown.html) **refType**: _strong_



Map associated with outbound routes.

### 1.11 route_maps : in

**Type**: _uuid_ **refTable**: [unknown](unknown.html) **refType**: _strong_



Map associated with incoming routes.

### 1.12 remove_private_as

**Type**: _boolean_

Specifies whether private AS should be removed. If not specified, the default
value is false.

### 1.13 prefix_lists

**Type**: _string->uuid_ **refTable**: [Prefix_List](prefix_list.html) **refType**: _strong_



Name and direction of the prefix lists.

### 1.14 prefix_lists : out

**Type**: _uuid_ **refTable**: [unknown](unknown.html) **refType**: _strong_



Prefix list associated with outbound routes.

### 1.15 prefix_lists : in

**Type**: _uuid_ **refTable**: [unknown](unknown.html) **refType**: _strong_



Prefix list associated with incoming routes.

### 1.16 inbound_soft_reconfiguration

**Type**: _boolean_

Allow inbound soft reconfiguration for this neighbor.

### 1.17 remote_as

**Type**: _integer_

Peer AS number. For EBGP, the peer is in another AS, so the remote AS number
must be different from the local router's AS number or BGP router asn. For IBGP,
the peer is in the same AS, so the two AS numbers must be the same. Remote AS
number. Range: 1-4294967295.

### 1.18 ttl_security_hops

**Type**: _integer_

Specifies the maximum number of hops to the BGP peer.

### 1.19 ebgp_multihop

**Type**: _boolean_

If set to "true", allows BGP connections with peers that are not directly
connected. Default is "false".

### 1.20 passive

**Type**: _boolean_

Indicates that open messages should NOT be sent to this neighbor. Default is
false.

### 1.21 advertisement_interval

**Type**: _integer_

Minimum interval between sending BGP routing updates. Range: 0-600 seconds.

### 1.22 allow_as_in

**Type**: _integer_

Allow-as-in is the number of times BGP can allow an instance of AS to be in the
AS_PATH.

### 1.23 description

**Type**: _string_

This is an optional string which can be used for describing this entry. Default
is empty.

### 1.24 local_as

**Type**: _integer_

To specify a different asn from BGP router asn to be used as local AS number in
update messages to peers. Local AS number. Range: 1-4294967295.

### 1.25 password

**Type**: _string_

The password for this entry.

### 1.26 tcp_port_number

**Type**: _integer_

This is the BGP neighbor's tcp port number.  Default value is 179.

### 1.27 is_peer_group

**Type**: _boolean_

This is a flag which identifies whether this specific entry is an individual BGP
neighbor or is a BGP peer group.  A value of true implies a peer group.
Otherwise, the entry represents a BGP neighbor.  If the value is not set, it
implies false.

### 1.28 timers

**Type**: _string->integer_

BGP per neighbor timers - Connect timer/Keep-alive Interval.

### 1.29 timers : holdtime

**Type**: _integer_

Set the hold time for a specific BGP peer. The value is hold time in seconds.
Default value is 180 seconds.

### 1.30 timers : keepalive

**Type**: _integer_

Set the keepalive interval for a specific BGP peer. The value is keepalive
interval in seconds. Default value is 60 seconds.

### 1.31 maximum_prefix_limit

**Type**: _integer_

Maximum number of prefixes that can be accepted on a BGP peer session. When the
limit is exceeded, a system log message is logged.

## 2. BGP Neighbor Statistics

The `statistics` column contains various counters about this BGP neighbor.

### 2.1 statistics

**Type**: _string->integer_

### 2.2 statistics : bgp_peer_dynamic_cap_in_count

**Type**: _integer_

This indicates how many times a dynamic cap message has been received.

### 2.3 statistics : bgp_peer_refresh_in_count

**Type**: _integer_

This indicates how many times a frefresh message has been received.

### 2.4 statistics : bgp_peer_update_in_count

**Type**: _integer_

This indicates how many times an update message has been received.

### 2.5 statistics : bgp_peer_readtime

**Type**: _integer_

This indicates the last time an update or keepalive message has been received.

### 2.6 statistics : bgp_peer_refresh_out_count

**Type**: _integer_

This indicates how many times a refresh message has been sent.

### 2.7 statistics : bgp_peer_dropped_count

**Type**: _integer_

This indicates the number of times peers have been dropped from the established
state.

### 2.8 statistics : bgp_peer_keepalive_in_count

**Type**: _integer_

This indicates how many times a keepalive message has been received.

### 2.9 statistics : bgp_peer_open_in_count

**Type**: _integer_

This indicates how many times an open message has been received.

### 2.10 statistics : bgp_peer_open_out_count

**Type**: _integer_

This indicates how many times an open message has been sent.

### 2.11 statistics : bgp_peer_keepalive_out_count

**Type**: _integer_

This indicates how many times a keepalive message has been sent.

### 2.12 statistics : bgp_peer_dynamic_cap_out_count

**Type**: _integer_

This indicates how many times a dynamic cap message has been sent.

### 2.13 statistics : bgp_peer_resettime

**Type**: _integer_

Indicates the last time peer was reset.

### 2.14 statistics : bgp_peer_notify_in_count

**Type**: _integer_

This indicates how many times a notify message has been received.

### 2.15 statistics : bgp_peer_notify_out_count

**Type**: _integer_

This indicates how many times a notify message has been sent.

### 2.16 statistics : bgp_peer_established_count

**Type**: _integer_

This indicates the number of times peers have been established.

### 2.17 statistics : bgp_peer_uptime

**Type**: _integer_

This indicates how long since peer has been in the established state, or since
the last route update was received.

### 2.18 statistics : bgp_peer_update_out_count

**Type**: _integer_

This indicates how many times an update message has been sent.

## 3. Status

### 3.1 status

**Type**: _string->string_

These values describe various status information about this BGP neighbor or BGP
Peer group entry.

### 3.2 status : bgp_num_clear_counters_peer_soft_out_requested

**Type**: _integer_

Indicates the number of times soft clear was requested for outbound routing
policy updates. When this value is greater than
bgp_num_clear_counters_peer_soft_out_performed, then soft clear is still
pending.

### 3.3 status : bgp_num_clear_counters_peer_soft_in_performed

**Type**: _integer_

Indicates the number of times soft clear is performed for inbound routing policy
updates.

### 3.4 status : bgp_num_clear_counters_peer_soft_out_performed

**Type**: _integer_

Indicates the number of times soft clear is performed for outbound routing
policy updates.

### 3.5 status : bgp_num_clear_counters_peer_soft_in_requested

**Type**: _integer_

Indicates the number of times soft clear was requested for inbound routing
policy updates. When this value is greater than
bgp_num_clear_counters_peer_soft_in_performed, then soft clear is still pending.

## 4. BGP Neighbor or Peer group Status Info

The `status` column contains one or more informational entries indicating
various status values for this BGP neighbor.

### 4.1 status

**Type**: _string->string_

These values describe various status information about this BGP neighbor or BGP
Peer group entry.

### 4.2 status : bgp_peer_state

**Type**: _string_

This represents the BGP neighbor state at this specific instance in time.  The
value can be one of Idle, Connect, Active, OpenSent, OpenConfirm, Established,
Clearing or Deleted and can change any time.  Default is Idle.

## 5. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 5.1 external_ids

**Type**: _string->string_

### 5.2 other_config

**Type**: _string->string_

