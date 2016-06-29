# BGP_Neighbor

![BGP_Neighbor_table_img](http://www.plantuml.com/plantuml/img/0Ve01Vz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo19RdHbScPXOsKAOsnXStCWGaTGNqvbQMTeOczo2dqAGaTGNqvbQMTeOczo82raBJuWIMvqPN9cOMDb2a97K5zEPMbdQ69lSY0yBNKj8497K5zEPMbdQ69lSWfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

This table holds both BGP neighbors and BGP peer groups.  A boolean named
is_peer_group identifies whether a specific entry is a bgp neighbor or a peer
group.

## 1. Neighbor Configuration group

### 1.1 update_source column

Specifies the source-address to establish BGP connections to neighbors.

### 1.2 weight column

This is the weight for routes from this neighbor.

### 1.3 local_interface column

Reference to the corresponding interface.  This is used only for ipv6. Default
is none.

### 1.4 bgp_peer_group column

This column is used only if the entry is a BGP neighbor.  It represents the peer
group this BGP neighbor is a member of.  Default is none.

### 1.5 shutdown column

Specifies whether the neighbor has been administratively shut down. If not
specified, the default is false.

### 1.6 aspath_filters column

Name and direction of the as-path filters.

### 1.7 aspath_filters : out key

AS Path filter associated with outbound routes.

### 1.8 aspath_filters : in key

AS Path filter associated with incoming routes.

### 1.9 route_maps column

Name and direction of the route maps.

### 1.10 route_maps : out key

Map associated with outbound routes.

### 1.11 route_maps : in key

Map associated with incoming routes.

### 1.12 remove_private_as column

Specifies whether private AS should be removed. If not specified, the default
value is false.

### 1.13 prefix_lists column

Name and direction of the prefix lists.

### 1.14 prefix_lists : out key

Prefix list associated with outbound routes.

### 1.15 prefix_lists : in key

Prefix list associated with incoming routes.

### 1.16 inbound_soft_reconfiguration column

Allow inbound soft reconfiguration for this neighbor.

### 1.17 remote_as column

Peer AS number. For EBGP, the peer is in another AS, so the remote AS number
must be different from the local router's AS number or BGP router asn. For IBGP,
the peer is in the same AS, so the two AS numbers must be the same. Remote AS
number. Range: 1-4294967295.

### 1.18 ttl_security_hops column

Specifies the maximum number of hops to the BGP peer.

### 1.19 ebgp_multihop column

If set to "true", allows BGP connections with peers that are not directly
connected. Default is "false".

### 1.20 passive column

Indicates that open messages should NOT be sent to this neighbor. Default is
false.

### 1.21 advertisement_interval column

Minimum interval between sending BGP routing updates. Range: 0-600 seconds.

### 1.22 allow_as_in column

Allow-as-in is the number of times BGP can allow an instance of AS to be in the
AS_PATH.

### 1.23 description column

This is an optional string which can be used for describing this entry. Default
is empty.

### 1.24 local_as column

To specify a different asn from BGP router asn to be used as local AS number in
update messages to peers. Local AS number. Range: 1-4294967295.

### 1.25 password column

The password for this entry.

### 1.26 tcp_port_number column

This is the BGP neighbor's tcp port number.  Default value is 179.

### 1.27 is_peer_group column

This is a flag which identifies whether this specific entry is an individual BGP
neighbor or is a BGP peer group.  A value of true implies a peer group.
Otherwise, the entry represents a BGP neighbor.  If the value is not set, it
implies false.

### 1.28 timers column

BGP per neighbor timers - Connect timer/Keep-alive Interval.

### 1.29 timers : holdtime key

Set the hold time for a specific BGP peer. The value is hold time in seconds.
Default value is 180 seconds.

### 1.30 timers : keepalive key

Set the keepalive interval for a specific BGP peer. The value is keepalive
interval in seconds. Default value is 60 seconds.

### 1.31 maximum_prefix_limit column

Maximum number of prefixes that can be accepted on a BGP peer session. When the
limit is exceeded, a system log message is logged.

## 2. BGP Neighbor Statistics group

The `statistics` column contains various counters about this BGP neighbor.

### 2.1 statistics column

### 2.2 statistics : bgp_peer_dynamic_cap_in_count key

This indicates how many times a dynamic cap message has been received.

### 2.3 statistics : bgp_peer_refresh_in_count key

This indicates how many times a frefresh message has been received.

### 2.4 statistics : bgp_peer_update_in_count key

This indicates how many times an update message has been received.

### 2.5 statistics : bgp_peer_readtime key

This indicates the last time an update or keepalive message has been received.

### 2.6 statistics : bgp_peer_refresh_out_count key

This indicates how many times a refresh message has been sent.

### 2.7 statistics : bgp_peer_dropped_count key

This indicates the number of times peers have been dropped from the established
state.

### 2.8 statistics : bgp_peer_keepalive_in_count key

This indicates how many times a keepalive message has been received.

### 2.9 statistics : bgp_peer_open_in_count key

This indicates how many times an open message has been received.

### 2.10 statistics : bgp_peer_open_out_count key

This indicates how many times an open message has been sent.

### 2.11 statistics : bgp_peer_keepalive_out_count key

This indicates how many times a keepalive message has been sent.

### 2.12 statistics : bgp_peer_dynamic_cap_out_count key

This indicates how many times a dynamic cap message has been sent.

### 2.13 statistics : bgp_peer_resettime key

Indicates the last time peer was reset.

### 2.14 statistics : bgp_peer_notify_in_count key

This indicates how many times a notify message has been received.

### 2.15 statistics : bgp_peer_notify_out_count key

This indicates how many times a notify message has been sent.

### 2.16 statistics : bgp_peer_established_count key

This indicates the number of times peers have been established.

### 2.17 statistics : bgp_peer_uptime key

This indicates how long since peer has been in the established state, or since
the last route update was received.

### 2.18 statistics : bgp_peer_update_out_count key

This indicates how many times an update message has been sent.

## 3. Status group

### 3.1 status column

These values describe various status information about this BGP neighbor or BGP
Peer group entry.

### 3.2 status : bgp_num_clear_counters_peer_soft_out_requested key

Indicates the number of times soft clear was requested for outbound routing
policy updates. When this value is greater than
bgp_num_clear_counters_peer_soft_out_performed, then soft clear is still
pending.

### 3.3 status : bgp_num_clear_counters_peer_soft_in_performed key

Indicates the number of times soft clear is performed for inbound routing policy
updates.

### 3.4 status : bgp_num_clear_counters_peer_soft_out_performed key

Indicates the number of times soft clear is performed for outbound routing
policy updates.

### 3.5 status : bgp_num_clear_counters_peer_soft_in_requested key

Indicates the number of times soft clear was requested for inbound routing
policy updates. When this value is greater than
bgp_num_clear_counters_peer_soft_in_performed, then soft clear is still pending.

## 4. BGP Neighbor or Peer group Status Info group

The `status` column contains one or more informational entries indicating
various status values for this BGP neighbor.

### 4.1 status column

These values describe various status information about this BGP neighbor or BGP
Peer group entry.

### 4.2 status : bgp_peer_state key

This represents the BGP neighbor state at this specific instance in time.  The
value can be one of Idle, Connect, Active, OpenSent, OpenConfirm, Established,
Clearing or Deleted and can change any time.  Default is Idle.

## 5. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 5.1 external_ids column

### 5.2 other_config column

