# OpenSwitch Schema



## 1. System table

Configuration for an OpenSwitch system. There must be exactly one record in the
[System](#system-table) table.


### 1.1 db_version column

The database schema version number in the form `_major_._minor_._tweak_`, e.g.
`1.2.3`.  Whenever the database schema is changed in a non-backward compatible
way (e.g. deleting a column or a table), _major_ is incremented.  When the
database schema is changed in a backward compatible way (e.g. adding a new
column), _minor_ is incremented.  When the database schema is changed
cosmetically (e.g. reindenting its syntax), _tweak_ is incremented.

The schema version is part of the database schema, so it can also be retrieved
by fetching the schema using the Open vSwitch database protocol.


### 1.2 dns_servers column



### 1.3 qos column

Specifies the schedule profile for ports that do not specify their own schedule
profile (see [Port](#port-table) qos column). When missing, the [QoS](QoS) row with
[hw_default](#hw-default-column) true will be used.


### 1.4 ntp_config column



### 1.5 next_cfg column

Sequence number for client to increment.  When a client modifies any part of the
database configuration and wishes to wait for OpenSwitch to finish applying the
changes, it may increment this sequence number.


### 1.6 qos_cos_map_entries column

Contains references to each entry in the global COS map used by port trust mode
COS. (see [QoS_DSCP_Map_Entry](QoS_DSCP_Map_Entry))


### 1.7 asset_tag_number column



### 1.8 broadview_config column



### 1.9 syslog_remotes column

List of syslog servers to which syslog messages will be forwarded.
[Syslog_Remote](Syslog_Remote)


### 1.10 qos_config column



### 1.11 manager_options column

Database clients to which the OpenSwitch database server should connect or to
which it should listen, along with options for how these connection should be
configured.  See the [Manager](Manager) table for more information.


### 1.12 ntp_statistics column



### 1.13 ecmp_config column



### 1.14 dhcp_config column



### 1.15 management_vrf column



### 1.16 ntp_status column

This column holds the global status information for NTP.


### 1.17 bridges column

Set of bridges.


### 1.18 subsystems column



### 1.19 statistics column



### 1.20 auto_provisioning_status column



### 1.21 hostname column



### 1.22 domain_name column

Domain name as configured by the user.


### 1.23 acls column

List of all Access Control Lists (ACLs) in the system.  The existence of the
list is not an indication that it has been applied.


### 1.24 mgmt_intf column

This column is a map of string-string pairs Management interface column contains
the attributes of management interface. The keys are name, mode, ip, subnet
mask, default gateway, dns server IPv4 addresses. This column holds values that
are configured by the user.


### 1.25 radius_servers column

Specifies radius servers configuration. See the [Radius_Server](Radius_Server)
table for more information.


### 1.26 next_hw column

Sequence number to indicate that a change has occurred in the hardware
configuration (e.g., a subsystem has been added or removed).


### 1.27 cur_hw column

Sequence number that indicates the current change level for the h/w
configuration. When [cur_hw](System.cur_hw) is the same as
[next_hw](System.next_hw), then all platform daemon processing has completed in
response to the hardware addition or removal. This is not used for transceiver
pluggable module insertion/removal.


### 1.28 vrfs column



### 1.29 router_id column



### 1.30 management_mac column

Ethernet MAC address for the management interface port for this system.


### 1.31 other_info column



### 1.32 q_profile column

Specifies the queue profile for ports that do not specify their own queue
profile (see [Port](Port) q_profile column). When missing, the
[Q_Profile](Q_Profile) row with [hw_default](Q_Profile.hw_default) true will be
used.


### 1.33 ssl column



### 1.34 copp_statistics column



### 1.35 boot_time column

Boot time of the machine, represented in seconds since 1970-01-01 00:00:00 UTC.
OVSDB integers are 64 bit, which means it will take some time until we roll
over.


### 1.36 daemons column



### 1.37 external_ids column



### 1.38 logrotate_config column



### 1.39 lldp_statistics column



### 1.40 mgmt_intf_status column

This column holds the status of the management interface IP parameters. This
column contains key-value pairs that report the mangement interface IP
attributes like IP address, subnet, default gateway, primary and secondary name
server. These values are either statically configured by the user or populated
by the DHCP client. The keys of this column is same as that of mgmt_intf column.


### 1.41 switch_version column

The OpenSwitch version number, e.g. `0.1.0`.


### 1.42 status column

System level status information per service like `LLDP`, etc.


### 1.43 lacp_config column



### 1.44 snmp_communities column

Community strings to be used by the system when communicating over
SNMPv1/SNMPv2c.


### 1.45 loop_protect_disable_timer column

This specifies the time in seconds for which the ports are to be disabled on
detecting a loop. Default value is `0` i.e the port is disabled indefinitely.


### 1.46 aaa column



### 1.47 system_mac column

Ethernet MAC address available to use anywhere a non-unique MAC is needed.


### 1.48 sflow column

sFlow(R) configuration.


### 1.49 software_info column



### 1.50 other_config column



### 1.51 qos_status column

Key-value pairs that report the Quality of Service status in hardware for ports
that do not specify their own configuration.


### 1.52 bufmon_info column



### 1.53 qos_dscp_map_entries column

Contains references to each entry in the global DSCP map used by port trust mode
DSCP. (see [QoS_DSCP_Map_Entry](QoS_DSCP_Map_Entry))


### 1.54 bufmon_config column



### 1.55 cur_cfg column

Sequence number that OpenSwitch sets to the current value of
[next_cfg](System.next_cfg) after it finishes applying a set of configuration
changes.


### 1.56 loop_protect_transmit_interval column

This specifies the time interval in seconds between successive transmissions of
loop-protect packets. Default value is `5` seconds.


## 2. Subsystem table



### 2.1 leds column



### 2.2 other_info column



### 2.3 name column



### 2.4 interfaces column

References to the interfaces which are part of this subsystem.


### 2.5 other_config column



### 2.6 hw_desc_dir column

Directory where the hardware description files for this subsystem are located.


### 2.7 asset_tag_number column



### 2.8 fans column



### 2.9 next_mac_address column

Next available (unused) Ethernet MAC address from the MAC address pool for this
subsystem.


### 2.10 macs_remaining column

The number of available (unused) Ethernet MAC address from the MAC address pool
for this subsystem.


### 2.11 power_supplies column



### 2.12 external_ids column



### 2.13 type column



### 2.14 temp_sensors column



## 3. Bridge table

Configuration for a bridge within an [System](System).

A [Bridge](Bridge) record represents an Ethernet switch with one or more
``ports,'' which are the [Port](Port) records pointed to by the
[Bridge](Bridge)'s [ports](Bridge.ports) column. In the first release, only one
default bridge (bridge_normal) is supported


### 3.1 status column

Key-value pairs that report bridge status.


### 3.2 datapath_id column



### 3.3 name column

Bridge identifier.  Should be alphanumeric and no more than about 8 bytes long.
Must be unique among the names of ports, interfaces, and bridges on a host.


### 3.4 mirrors column

[Mirror](Mirror) references for sessions configured in this bridge.


### 3.5 other_config column



### 3.6 mstp_instances column

MSTP configuration for individual instance.


### 3.7 mstp_enable column

Set this value to `true`, to enable MSTP. Default value is `false`.


### 3.8 datapath_version column



### 3.9 external_ids column



### 3.10 vlans column

VLANs included in the bridge.


### 3.11 ports column

Ports included in the bridge.


### 3.12 mstp_common_instance column

MSTP configuration for CIST(Common Instance Spanning Tree).


### 3.13 datapath_type column

Name of datapath provider.


## 4. VRF table

Each entry in this table represents a single routing domain, commonly known as
Virtual Routing and Forwarding.


### 4.1 status column



### 4.2 ospf_routers column

The list of all the OSPFv2 Router instances.


### 4.3 name column

VRF identifier. Should be alphanumeric. VRF names must be unique.


### 4.4 other_config column



### 4.5 active_router_id column

Router-ID (in IPv4 format) that is currently used in the system, unless
overridden by protocol specific one.


### 4.6 ports column

Ports included in the VRF.


### 4.7 table_id column

Kernel table_id assigned for routing table of this VRF.


### 4.8 external_ids column



### 4.9 bgp_routers column

BGP routers keyed by ASN value.


### 4.10 dhcp_server column

DHCP Server in the VRF.


## 5. MSTP_Instance table

This represents information regarding a Bridge's Bridge Protocol entity for the
specified Spanning Tree instance.


### 5.1 mstp_instance_ports column

MSTP configuration for port.


### 5.2 time_since_top_change column

The time last topology change happened for this instance. The format for this is
number of seconds from epoch.


### 5.3 hardware_grp_id column

The hardware spanning tree group ID. Default value is 0.


### 5.4 designated_root column

The root bridge name for a MSTP instance.


### 5.5 topology_change_count column

The total number of topology changes that have occurred for this instance.


### 5.6 vlans column

VLANs included in the MSTP instance.


### 5.7 topology_unstable column

This is set to `true` when a topology change has occurred. Once topology
stabilizes it will be set back to `false`. Default is `false`.


### 5.8 priority column

Set this value to specify the priority value, configured as a multiple of 4096
The lower a priority value, the higher the priority. Default value is 32768.


### 5.9 bridge_identifier column

+ The root bridge ID for CIST. Default value 64 bit string(4 bit priority
+ 12 bit Instance ID
+ 48bit system MAC address)


### 5.10 root_path_cost column

The path cost from the transmitting Bridge to the Root Bridge for the MSTI.


### 5.11 root_port column

Specifies the root port name for a MSTP instance.


### 5.12 root_priority column

The root bridge priority. The lower a priority value, the higher the priority.
Default value is 32768.


## 6. MSTP_Instance_Port table

This represents information regarding a specific Port within the bridge's bridge
protocol entity, for a given MSTI.


### 6.1 designated_bridge column

The designated bridge for this port.


### 6.2 port_role column

The role of port in the active MSTP topology


### 6.3 designated_root column

The root bridge name for a MSTP instance.


### 6.4 port_priority column

Set this value to specify the priority value used along with the switch MAC
address to determine which device is root. Configured as a multiple of 16. The
lower a priority value, the higher the priority. Default value is 128.


### 6.5 admin_path_cost column

The cost to reach root port. Default value is determined from the interface
speed. Bandwidth           Port cost 10 Mbps             2,000,000 100 Mbps
200,000 1 Gigabit Ethernet  20,000 10 Gigabit Ethernet 2,000


### 6.6 designated_bridge_priority column

The designated bridge priority at this port.


### 6.7 port_state column

The state of the port in the active topology Default value is Blocking.


### 6.8 designated_root_priority column

The priority value for designated port. Default value is 32768.


### 6.9 designated_cost column

The path cost for designated bridge.


### 6.10 port column

Specifies port for the MSTP instance.


### 6.11 designated_port column

The designated port ID.


## 7. MSTP_Common_Instance table

This represents information regarding a Bridge's Bridge Protocol entity for the
CIST..


### 7.1 remaining_hops column

The hop count after which this instance MSTP BPDU will be discarded. Default
value is 20


### 7.2 mstp_common_instance_ports column

CIST configurations for port.


### 7.3 topology_change_count column

The total number of topology changes that have occurred for this instance.


### 7.4 forward_delay_expiry_time column

The epoch time in seconds when forward delay will expire.


### 7.5 oper_tx_hold_count column

The value used by the MSTP transmit state machine to limit the maximum
transmission rate of MST BPDUs within the hello interval.


### 7.6 max_age column

Set this value to specify the maximum-aging time(The time a device waits without
receiving spanning tree configuration messages before attempting a
reconfiguration) for all MST instances. Default value is 20.


### 7.7 max_hop_count column



### 7.8 designated_root column

The root bridge name for a CIST instance.


### 7.9 topology_unstable column

This is set to `true` when a topology change has occurred. Once topology
stabilizes it will be set back to `false`. Default is `false`.


### 7.10 priority column

Set this value to specify the priority value, configured as a multiple of 4096
The lower a priority value, the higher the priority. Default value is 32768.


### 7.11 root_path_cost column

The path cost from the transmitting Bridge to the Root Bridge for the MSTI.


### 7.12 root_port column

The root port name for a CIST instance.


### 7.13 root_priority column

The root bridge priority. The lower a priority value, the higher the priority.
Default value is 32768.


### 7.14 hello_time column

The hello time value for this instance. Default value is 2.


### 7.15 cist_path_cost column

The path cost from the transmitting bridge to the CIST regional root.


### 7.16 oper_max_age column

Set this value to specify the maximum-aging time(The time a device waits without
receiving spanning tree configuration messages before attempting a
reconfiguration) for all MST instances.


### 7.17 oper_hello_time column

The operating hello timer value for this instance.


### 7.18 regional_root column

The regional root for the CIST.


### 7.19 bridge_identifier column

+ The root bridge ID for CIST. Default value 64 bit string(4 bit priority
+ 12 bit Instance ID
+ 48bit system MAC address)


### 7.20 time_since_top_change column

The time last topology change happened for this instance. The format for this is
number of seconds from epoch.


### 7.21 hardware_grp_id column

The hardware spanning tree group ID. Default value is 0.


### 7.22 tx_hold_count column

The value used by the MSTP transmit state machine to limit the maximum
transmission rate of MST BPDUs within the hello interval. Default value is 6.


### 7.23 vlans column

VLANs included in the CIST instance.


### 7.24 hello_expiry_time column

The epoch time in seconds after which a hello packet will be sent.


### 7.25 oper_forward_delay column

The forward delay timer value for this instance.


### 7.26 forward_delay column

The forward delay time value for this instance. Default value is 15.


## 8. MSTP_Common_Instance_Port table

This represents information regarding a specific Port within the Bridge's Bridge
Protocol entity, for the CIST.


### 8.1 port_role column

The role of this port in the active MSTP topology.


### 8.2 fwd_transition_count column

The number of times this port has transitioned to the forwarding state.


### 8.3 loop_guard_disable column

Set this value to `true` if loop guard is enabled (to block sending and
receiving BPDUs on the port). Default value is `false`.


### 8.4 bpdu_guard_disable column

Set this value to `true` if BPDU Guard enabled (to shut down the port if that
port receives a BPDU). Default is `false`.


### 8.5 protocol_migration_enable column

Set this value to `true` to switch the STP working mode or to `false` to
explicitly disable it. Default is `true`.


### 8.6 port_path_cost column

The operational value of the path cost.


### 8.7 port column

Specifies port for the CIST instance.


### 8.8 port_hello_time column

The port's hello time value, for the CIST.


### 8.9 bpdu_filter_disable column

Set this value to `true` if BPDU filter is enabled(to suppress sending and
receiving BPDUs on the port). Default value is `false`.


### 8.10 designated_bridge column

The designated bridge identifier component of the port's MSTI port priority
vector.


### 8.11 designated_path_cost column

The path cost for this port.


### 8.12 designated_root column

The designated root ID for the port.


### 8.13 port_state column

The state of the port in the active topology. Default value is Blocking.


### 8.14 restricted_port_role_disable column

Set this value to `true` if restiricted role enabled (not to be selected as Root
Port for the CIST or any MSTI). Default is `false`.


### 8.15 admin_edge_port_disable column

Set this value to `true`, if this admin edge port should not participate in root
election. Default is `false`.


### 8.16 root_guard_disable column

Set this value to `true` if root guard is enabled(to participate in STP as long
as the device does not try to become the root). Default value is `false`.


### 8.17 designated_port column

The designated port identifier component of the port's MSTI port priority
vector.


### 8.18 link_type column

Specifies the link type. Default value is point_to_point.


### 8.19 bpdus_rx_enable column

Set this value to `false` to stop transmission of BPDUs. Default is `true`.


### 8.20 mstp_statistics column



### 8.21 admin_path_cost column

The path cost for the port to reach spanning-tree root.


### 8.22 cist_path_cost column

The CIST path cost from the transmitting bridge to the CIST regional root.


### 8.23 port_priority column

Set this value to specify the port-priority. configurable in increments of 16.
Default value is 128.


### 8.24 restricted_port_tcn_disable column

Set this value to `true` if restiricted port tcn is enabled(not to propagate
topology changes to other ports). Default is `false`.


### 8.25 cist_regional_root_id column

The regional root Id for the CIST.


### 8.26 oper_edge_port column

The operational port type as edge port or not for the CIST.


### 8.27 bpdus_tx_enable column

Set this value to `false` not to transmit the BPDUs Default is `true`.


## 9. Daemon table

Each entry in this table represents a single system daemon and contains
information about that specific daemon. One use is to identify those daemons
that read and process hardware description files to add new hardware into the
db.


### 9.1 is_hw_handler column

A boolean to indicate if this daemon is responsible for processing hardware
description information (either on boot, or as hardware subsystems are added or
removed).


### 9.2 cur_hw column

Sequence number that a daemon sets to the current value of
[next_hw](System.next_hw) in the [System](System) table after it has
successfully responded to a hardware change.


### 9.3 name column

The name of the daemon.


## 10. Route_Map table



### 10.1 route_map_entries column

Route map entries keyed by preference value.


### 10.2 status column



### 10.3 external_ids column



### 10.4 other_config column



### 10.5 name column

Reference to the VRF table, to which this route belongs.


## 11. Route_Map_Entry table



### 11.1 status column



### 11.2 set column

The set rule for route map.


### 11.3 exitpolicy column

Rather than normal exiting, route map can continue on processing next route map,
or goto N route map and continue on processing.


### 11.4 description column



### 11.5 call column

If call command is used, nextrm indicate which route map to goto.


### 11.6 match_community_list column

Match routes based on community list.


### 11.7 other_config column



### 11.8 set_community_list_delete column

Removes communities from the specified community list for BGP route
advertisements.


### 11.9 match_extcommunity_list column

Match routes based on extended community list.


### 11.10 goto_target column

If exitpolicy is goto, nextpref is the route map to jump to.


### 11.11 match_ipv4_prefix_list column

Match routes based on IPv4 prefix list.


### 11.12 action column

There are three types, permit, deny, and any.


### 11.13 match_as_path column

Match routes based on AS path.


### 11.14 external_ids column



### 11.15 match column

The match rule for route map. Default is deny.


### 11.16 match_ipv6_prefix_list column

Match routes based on IPv6 prefix list.


## 12. BGP_ASPath_Filter table



### 12.1 deny column

Denied POSIX regular expressions.


### 12.2 name column

Name of the as-path filter.


### 12.3 permit column

Permitted POSIX regular expressions.


## 13. Prefix_List table



### 13.1 prefix_list_entries column

Prefix list entries keyed by preference value.


### 13.2 external_ids column



### 13.3 other_config column



### 13.4 name column

Name of the prefix list.


### 13.5 description column



## 14. Prefix_List_Entry table



### 14.1 le column



### 14.2 other_config column



### 14.3 ge column



### 14.4 prefix column



### 14.5 action column

There are three types, permit, deny, and any.


### 14.6 external_ids column



## 15. BGP_Community_Filter table



### 15.1 deny column

Denied POSIX regular expressions.


### 15.2 type column

There are two types, either "extcommunity-list" or "community-list".


### 15.3 name column

Name of the list.


### 15.4 permit column

Permitted POSIX regular expressions.


## 16. Route table

Global routes information base within an [System](System).

A [Route](Route) record represents a route. This is a unique record per (vrf,
prefix, protocol) set.


### 16.1 distance column

Administrative distance for the route entry. This value is populated every time
a protocol or a user adds a new entry. The default value is 1 which is the
default distance for static routes.


### 16.2 from column

Protocol that is responsible for this entry. The value is `bgp` if BGP created
this entry, `static` when the user configures a static route, `connected` if it
is a directly connected device and `ospf` if OSPF created this entry.


### 16.3 address_family column

Represents the address family for this entry. Default value is `ipv4`.


### 16.4 protocol_specific column



### 16.5 metric column

This is the BGP Multi Exit Discriminator (MED) attribute used in best path
selection. The MED provides a dynamic way to influence another AS in the way to
reach a certain route when there are multiple entry points for that AS.  BGP
decision process takes weight, local preference, AS path, Origin and MED into
account.  For selection, if all other factors are equal, the exit point with the
lowest MED is preferred. Default value is 0


### 16.6 selected column

Route table can have entries which may not be selected for forwarding. This flag
indicates if this entry is selected as an active route for forwarding. Default
is `false`.


### 16.7 sub_address_family column

Represents more information regarding this entry. Default is `unicast`.


### 16.8 prefix column

IPv4 or IPv6 destination prefix and mask in the address/mask format. Example
192.168.0.0/16


### 16.9 vrf column

Reference to the VRF table, to which this route belongs.


### 16.10 protocol_private column

Indicates that this row is a protocol specific route entry. The entries which
have this value set, should not participate in routing. Example: BGP can store
routes for reference and future selection but should not currently be used for
forwarding. Default is `false`.


### 16.11 nexthops column

List of all the nexthops for this entry. This will be empty in case of
blackhole.


## 17. Nexthop table

Global list of all the nexthops as used by the [Route](Route) table. Each entry
in the [Route](Route) can have a reference to one or many(for ECMP) entries in
this table.


### 17.1 status column



### 17.2 selected column

Indicates if this nexthop is actively participating in forwarding. Multiple
nexthops can exist for each route entry but the routing protocol can indicate if
a particular nexthop should not be used in forwarding. Default is `true`.


### 17.3 weight column

Weight is used to differentially balance the packets. Example: For a route if
there are 2 nexthops nh1 with weight 5 and nh2 with weight 1, then for every 5
packets that uses nh1, one packet will use nh2. In the first release, the above
case is not supported. Only ECMP is supported. Default is 0 (for static routes).


### 17.4 type column

Type of the nexthop. Default is `unicast`.


### 17.5 other_config column



### 17.6 external_ids column



### 17.7 ip_address column

IP address of the nexthop device.


### 17.8 ports column

List of outgoing ports. Nexthop entries of type `unicast` can have atmost 1
port.


## 18. BGP_Router table



### 18.1 router_id column

Specifies the router-id for given ASN.


### 18.2 status column



### 18.3 redistribute column

Specifies which protocol routes should be redistributed into BGP. The routes can
be filtered by specifying the route-map.


### 18.4 deterministic_med column

When enabled, selects the best-MED path among paths advertised from the
neighboring AS. Default is false.


### 18.5 bgp_neighbors column

BGP neighbors or neighbor groups, keyed by IP for the former or any     string
name for the latter.


### 18.6 always_compare_med column

Compares MED (Multi-Exit Discriminitor) from different neighbors. Default is
false.


### 18.7 other_config column



### 18.8 gr_stale_timer column

Specifies the maximum time to hold onto restarting peer stale paths. Range:
1-3600 seconds. Default value is 360 seconds.


### 18.9 fast_external_failover column

Enables fast external failover for BGP directly connected peering sessions.
Default is false.


### 18.10 timers column



### 18.11 log_neighbor_changes column

Enables logging of BGP neighbor status changes. Default is false.


### 18.12 external_ids column



### 18.13 networks column

Announces networks for given bgp router.


### 18.14 maximum_paths column

Number of paths BGP may install into the routing table. If not specified, BGP
selects a single path. Default is 1.


## 19. BGP_Neighbor table

This table holds both BGP neighbors and BGP peer groups.  A boolean named
is_peer_group identifies whether a specific entry is a bgp neighbor or a peer
group.


### 19.1 update_source column

Specifies the source-address to establish BGP connections to neighbors.


### 19.2 weight column

This is the weight for routes from this neighbor.


### 19.3 local_interface column

Reference to the corresponding interface.  This is used only for ipv6. Default
is none.


### 19.4 bgp_peer_group column

This column is used only if the entry is a BGP neighbor.  It represents the peer
group this BGP neighbor is a member of.  Default is none.


### 19.5 shutdown column

Specifies whether the neighbor has been administratively shut down. If not
specified, the default is false.


### 19.6 aspath_filters column

Name and direction of the as-path filters.


### 19.7 route_maps column

Name and direction of the route maps.


### 19.8 remove_private_as column

Specifies whether private AS should be removed. If not specified, the default
value is false.


### 19.9 prefix_lists column

Name and direction of the prefix lists.


### 19.10 inbound_soft_reconfiguration column

Allow inbound soft reconfiguration for this neighbor.


### 19.11 statistics column



### 19.12 remote_as column

Peer AS number. For EBGP, the peer is in another AS, so the remote AS number
must be different from the local router's AS number or BGP router asn. For IBGP,
the peer is in the same AS, so the two AS numbers must be the same. Remote AS
number. Range: 1-4294967295.


### 19.13 ttl_security_hops column

Specifies the maximum number of hops to the BGP peer.


### 19.14 ebgp_multihop column

If set to "true", allows BGP connections with peers that are not directly
connected. Default is "false".


### 19.15 passive column

Indicates that open messages should NOT be sent to this neighbor. Default is
false.


### 19.16 advertisement_interval column

Minimum interval between sending BGP routing updates. Range: 0-600 seconds.


### 19.17 allow_as_in column

Allow-as-in is the number of times BGP can allow an instance of AS to be in the
AS_PATH.


### 19.18 status column

These values describe various status information about this BGP neighbor or BGP
Peer group entry.


### 19.19 description column

This is an optional string which can be used for describing this entry. Default
is empty.


### 19.20 local_as column

To specify a different asn from BGP router asn to be used as local AS number in
update messages to peers. Local AS number. Range: 1-4294967295.


### 19.21 external_ids column



### 19.22 password column

The password for this entry.


### 19.23 tcp_port_number column

This is the BGP neighbor's tcp port number.  Default value is 179.


### 19.24 is_peer_group column

This is a flag which identifies whether this specific entry is an individual BGP
neighbor or is a BGP peer group.  A value of true implies a peer group.
Otherwise, the entry represents a BGP neighbor.  If the value is not set, it
implies false.


### 19.25 other_config column



### 19.26 timers column

BGP per neighbor timers - Connect timer/Keep-alive Interval.


### 19.27 maximum_prefix_limit column

Maximum number of prefixes that can be accepted on a BGP peer session. When the
limit is exceeded, a system log message is logged.


## 20. Recursive_Nexthop table

Recursive next hop resolution. When a protocol has a new recursive next hop and
its reachability is unknown, the protocol requests the recursive next hop to be
resolved. The result is represented as nh_ips, nh_metric, and nh_ports.


### 20.1 rnh_ip column

IPv4 or IPv6 recursive next hop address to be resolved. Example 192.168.0.2


### 20.2 rnh_from column

This indicates from which protocol the request comes.


### 20.3 nh_metric column

The cost to reach the forwarding next hops that the recursive next hop is
resolved to.


### 20.4 vrf column

Reference to the VRF to which this entry belongs to.


### 20.5 nh_ips column

The IPv4 or IPv6 addresses of the forwarding next hops that the recursive next
hop is resolved to. It is possible that the recursive next hop is resolved to a
single forwarding next hop or a ECMP which consists a list of forwarding next
hops. Example 12.1.0.2


### 20.6 nh_ports column

The ports of the forwarding next hops that the recursive next hop is resolved
to. It is possible that the recursive next hop is resolved to a single
forwarding next hop or a ECMP which consists a list of next hops.


## 21. BGP_Route table

BGP local RIB.


### 21.1 origin column

Origin of the BGP route. Allowed values are
<mark>egp</mark>,<mark>igp</mark>,<mark>incomplete</mark> igp origin code
specifies whether route entry originated from an Interior Gateway Protocol (IGP)
and was advertised with a network router configuration command. egp origin code
specifies whether route entry originated from an Exterior Gateway Protocol
(EGP). incomplete origin code is assigned to redistributed routes. Default value
is igp.


### 21.2 weight column

Weight of the BGP route. Default value is 32768


### 21.3 metric column

This is the BGP Multi Exit Discriminator (MED) attribute used in best path
selection. Default value is 0


### 21.4 creation_time column

Time in seconds, at which the route arrived from the neighbor. Value is the
number of seconds elapsed since epoch. Default value is 0.


### 21.5 community column

Space delimited list of community names for the route. No value means that no
community names are associated with the route.


### 21.6 peer column



### 21.7 prefix column

IPv4 or IPv6 destination prefix and mask in the address/mask format. Example
192.168.0.0/16


### 21.8 address_family column

Represents the address family for this entry. Default value is `ipv4`.


### 21.9 aggregator column

IP address of the BGP node responsible for route aggregation. Value is empty if
route is not aggregated.


### 21.10 aspath column

Aspath for a BGP route. Aspath is the list of autonomous system numbers of the
BGP nodes traversed by the route before reaching local node. Aspath contains
key-value pairs with keys corresponding to the position of the autonomous system
number in the list of autonomous system numbers and values corresponding to
autonomous system numbers.


### 21.11 sub_address_family column

Represents subsequent address family identifier such as unicast, multicast or
MPLS VPN. Default is `unicast`.


### 21.12 aggregator_as column

Originating AS number of the aggregate route. Default value is 0.


### 21.13 ecommunity column

Space delimited list of extended community names for the route. No value means
that no extended community names are associated with the route.


### 21.14 vrf column

Reference to the VRF to which this route belongs.


### 21.15 protocol_iBGP column

Specifies whether the route was learned through iBGP session. Default value is
false.


### 21.16 aggregate column

True if notification is sent to upstream routers that the route is aggregated.
Default value is false.


### 21.17 protocol_internal column

Specifies whether the route originated locally on the BGP peer. Default value is
false.


### 21.18 distance column

Administrative distance for the route entry. Default value is 0.


### 21.19 path_attributes column



### 21.20 flags column

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


### 21.21 local_pref column

Local preference of the BGP route. Default value is 0.


### 21.22 bgp_nexthops column

Represents nexthops for this entry. Each entry in the [BGP_Route](BGP_Route) can
have a reference to one or many(for ECMP) nexthop entries.


## 22. BGP_Nexthop table

List of all nexthops used by BGP. Each entry in the BGP RIB can have a reference
to one or many (for ECMP) nexthop entries.


### 22.1 ip_address column

IP address of the nexthop device.


### 22.2 type column

Type of the nexthop. Default is `unicast`.


## 23. Neighbor table

List of all the connected neighbors.


### 23.1 status column



### 23.2 address_family column

Address family of the neighbor.


### 23.3 mac column

MAC address learned for this neighbor.


### 23.4 state column

Current state of the neighbor entry.


### 23.5 vrf column

Reference to the VRF table, to which this neighbor belongs.


### 23.6 ip_address column

The IPv4 address or the IPv6 address of neighbor


### 23.7 port column

Port on which this neighbor was learned.


## 24. VLAN table



### 24.1 macs_invalid column

If `true`, indicates that MACs on this VLAN are invalid. This might be set by
any agent of the system that decides that MACs are indeed invalid. Eventually
those MACs will be cleared from the system and macs_invalid will revert to
`false`.


### 24.2 description column

User provided description of this VLAN.


### 24.3 aclv4_in_cfg_version column

The version of the 'aclv4_in_cfg' column. This value is incremented by the
management interface each- CLI/REST/Web UI, etc. every time it changes the
'aclv4_in_cfg' value. An empty value means no ACL has been configured for the
VLAN.


### 24.4 aclv4_in_cfg column

ACL, potentially in flight, desired to be applied to this VLAN, as identified in
the [ACL](ACL).


### 24.5 admin column

Administratively configured state of this VLAN. Default is down if not
specified.


### 24.6 aclv4_in_status column

The status of the last version of 'aclv4_in_cfg' column, that has been processed
by switchd.


### 24.7 other_config column



### 24.8 id column

The ID of this VLAN.


### 24.9 aclv4_in_statistics column



### 24.10 aclv4_in_statistics_clear_performed column

The number of times that ACL statistics for this VLAN have been cleared..


### 24.11 hw_vlan_config column

Key-value pairs that represent the configuration passed down to hardware.


### 24.12 oper_state column

Operational state of this VLAN.


### 24.13 oper_state_reason column

Human readable reason for the operational state of this VLAN.


### 24.14 internal_usage column

Key-value pairs that represent how this VLAN is used internally by the system.


### 24.15 external_ids column



### 24.16 aclv4_in_statistics_clear_requested column

The number of times a request was made to clear the ACL statistics for this
VLAN.


### 24.17 aclv4_in_applied column

Current, successfully applied ACL to this VLAN, as identified in the [ACL](ACL)


### 24.18 name column

VLAN name.  Should be alphanumeric and no more than about 8 bytes long.


## 25. Port table

A port within a [Bridge](Bridge).

Most commonly, a port has exactly one ``interface,'' pointed to by its
[interfaces](Port.interfaces) column.  Such a port logically corresponds to a
port on a physical Ethernet switch.  A port with more than one interface is a
''bonded port'' (see [Bonding Configuration] (Bonding Configuration)).

Some properties that one might think as belonging to a port are actually part of
the port's [Interface](Interface) members.

If port has an IP address, then it becomes L3 and might participate in VRFs.
Unless referenced interface has an "internal" type, L3 port can not participate
in the bridge. "internal" ports that basically represent VLAN interfaces may be
referenced by both Bridge and VRF.


### 25.1 egress_redirect_to_port column

When set, egress traffic of this port will be redirected to the referenced port.


### 25.2 trunks column

For a trunk, native-tagged, or native-untagged port, the 802.1Q VLAN or VLANs
that this port trunks; if it is empty, then the port trunks all VLANs defined in
the [VLAN](VLAN) table.  Must be empty if this is an access port.

A native-tagged or native-untagged port always trunks its native VLAN,
regardless of whether [trunks](Port.trunks) includes that VLAN.


### 25.3 qos column

References schedule profile for this port. If this is unspecified, then the
schedule profile referenced in [System](System)) table qos will be used.


### 25.4 ip4_address_secondary column

This is a list of secondary IPv4 addresses and subnet mask in the address/mask
format.


### 25.5 aclv4_in_cfg column

ACL, potentially in flight, desired to be applied to this port, as identified in
the [ACL](ACL).


### 25.6 aclv4_in_status column

The status of the last version of 'aclv4_in_cfg' column, that has been processed
by switchd.


### 25.7 bond_options column



### 25.8 qos_config column



### 25.9 tag column

For an access port, the port's implicitly tagged VLAN.  For a native-tagged or
native-untagged port, the port's native VLAN.  Must be empty if this is a trunk
port.


### 25.10 kernel_interface_ready column

Indicates whether kernel interface is provisioned for the port. Default is
false.


### 25.11 ip6_address column

The IPv6 address and subnet mask in the address/mask format. This is the primary
IPv6 address.


### 25.12 ospf_if_out_cost column

The output cost assigned to the corresponding OSPFv2 interface. The default
value depends on the interface bandwidth and on the auto-cost reference
bandwidth.


### 25.13 ip6_address_secondary column

This is a list of secondary IPv6 addresses and subnet mask in the address/mask
format.


### 25.14 q_profile column

References queue profile for this port. If this is unspecified, then the queue
profile referenced in [System](System)) table q_profile will be used.


### 25.15 loop_protect_vlan column



### 25.16 dhcp_relay_statistics column



### 25.17 bond_active_slave column



### 25.18 ospf_auth_text_key column

The authentication key for OSPFv2 authentication type "text".


### 25.19 loop_protect_status column



### 25.20 flood_block column

When set to &#8216;true&#8217;, all flood traffic received from and forwarded to
this port will be dropped. The default value is `false`.


### 25.21 vlan_options column



### 25.22 ospf_intervals column



### 25.23 egress_blocked_to_ports column

When set, all traffic which ingresses this port will be blocked from being
forwarded out of the specified ports.


### 25.24 ip4_address column

The IPv4 address and subnet mask in the address/mask format. This is the primary
IP address.


### 25.25 aclv4_in_statistics_clear_requested column

The number of times a request was made to clear the ACL statistics for this
port.


### 25.26 ospf_priority column

The router with the highest priority will be more eligible to become Designated
Router. Setting the value to 0, makes the router ineligible to become Designated
Router. The default value is 1.


### 25.27 status column

Key-value pairs that report port status.


### 25.28 loop_protect_statistics column



### 25.29 lacp_status column

Key-value pairs that report lacp-specific port status.


### 25.30 hw_config column

Key-value pairs that represent the configuration passed down to hardware.


### 25.31 macs_invalid column

If `true`, indicates that MACs on this port are invalid. This might be set by
any agent of the system that decides that MACs are indeed invalid. Eventually
those MACs will be cleared from the system and macs_invalid will revert to
`false`.


### 25.32 ospf_auth_type column

The type of OSPFv2 authentication. If not set, then parent area level
authentication holds for the port.


### 25.33 interfaces column

The port's interfaces.  If there is more than one, this is a bonded Port. A
maximum of 8 interfaces can be assigned to a port.


### 25.34 loop_protect_port_disabled column

This value will be set to `true`,if the port is disabled by Loop-protect.
Default value is `false`.


### 25.35 bond_mode column

The type of bonding used for a bonded port. Bond mode controls the selection of
a interface from a group of aggregate interfaces with which to transmit a frame.
This selection is performed with a hash function using either source and
destination mac addresses (l2), ip addresses (l3) or tcp/udp ports (l4) as
parameters. Defaults to `l3-src-dst-hash` if not assigned.


### 25.36 statistics column



### 25.37 loop_protect_action column

This determines action for the Loop-protect feature.The value is set to "tx-
port-disable" for disabling the sending port on detecting a loop, "tx-rx-
disable" disables both sending and receiving ports when loop is detected and
"do-not-disable" will not disable any port. Default value is `tx-port-disable`.


### 25.38 vlan_mode column

The VLAN mode of the port, as described above.  When this column is empty, a
default mode is selected as follows:

+ If [tag](Port.tag) contains a value, the port is an access port.  The
[trunks](Port.trunks) column should be empty.
+ Otherwise, the port is a trunk port.  The [trunks](Port.trunks) column value
is honored if it is present.


### 25.39 external_ids column



### 25.40 loop_protect_enable column

When set to `true`, Loop-protect is enabled on this port. Default value is
`false`.


### 25.41 ospf_if_type column

The type of the OSPFv2 network interface. The default value is the type of the
interface from the Interface table.


### 25.42 bond_status column

Key-value pairs that report bond-specific port status (both static and dynamic).
This column complements the [lacp_status](Port.lacp_status) column.


### 25.43 lacp column

Configures LACP on this port.  LACP allows directly connected switches to
negotiate which links may be bonded.  LACP may be enabled on non-bonded ports
for the benefit of any switches they may be connected to.  `active` ports are
allowed to initiate LACP negotiations.  `passive` ports are allowed to
participate in LACP negotiations initiated by a remote switch, but not allowed
to initiate such negotiations themselves.  If LACP is enabled on a port whose
partner switch does not support LACP, the bond will be disabled. Defaults to
`off` if unset.


### 25.44 name column

Port name.  Should be alphanumeric and no more than about 8 bytes long.  May be
the same as the interface name, for non-bonded ports.  Must otherwise be unique
among the names of ports, interfaces, and bridges on a host.


### 25.45 aclv4_in_cfg_version column

The version of the 'aclv4_in_cfg' column. This value is incremented by the
management interface - CLI/REST/Web UI, etc. every time it changes the
'aclv4_in_cfg' value. An empty value means no ACL has been configured for the
port.


### 25.46 vlan_tunnel_keys column

Specifies translation from a vlan to the [Logical_Switch](Logical_Switch). If
this is an access port, only one key needs to be specified. VLAN 0 means that
untagged traffic on the port is mapped to the specified logical switch.


### 25.47 admin column

The administrative state of the Port configured by user. The port admin state
determines the hardware configuration based on the business logic. When port
"admin" is configured down the interface(s) associated with the port should
force their hardware configuration to down. By default the port is up.


### 25.48 mac_learn_disable column

When set to 'true', mac learning will be disabled on the port. The default value
is `false`.


### 25.49 other_config column



### 25.50 mac column

The MAC address to use for this port for the purpose of choosing the bridge's
MAC address.  This column does not necessarily reflect the port's actual MAC
address, nor will setting it change the port's actual MAC address.


### 25.51 ospf_mtu_ignore column

This determines if OSPFv2 should ignore any IP MTU mismatch with a neighbor or
not. The default value is false, that is not to establish adjacency if the
neighbor MTU does not match the local interface MTU.


### 25.52 aclv4_in_statistics_clear_performed column

The number of times the ACL statistics for this port have been cleared.


### 25.53 macs_invalid_on_vlans column

If a set of VLANs is specified, it indicates that MACs on this port and that set
of VLANs are invalid. This might be set by any agent of the system that decides
that MACs are indeed invalid. Eventually those MACs will be cleared from the
system and macs_invalid_on_vlans will revert to an empty set.


### 25.54 forwarding_state column

The Port's forwarding state is determined by the state of the interface or
interfaces in case of LAG and by the information provided by protocols working
at the logical port level, MSTP for example.

The value is set after all possible conditions have been taken into account.
The conditions are evaluated by an arbiter that takes the decision of which
value to set on the forwarding state based on protocol state.


### 25.55 qos_status column



### 25.56 aclv4_in_applied column

Current, successfully applied ACL to this port, as identified in the [ACL](ACL)


### 25.57 mclag_remote_interfaces column

List of interfaces on the MCLAG peer device which are part of same LAG.
[MCLAG_Remote_Interface](MCLAG_Remote_Interface)


### 25.58 ospf_auth_md5_keys column

The authentication keys for OSPFv2 authentication type "md5".


### 25.59 aclv4_in_statistics column



## 26. Interface table

An interface within a [Port](Port).


### 26.1 hw_bond_config column

Key-value pairs that configure the interface as a member of bond.


### 26.2 split_parent column

For a split child interface, this is the reference to the parent
[Interface](Interface).


### 26.3 link_state column

The observed state of the physical network link.  This is ordinarily the link's
carrier status.


### 26.4 mclag_status column



### 26.5 subintf_parent column

For a subinterface, this column holds the reference to the parent interface
[Interface](Interface). The key is the dot1q encapsulation vlan id and the value
is the uuid of parent interface.


### 26.6 kernel_interface_ready column

Indicates whether kernel interface is provisioned.  Default is false.


### 26.7 user_config column

Key-value pairs that stores the user configuration of [Interface](Interface).


### 26.8 queue_tx_bytes column

For each outbound queue, a count of the queue's total bytes transmitted.


### 26.9 link_resets column

The number of times OpenSwitch has observed the
[link_state](Interface.link_state) of this [Interface](Interface) change.


### 26.10 queue_tx_errors column

For each outbound queue, a count of the queue's total transmit errors or drops.


### 26.11 statistics column



### 26.12 duplex column

The duplex mode of the physical network link.


### 26.13 hw_status column



### 26.14 lldp_neighbor_info column

Keys-value pairs of neighbor's port info as discovered by LLDP.


### 26.15 type column

The interface type, one of:

+ __`system`__:  An ordinary network device, e.g. `eth0` on Linux. Sometimes
referred to as ``external interfaces'' since they are generally connected to
hardware external to that on which the OpenSwitch is running.  The empty string
is a synonym for `system`.
+ __`internal`__:  A simulated network device that sends and receives traffic.
An internal interface whose [name](Interface.name) is the same as its bridge's
[name](Bridge.name) is called the ``local interface.''  It does not make sense
to bond an internal interface, so the terms ``port'' and ``interface'' are often
used imprecisely for internal interfaces.
+ __`vlansubint`__:  A sub-interface created for a physical interface. Sub-
interfaces are used for router-on-stick configurations and to allow separation
of traffic on a L3 physical interface based on dot1q encapsulation VLAN and
apply policies on them.
+ __`loopback`__:  A loopback interface is a virtual interface, supporting
IPv4/IPv6 address configuration, that remains up until it is deleted by
administrator. Loopback interface IP address is used as router-id and source
address by many protocols.
+ __`vxlan`__:  This is a vitual interface of type vxlan (L2 overlay over L3
network RFC 7348).


### 26.16 lacp_current column

Boolean value indicating LACP status for this interface.  If true, this
interface has current LACP information about its LACP partner.  This information
may be used to monitor the health of interfaces in a LACP enabled port.  This
column will be empty if LACP is not enabled.


### 26.17 status column

Key-value pairs that report port status.  Supported status values are
[type](Interface.type)-dependent; some interfaces may not have a valid
[driver_name](Interface.status.driver_name), for example.


### 26.18 lacp_status column

Key-value pairs that report LACP protocol status.


### 26.19 mac_in_use column

The MAC address in use by this [Interface](Interface).


### 26.20 hw_intf_config column

Key-value pairs that represent the configuration passed down to hardware.


### 26.21 link_speed column

The negotiated speed of the physical network link in bits per second. Valid
values are positive integers greater than 0.


### 26.22 pause column

The status of the Ethernet PAUSE (link-level flow control) mode of the physical
network link.


### 26.23 admin_state column

The administrative state of the physical network link.


### 26.24 external_ids column



### 26.25 lldp_statistics column



### 26.26 split_children column

For a split parent interface, this is the reference to the list of children
[Interface](Interface)s.


### 26.27 hw_intf_info column

Key-value pairs that show the information about a physical interface.


### 26.28 name column

Interface name.  Should be alphanumeric and no more than about 8 bytes long.
May be the same as the port name, for non-bonded ports.  Must otherwise be
unique among the names of ports, interfaces, and bridges on a host.


### 26.29 queue_tx_packets column

For each outbound queue, a count of the queue's total packets transmitted.


### 26.30 bond_status column

Key-value pairs that report the status of a bond.  This applies to both static
or LACP bonds.


### 26.31 other_config column



### 26.32 mtu column

The MTU (maximum transmission unit); i.e. the largest amount of data that can
fit into a single Ethernet frame. The standard Ethernet MTU is 1500 bytes.  Some
physical media and many kinds of virtual interfaces can be configured with
higher MTUs.

This column will be empty for an interface that does not have an MTU as, for
example, some kinds of tunnels do not.


### 26.33 forwarding_state column



### 26.34 error column

If the configuration of the [Interface](Interface) failed, OpenSwitch sets this
column to an error description in human readable form.  Otherwise, OpenSwitch
clears this column.


### 26.35 pm_info column

Key-value pairs that report pluggable module information.


### 26.36 options column



## 27. MCLAG table



### 27.1 device_priority column

Configures MCLAG device priority. The default value is `1`. Device with the
lower value of priority will be the primary in the case of split brain handling.


### 27.2 split_brain_handling column

Configures how MCLAG split-brain is handled. "one-fragment-active" means in case
of a split, MCLAG links of primary will be active and secondary will be
disabled. "dual-active" means in case of a split, MCLAG links of both primary
and secondary will be active. The default value is `one-fragment-active`.


### 27.3 isl_port column

References port to be used as inter switch link.


### 27.4 keepalive_status column



### 27.5 isl_statistics column



### 27.6 oper_status column



### 27.7 keepalive_port column

Specifies L3 port for keepalive [Port](Port).


### 27.8 isl_timers column



### 27.9 keepalive_vrf column

VRF to be used for keepalive routing. If not configured, keepalive functionality
is disabled.


### 27.10 keepalive_udp_port column

UDP port number of peer device. The default value is `7678`.


### 27.11 keepalive_statistics column



### 27.12 peer_status column



### 27.13 keepalive_src_ip column

IPv4 address of the device. If not configured, keepalive functionality is
disabled.


### 27.14 keepalive_peer_ip column

IPv4 address of the peer device. If not configured, keepalive functionality is
disabled.


### 27.15 keepalive_timers column



## 28. MCLAG_Remote_Interface table

Each entry contains the information about a physical interface on the peer
switch which is configured for MCLAG. This information is determined by
exchanging packets over the ISL link between the MLAG switches.


### 28.1 lacp_partner_system_id column

Peer interface's LACP partner system ID.


### 28.2 name column

Name of the peer interface.


### 28.3 duplex column

The duplex mode of the physical network link.


### 28.4 link_state column

The observed state of the physical network link.  This is ordinarily the link's
carrier status.


### 28.5 link_speed column

The negotiated speed of the physical network link in bits per second. Valid
values are positive integers greater than 0.


### 28.6 admin_state column

The administrative state of the physical network link.


### 28.7 lacp_partner_port_id column

Peer interface's LACP partner port ID.


### 28.8 lacp_partner_state column

LACP partner state.


### 28.9 lacp_partner_key column

Peer interface's LACP partner key.


## 29. Fan table



### 29.1 status column



### 29.2 direction column



### 29.3 name column



### 29.4 rpm column



### 29.5 other_config column



### 29.6 hw_config column



### 29.7 external_ids column



### 29.8 speed column



## 30. LED table



### 30.1 status column

Status of the LED is the current operational status.


### 30.2 other_config column



### 30.3 state column

State of the LED controls the lighting behavior.


### 30.4 hw_config column



### 30.5 external_ids column



### 30.6 id column

Logical name of the LED.


## 31. Temp_sensor table



### 31.1 status column

Results of evaluation of the current temperature against the sensor's threshold
values.


### 31.2 name column

Logical name of the temperature sensor, including the subsystem name and numeric
identifier of the temperature sensor.


### 31.3 min column

Historic minimum (since last restart of tempd process), in milidegrees Celcius.


### 31.4 fan_state column

Recommended minimum fan setting based on current temperature. The fand process
should choose the worst-case sensor fan_state when determining the fan setting
for the subsystem.


### 31.5 max column

Historic maximum (since last restart of tempd process), in milidegrees Celcius.


### 31.6 other_config column



### 31.7 location column

Descriptive text for the physical location of the temperature sensor relative to
the subsystem.


### 31.8 hw_config column



### 31.9 external_ids column



### 31.10 temperature column

Current temperature reading, in milidegrees Celcius.


## 32. Power_supply table

Information for a power supply unit (PSU).


### 32.1 status column



### 32.2 statistics column

Various statistics about the PSU.


### 32.3 name column



### 32.4 characteristics column

Electrical characteristics.


### 32.5 other_config column



### 32.6 hw_config column



### 32.7 external_ids column



### 32.8 identity column

PSU identification.


## 33. Manager table

Configuration for a database connection to an OpenSwitch database (OVSDB)
client.

This table primarily configures the OpenSwitch database (`ovsdb-server`), not
the OpenSwitch switch (`ovs-vswitchd`).  The switch does read the table to
determine what connections should be treated as in-band.

The OpenSwitch database server can initiate and maintain active connections to
remote clients.  It can also listen for database connections.


### 33.1 max_backoff column

Maximum number of milliseconds to wait between connection attempts. Default is
implementation-specific.


### 33.2 status column



### 33.3 target column

Connection method for managers.

The following connection methods are currently supported:

+ __`ssl:_ip_`[`:_port_`]__:    The specified SSL _port_ on the host at the
given _ip_, which must be expressed as an IP address (not a DNS name).  The
[ssl](System.ssl) column in the [System](System) table must point to a valid SSL
configuration when this form is used.   If _port_ is not specified, it currently
defaults to 6632.  In the future, the default will change to 6640, which is the
IANA-defined value.   SSL support is an optional feature that is not always
built as part of OpenSwitch.
+ __`tcp:_ip_`[`:_port_`]__:    The specified TCP _port_ on the host at the
given _ip_, which must be expressed as an IP address (not a DNS name), where
_ip_ can be IPv4 or IPv6 address.  If _ip_ is an IPv6 address, wrap it in square
brackets, e.g. `tcp:[::1]:6632`.   If _port_ is not specified, it currently
defaults to 6632.  In the future, the default will change to 6640, which is the
IANA-defined value.
+ __`pssl:`[_port_][`:_ip_`]__:    Listens for SSL connections on the specified
TCP _port_. Specify 0 for _port_ to have the kernel automatically choose an
available port.  If _ip_, which must be expressed as an IP address (not a DNS
name), is specified, then connections are restricted to the specified local IP
address (either IPv4 or IPv6 address).  If _ip_ is an IPv6 address, wrap in
square brackets, e.g. `pssl:6632:[::1]`.  If _ip_ is not specified then it
listens only on IPv4 (but not IPv6) addresses. The [ssl](System.ssl) column in
the [System](System) table must point to a valid SSL configuration when this
form is used.   If _port_ is not specified, it currently defaults to 6632.  In
the future, the default will change to 6640, which is the IANA-defined value.
SSL support is an optional feature that is not always built as part of
OpenSwitch.
+ __`ptcp:`[_port_][`:_ip_`]__:    Listens for connections on the specified TCP
_port_. Specify 0 for _port_ to have the kernel automatically choose an
available port.  If _ip_, which must be expressed as an IP address (not a DNS
name), is specified, then connections are restricted to the specified local IP
address (either IPv4 or IPv6 address).  If _ip_ is an IPv6 address, wrap it in
square brackets, e.g. `ptcp:6632:[::1]`.  If _ip_ is not specified then it
listens only on IPv4 addresses.   If _port_ is not specified, it currently
defaults to 6632.  In the future, the default will change to 6640, which is the
IANA-defined value.

When multiple managers are configured, the [target](Manager.target) values must
be unique.  Duplicate [target](Manager.target) values yield unspecified results.


### 33.4 connection_mode column

If it is specified, this setting must be one of the following strings that
describes how OpenSwitch contacts this OVSDB client over the network:

+ __`in-band`__:   In this mode, this connection's traffic travels over a bridge
managed by OpenSwitch.  With this setting, OpenSwitch allows traffic to and from
the client regardless of the contents of the OpenFlow flow table.  (Otherwise,
OpenSwitch would never be able to connect to the client, because it did not have
a flow to enable it.)  This is the most common connection mode because it is not
necessary to maintain two independent networks.
+ __`out-of-band`__:   In this mode, the client's traffic uses a control network
separate from that managed by OpenSwitch, that is, OpenSwitch does not use any
of its own network devices to communicate with the client. The control network
must be configured separately, before or after `pswitchd` is started.

If not specified, the default is implementation-specific.


### 33.5 other_config column



### 33.6 inactivity_probe column

Maximum number of milliseconds of idle time on connection to the client before
sending an inactivity probe message.  If OpenSwitch does not communicate with
the client for the specified number of seconds, it will send a probe.  If a
response is not received for the same additional amount of time, OpenSwitch
assumes the connection has been broken and attempts to reconnect.  Default is
implementation-specific. A value of 0 disables inactivity probes.


### 33.7 external_ids column



### 33.8 is_connected column

`true` if currently connected to this manager, `false` otherwise.


## 34. SSL table

SSL configuration for an System.


### 34.1 certificate column

Name of a PEM file containing a certificate, signed by the certificate authority
(CA) used by the controller and manager, that certifies the switch's private
key, identifying a trustworthy switch.


### 34.2 external_ids column



### 34.3 bootstrap_ca_cert column

If set to `true`, then OpenSwitch will attempt to obtain the CA certificate from
the controller on its first SSL connection and save it to the named PEM file. If
it is successful, it will immediately drop the connection and reconnect, and
from then on all SSL connections must be authenticated by a certificate signed
by the CA certificate thus obtained.  _This option exposes the SSL connection to
a man-in-the-middle attack obtaining the initial CA certificate._  It may still
be useful for bootstrapping.


### 34.4 private_key column

Name of a PEM file containing the private key used as the switch's identity for
SSL connections to the controller.


### 34.5 ca_cert column

Name of a PEM file containing the CA certificate used to verify that the switch
is connected to a trustworthy controller.


## 35. Radius_Server table

These radius servers are being used for authenticating when users wants to login
to the box.


### 35.1 retries column

Specifies the number of retries to radius server if there is no response.
Default retry value is 1.


### 35.2 passkey column

Specifies the passkey between radius client and radius server for
authentication. Default passkey is testing123-1.


### 35.3 udp_port column

Specifies the udp port number for authentication. Default udp port number for
authentication is 1812.


### 35.4 priority column

Specifies the order in which radius servers are configured on the switch.


### 35.5 timeout column

Specifies the timeout between authentication requests to radius server. Default
timeout is 5 seconds.


### 35.6 ip_address column

IP address of the radius server configured.


## 36. CLI_Alias table

Alias configurations for the command line interface.


### 36.1 alias_name column

Shortcut name configured by the user for a set of commands.


### 36.2 external_ids column



### 36.3 other_config column



### 36.4 alias_definition column

The list of commands to be executed when the shortcut is used. Different
commands can be separated by ";". Runtime arguments can be specified using $1,
$2 etc. Any extra arguments, will be added at the end of last command. Eg:
Execute the command "alias mycmd hostname $1; console length $2; console width
$3" to configure "mycmd" as shortcut. On executing "mycmd Switch1 80 24", it
will be expanded to "hostname Switch1; console length 80; console width 24".
"mycmd" will be stored in alias_name" and "hostname $1; console length $2;
console width $3" will be saved in alias_definition.


## 37. bufmon table

Configuration and status of the counters per Capacity Monitoring feature


### 37.1 status column

Specifies the status of the counter.


### 37.2 name column

Name of the counter as it will be shown in the management systems and will be
referenced by all the interested agents. No spaces should be used in the name.


### 37.3 counter_value column

Last collected value of the counter.


### 37.4 enabled column

Specifies whether counter is enabled.


### 37.5 hw_unit_id column

Identifies the ASIC that counter belongs to.


### 37.6 counter_vendor_specific_info column

Contains any information that might help ASIC specific driver to identify the
counter. Both keys and values are driver and ASIC specific.


### 37.7 trigger_threshold column

Specifies counter specific threshold that would trigger collection.


## 38. DHCP_Server table

DHCP Server configuration.


### 38.1 matches column

Matching incoming DHCP options.


### 38.2 static_hosts column

Static leases.


### 38.3 other_config column



### 38.4 bootp column

Key-value pairs that specifies BOOTP options for the DHCP clients.


### 38.5 ranges column

Dynamic IP address ranges.


### 38.6 dhcp_options column

DHCP options settings.


## 39. DHCPSrv_Range table

Dynamic IP address ranges configuration of the DHCP server.


### 39.1 is_static column

Set this value to `true` to assign static IP addresses to DHCP clients that have
static host configuration. If the value is set to `false`, then the IP addresses
in this range would be use for dynamic allocation. If not specifed, the IP
address range would be used for dynamic allocation.


### 39.2 name column

Identifier for DHCP Server IP address range configuration. This has to be unique
across all DHCP ranges and across all VRFs.


### 39.3 start_ip_address column

Specifies the start IPv4/IPv6 address of the dynamic IP address range.


### 39.4 set_tag column

Sets an alphanumeric label that marks the network so that dhcp options would be
specified on a per-network basis.


### 39.5 broadcast column

This is used only in IPv4 address ranges configuration. Specifies the broadcast
address that would be used for the assigned IP addresses in this range and this
would be sent to DHCP clients. If not specified, broadcast address of the switch
interface that received the DHCP request would be used.


### 39.6 netmask column

This is used only in IPv4 address ranges configuration. Specifies the netmask
that would be used for the assigned IP addresses in this range and this would be
sent to DHCP clients. If end ip address is not configured for this range, then
end ip address would be chosen based on the netmask. If netmask is not
specified, then netmask of the switch interface that received the DHCP request
would be used.


### 39.7 lease_duration column

Specifies the lease expiry time in minutes. If not specified, default value of
one hour (60) would be used.


### 39.8 constructor column

This is used only in IPv6 address ranges configuration. Specifies the interface
whose IP address would be used to calculate the end IP address for this range.
This is used when end ip address is not specified.


### 39.9 prefix_len column

This is used only in IPv6 address ranges configuration. Specifies the prefix
length that would be used for the assigned IPv6 addresses. If not specifed,
default value of 64 would be used.


### 39.10 match_tags column

Specifies the list of the tags that would be matched for the incoming DHCP
request on the interfaces whose IP addresses are in the configured range.


### 39.11 end_ip_address column

Specifies the end IPv4/IPv6 address of the dynamic IP address range. If not
specifed, then for IPv4 address family - end ip address would be calculated
based on the configured netmask for this range or based on the netmask of the
interface that received the DHCP request and for IPv6 family - end ip address
would be calculated based on the constructor template configuration.


## 40. DHCPSrv_Static_Host table

Static leases configured by the user.


### 40.1 set_tags column

Specifies the list of tags associated with the DHCP request. When a DHCP request
from the specific DHCP client is received, the list of configured tags would be
set and used to selectively send DHCP options for the client.


### 40.2 client_hostname column

Specifies the client hostname of the DHCP client to which the configured static
IP address would be assigned.


### 40.3 mac_addresses column

Specifies the list of MAC addresses of the DHCP hosts to which the static IP
address would be assigned. If more than one MAC addresses are specified, it
would work reliably only if one MAC address is active at a time.


### 40.4 lease_duration column

Specifies the lease expiry time in minutes. If not specified, default value of
one hour (60) would be used.


### 40.5 client_id column

Specifies the client id of the DHCP client to which the configured static IP
address would be assigned,


### 40.6 ip_address column

Specifies the static IP address that should be assigned to the specific
host.This ip address may contain an IPv4 address or an IPv6 address, or both.


## 41. DHCPSrv_Option table

Configuration to specify extra options (other than standard options) that would
be sent to the DHCP clients.


### 41.1 option_number column

Specifies the number of the extra option that should be sent to the DHCP
clients. The option number would be ignored if option name is specified.


### 41.2 option_name column

Specifies the name of the extra option that should be sent to the DHCP clients.


### 41.3 match_tags column

The option and option value specified in the configuration would be sent only if
the DHCP request from the client matches all the tags specified in this list.


### 41.4 option_value column

Specifies the value of the extra option that should be sent to the DHCP clients.


### 41.5 ipv6 column

Set this value to `true` if the configured option is for IPv6 and set to `false`
for IPv4 option. If not specifed, the configured option would be used for IPv4.


## 42. DHCPSrv_Match table

Configuration to set tags for the incoming DHCP requests based on the options
and its value sent by the clients.


### 42.1 option_number column

Specifies the number of the extra option that should be sent by the client to
set the configured tag for DHCP requests. The option number would be ignored if
option name is specified.


### 42.2 option_name column

Specifies the name of the option that should be sent by the client to set the
configured tag for DHCP requests.


### 42.3 option_value column

Specifies the value of the option that should be sent by the client to set the
configured tag for DHCP requests. If the value is not specified, then the tag
would be set for any value of the option.


### 42.4 set_tag column

Specifies the name of the tag that would be set if the incoming DHCP request has
the configured option and the value.


## 43. Logical_Switch table

Configuration for identifying overlay networks associated with bridges.


### 43.1 tunnel_key column

Tunnel key used in the overlay. For VXLAN, this is the VNI.


### 43.2 bridge column

Reference to a [Bridge](Bridge) participating in the overlay.


### 43.3 from column

The entity managing the overlay.


### 43.4 name column

Name of the overlay network.


### 43.5 description column

Description of the overlay network.


## 44. MAC table

Configuration for consolidated MAC table which can potentially be learnt from
ASIC, from the hw-vtep controller or statically configured.


### 44.1 status column



### 44.2 bridge column

Specifies the bridge [Bridge](Bridge) on which this MAC address is associated.


### 44.3 from column

This specifies whether this MAC address has been added by the hw-vtep controller
or dynamically learnt from the ASIC.


### 44.4 vlan column

VLAN associated with MAC address.


### 44.5 mac_addr column

MAC address.


### 44.6 tunnel_key column

If this MAC address is learnt from the tunnel port, then the tunnel_key will be
populated/configured. Otherwise, for static entries not having tunnel as port,
this column should not be populated.


### 44.7 expiry_time column

POSIX Time at which this MAC entry expires.


### 44.8 port column

Specifies the port [Port](Port) on which this MAC address is associated.


## 45. sFlow table

A set of sFlow(R) configurations.  sFlow is a protocol for remote monitoring of
switches.


### 45.1 sampling_per_speed column

The sampling rate can be configured per interface-speed (in Mbps) which means
the rate will be applied only for interfaces that match the speed. For example,
`sflow sampling 1024 1G` means a sampling rate of 1024 is applied to all the
1Gig interfaces on the system. If interface-speed is not specified, the global
rate is applied on the interface.


### 45.2 statistics column

Key value pairs that has sampling statistics.


### 45.3 name column

sFlow identifier for the configuration. Should be alphanumeric.


### 45.4 max_datagram column

Maximum number of bytes that will be send in the sflow datagram. If not
specified, the default is 1400 bytes.


### 45.5 agent column

Name of the network device whose IP address should be reported as the ``agent
address'' to collectors.  If not specified, the agent IP is derived from the
first interface in alphabetical order.


### 45.6 sampling column

Specifies the rate at which packets should be sampled and sent to the collector.
If not specified, rate defaults to 4096, which means one out of 4096 packets, on
average, will be sent to the collector.


### 45.7 header column

Number of bytes of a sampled packet to send to the collector. If not specified,
the default is 128 bytes.


### 45.8 agent_addr_family column

Address type of agent address reported. If agent interface has both IPv4 and
IPv6 address configured, then this column selects which address will be used.
Defaults to IPv4.


### 45.9 polling column

Specifies the interval at which counter statistics are send to the collector. If
not specified, interval defaults to 30 seconds


### 45.10 external_ids column



### 45.11 targets column

sFlow collectors in the form `_ip_:_port_`. Port defaults to 6343 if not
specified. Can have multiple collectors. Atleast one target has to be configured
for sflow to be enabled. Collectors can only be reached over vrf_default.


## 46. QoS_DSCP_Map_Entry table

Contains DSCP map entries used by QoS Trust Mode. It associates each code point
to local_priority (required), and (optionally), priority code point, color and
description.


### 46.1 description column

Used for customer documentation.


### 46.2 color column

It may be used later in the pipeline in packet-drop decision points. The default
is 'green'.


### 46.3 code_point column

The identifier for an entry in the DSCP map that represents the Differentiated
Services Code Point (DSCP) value for this entry.


### 46.4 other_config column



### 46.5 priority_code_point column

The 802.1Q priority that will be assigned to the packet. If the packet is
transmitted with a VLAN tag, this value will be in the Priority Code Point
field. If this value is not specified, the default behavior is that the priority
of the packet will not be changed.


### 46.6 local_priority column

This is a switch internal meta-data value that will be associated with the
packet. This value will be used later to select the egress queue for the packet.


### 46.7 hw_defaults column



### 46.8 external_ids column



## 47. QoS_COS_Map_Entry table

Contains COS map entries used by QoS Trust Mode. It associates each priority to
local_priority (required), and (optionally), color and description.


### 47.1 description column

Used for customer documentation.


### 47.2 color column

It may be used later in the pipeline in packet-drop decision points. The default
is 'green'.


### 47.3 code_point column

The identifier for an entry in the COS map that is the 802.1Q priority code
point for this entry.


### 47.4 other_config column



### 47.5 local_priority column

This is a switch internal meta-data value that will be associated with the
packet. This value will be used later to select the egress queue for the packet.


### 47.6 hw_defaults column



### 47.7 external_ids column



## 48. Q_Profile table

Used to specify named profiles of queue configuration. Ports use a queue profile
to configure their packet queue settings.


### 48.1 q_profile_entries column

Configuration parameters for individual queues.

Queues are numbered in *priority order*, with zero being the lowest priority.
The maximum number of queues is hardware dependent.


### 48.2 external_ids column



### 48.3 hw_default column

When true, this row contains the hardware default queue profile.

The default queue profile will be 8 queues when any of the following conditions
occur:

+No row in this table has hw_default true +More than one row in this table has
hw_default true +Any [Q_Profile_Entry](Q_Profile_Entry) rows referenced do not
have their hw_default true


### 48.4 name column

There must be a user-defined name of the schedule profile.


### 48.5 other_config column



## 49. Q_Profile_Entry table

Contains configuration parameters for one queue of one profile.


### 49.1 local_priorities column

This essential parameter specifies one or more local-priority(s) that are
assigned to this queue.  Packets' local-priority meta-data is initially assigned
by the port's QoS Trust Mode  (see [Port](Port) qos_config).  If missing, the
queue is not used.


### 49.2 external_ids column



### 49.3 hw_default column

When true, this row contains the hardware default queue profile parameters for
this queue.


### 49.4 description column

Used for documentation of these queue configuration parameters.


### 49.5 other_config column



## 50. QoS table

Used to specify named profiles of scheduling configuration. Ports use a schedule
profile to configure their packet queue servicing behavior.


### 50.1 external_ids column



### 50.2 hw_default column

When true, this row signifies the hardware default schedule profile.

Default schedule profile is "Strict Priority" when any of the following occur:

+No row in this table has hw_default true +More than one row in this table has
hw_default true +Any [Queue](Queue) rows referenced do not have their hw_default
true


### 50.3 queues column

Schedule parameters for individual queues.

Queues are numbered in *priority order*, with zero being the lowest priority.
The maximum number of queues is hardware dependent.


### 50.4 other_config column



### 50.5 name column

There must be a user-defined name of the schedule profile.


## 51. Queue table

Contains scheduling parameters for one queue of one profile.


### 51.1 external_ids column



### 51.2 hw_default column

When true, this row contains the hardware default schedule profile parameters
for this queue.


### 51.3 algorithm column

This parameter selects the scheduling behavior of the queue:

`strict` - Strict Priority will service all packets in the queue before any
packets in lower numbered queues as long as there are no packets in any higher
number queue.

`dwrr` - Deficit Weight Round Robin will apportion available bandwidth amongst
all non-empty dwrr queues in relation to their queue weights.

If this parameter is missing, it is assumed to be 'strict'.


### 51.4 weight column

The weight value for this queue. The maximum weight is hardware dependent.


### 51.5 other_config column



## 52. NTP_Association table

NTP Client Configuration info related to configured NTP servers and their status
info.`https://www.ietf.org/rfc/rfc5907.txt`


### 52.1 key_id column

Key id is used if NTP client wants to connect to an authenticated association.
Key id is not used when using an unauthenticated association.


### 52.2 address column

FQDN or ip address for the association.


### 52.3 association_status column

Key-value pairs that report NTP association status.


### 52.4 association_attributes column



### 52.5 vrf column

Specifies which VRF this association should connect with.


## 53. NTP_Key table

NTP Keys configuration


### 53.1 key_id column

Specifies a key_id which is used for NTP authentication.


### 53.2 trust_enable column

Enables trust settings for this key_id. Default is false.


### 53.3 key_password column

Specifies a key_password which is used for NTP authentication.


## 54. OSPF_Router table



### 54.1 router_id column



### 54.2 distance column



### 54.3 redistribute column

Redistributes the different types of routes into OSPFv2 network.


### 54.4 default_information column

The configurations related to the default routes advertisement. The router
should originate an AS-External (type-5) LSA describing a default route into the
Autonomus Sytem's all external-routing capable areas.


### 54.5 spf_calculation column



### 54.6 stub_router_adv column



### 54.7 passive_interface_default column

This determines whether all interfaces should be set to passive by default. The
default value is false.


### 54.8 nbma_nbrs column

The list of all the "OSPF_NBMA_Neighbor" for the OSPFv2 router instance, which
contains the OSPFv2 configurations related to non-broadcast multi-access
networks.


### 54.9 other_config column



### 54.10 active_interfaces column

The list of the active-interfaces. If "passive_interface_default" is set
"false", then this list should be empty.


### 54.11 networks column

The list of all the IPv4 networks configured to run OSPFv2 protocol. The key is
the network prefix in A.B.C.D/M format.


### 54.12 status column



### 54.13 ext_ospf_routes column

The list of all the ospf external routes.


### 54.14 passive_interfaces column

The list of the passive-interfaces. If "passive_interface_default" is set
"true", then this list should be empty.


### 54.15 opaque_as_lsas column

The list of all the AS scope Opaque_LSAs.


### 54.16 areas column

The list of all the "OSPF_Area" for the OSPFv2 router instance, which contains
the OSPFv2 area related configurations.


### 54.17 as_ext_lsas column

The list of all the AS External LSAs.


### 54.18 lsa_timers column



## 55. OSPF_Area table

The configurations and other details of and OSPFv2 Area entity.


### 55.1 status column



### 55.2 intra_area_ospf_routes column

The list of all the OSPFv2 intra area routes.


### 55.3 statistics column



### 55.4 opaque_link_lsas column

The list of all the Link scope Opaque LSAs.


### 55.5 ospf_auth_type column

The type of OSPFv2 authentication. If not set, the OSPFv2 protocol packets
excahges are not authenticated.


### 55.6 network_lsas column

The list of all the Network LSAs.


### 55.7 ospf_area_summary_addresses column

The list of all OSPFv2 summary aAddresses for this OSPFv2 area. If area range
addresses are configured, then ABR may advertise summarized prefixes to other
areas.


### 55.8 inter_area_ospf_routes column

The list of all the OSPFv2 inter area routes.


### 55.9 ospf_interfaces column

The list of all the "OSPF_Interface" for the OSPFv2 Area, which contains the
OSPFv2 interface realted configurations, statuses, and statistics.


### 55.10 router_lsas column

The list of all the Router LSAs.


### 55.11 other_config column



### 55.12 abr_summary_lsas column

The list of all the Type 3 ABR Summary LSAs.


### 55.13 area_type column

This defines how the external routing and summary lsas for this area will be
handled. The default value is "default".


### 55.14 nssa_translator_role column

If value is set to "always", then NSSA ABR always translates NSSA External (type
5) LSAs to AS External (type 7) LSAs. If value is set to "never", then NSSA ABR
will not translate NSSA External (type 5) LSAs to AS External (type 7) LSAs. If
value is set to "candidate", then  this ABR router participates in the
translator election to determine if it will perform the translation duties. If
this NSSA router is not an ABR, then this option has no effect. The default
value is "candidate".


### 55.15 ospf_vlinks column

The list of all the "OSPF_Vlink" for the OSPFv2 Area, which contains the OSPFv2
Virtual link related configurations.


### 55.16 asbr_summary_lsas column

The list of all the Type 4 ASBR Summary LSAs.


### 55.17 opaque_area_lsas column

The list of all the Area scope Opaque LSAs.


### 55.18 prefix_lists column

The ABR filters the  Type-3 summary-LSAs to or from area using prefix lists.


### 55.19 as_nssa_lsas column

The list of all the Type 7 NSSA External LSAs.


### 55.20 router_ospf_routes column

The list of all the OSPFv2 routes to the routers.


## 56. OSPF_Summary_Address table



### 56.1 prefix column

The prefix address in A.B.C.D/M format.


### 56.2 other_config column



## 57. OSPF_Interface table



### 57.1 neighbors column

The list of all the OSPFv2 neighbors on this OSPFv2 Interface.


### 57.2 status column



### 57.3 statistics column



### 57.4 ospf_vlink column

The virtual link related configurations. This is valid for the interface of type
"virtual link".


### 57.5 ifsm_state column

OSPFv2 Interface FSM states. The default value is "depend_upon".


### 57.6 port column

The "Port" corresponding to the OSPFv2 Interface.


### 57.7 name column

The OSPFv2 Interface name.


## 58. OSPF_Neighbor table



### 58.1 status column



### 58.2 statistics column



### 58.3 nbr_priority column

The priority of the neighbor. The default value is 255.


### 58.4 nfsm_state column

OSPFv2 Neighbor FSM states. The default value is "down".


### 58.5 nbr_if_addr column

The interface address of the OSPFv2 Neighbor on which the neighbor relationship
is established. The default value is 0, which is invalid if_address.


### 58.6 nbr_options column

The neighbor options or capabilities such as Opaque LSA capability, Demand
Circuit, External Attribute LSA capability, and so on.


### 58.7 bdr column

The router ID of the Backup Designated Router, as reported by the neighbor. The
default value is 0.


### 58.8 nbma_nbr column

The NBMA Neighbor related configurations, and statuses. This is valid in case of
NBMA Neighbor only.


### 58.9 dr column

The router ID of the Designated Router, as reported by the neighbor. The default
value is 0.


### 58.10 nbr_router_id column

The Neighbor Router ID is used to identify the neighbor. The default value is 0,
which is invalid router_id.


## 59. OSPF_NBMA_Neighbor table



### 59.1 nbr_address column

The IP address of the NMBA neighbor. The default value is 0, which is invalid.


### 59.2 status column



### 59.3 interface_name column

The name of the interface on which the NBMA Neighbor is adjacent.


### 59.4 nbr_router_id column

The router ID of the neighbor. The default value is 0, which is invalid
router_id.


### 59.5 other_config column



## 60. OSPF_Vlink table



### 60.1 area_id column

The area ID of the virtual link. Backbone area cannot have virtual link.


### 60.2 name column

The virtual link identifier.


### 60.3 peer_router_id column

The peer router ID.


### 60.4 other_config column



### 60.5 ospf_auth_text_key column

The authentication key for OSPFv2 authentication type "text".


### 60.6 ospf_auth_type column

The type of OSPFv2 authentication. If not set, then the area level
authentication of the transit area, holds for the port.


### 60.7 ospf_auth_md5_keys column

The authentication keys for OSPFv2 authentication type "md5" message-digest.


## 61. OSPF_Route table



### 61.1 route_info column



### 61.2 path_type column

The value indicates whether the path type is inter-area, intra-area, or
external.


### 61.3 prefix column

Specifies the prefix address in A.B.C.D/M format.


### 61.4 paths column

The list of paths.


## 62. OSPF_LSA table



### 62.1 area_id column

The OSPFv2 Area ID. This is for area scope LSAs. The default value is 0.


### 62.2 ls_seq_num column

The sequence number of the OSPFv2 LSA.


### 62.3 lsa_data column

The OSPFv2 LSA specific data.


### 62.4 ls_birth_time column

The OSPFv2 LSA birth time, number of seconds elapsed since Epoch, which can be
used to compute LSA age.


### 62.5 num_router_links column

Total number of router links. This is applicable in case of Router LSA. The
default value is 0.


### 62.6 prefix column

The prefix in A.B.C.D/M format. This is applicable in case of the type 3 and 4
Summary LSAs.


### 62.7 lsa_type column

The type of the OSPFv2 LSA.


### 62.8 ls_id column

The OSPFv2 LS_ID.


### 62.9 chksum column

The checksum in the OSPFv2 LSA. The default value is 0.


### 62.10 length column

The length of the OSPFv2 LSA in bytes. The default value is 20 bytes.


### 62.11 adv_router column

The Router ID of the advertising router.


### 62.12 options column

The options in the OSPFv2 LSA.


### 62.13 flags column

The flags in the OSPFv2 Router LSA.


## 63. DHCP_Relay table

Placeholder for a set of server configuration entries. DHCP-Relay feature uses
these entries to forward matching DHCP broadcast packets received on the layer3
Port.


### 63.1 ipv6_mcast_server column

List of IPv6 multicast or link local server destinations to which matching DHCP
broadcast packets received on the port are duplciated and forwarded. Value of
this key referenes a Port table entry, packets matching the criteria are
forwarded to the server through this port. A maximum of 8 IPv6 server
configurations are allowed. This count includes IPv6 unicast server
configurations from the column "ipv6_ucast_server".


### 63.2 other_config column



### 63.3 ipv6_ucast_server column

List of IPv6 unicast server destinations to which DHCP broadcast packets
received on the port are dulicated and forwarded. A maximum of 8 IPv6 server
configurations are allowed. The count includes IPv6 multicast and link local
server configuration from the column "ipv6_mcast_server".


### 63.4 vrf column

VRF through which DHCP server is reachable.


### 63.5 ipv4_ucast_server column

List of IPv4 unicast server destinations to which DHCP broadcast packets
received on the port are duplicated and forwarded. A maximum of 8 ipv4 unicast
server configurations are allowed.


### 63.6 port column

Layer 3 Port on which the configuration is made.


## 64. Mirror table

Mirror sessions referenced from a [Bridge](Bridge).

A mirror configures a bridge to send copies of selected packets to special
"mirrored" ports, in addition to their normal destinations. Mirroring traffic
may also be referred to as SPAN.


### 64.1 select_src_port column

Set of Ethernet port or LAG references in [Port](Port) on which received packets
are selected to be mirrored.


### 64.2 output_port column

Ethernet port or LAG reference in [Port](Port) used to transmit the mirror
packets.  There must be a valid Ethernet port or LAG for the session operation
state to become active.

The output port should be reserved exclusively for transmitting mirror packets
for this session.  It should not pariticapte in any other network activity (e.g.
Spanning Tree, LLDP etc).


### 64.3 statistics column



### 64.4 name column

There must be a user-defined name of the mirror session.


### 64.5 mirror_status column

Key-value pair(s) that report mirror status in hardware.


### 64.6 other_config column



### 64.7 select_dst_port column

Set of Ethernet port or LAG references in [Port](Port) on which transmitted
packets are selected to be mirrored.


### 64.8 active column

The intended state of the mirror session: active or inactive. The
[operation_state](Mirror.mirror_status.operation_state) value contains the actual state
in hardware (e.g. active, inactive, or error). When missing or false, the state
is inactive.


### 64.9 external_ids column



## 65. UDP_Bcast_Forwarder_Server table

Each entry represents the match and forward criteria for UDP broadcast packets
received on the port. UDP-Broadcast-Forwarder feature uses these entries to
forward selective UDP broadcast packets received on the routed Port to the
configured server(s).


### 65.1 udp_dport column

UDP broadcast packets with this destination udp port are forwarded to the
configured server(s).


### 65.2 dest_vrf column

VRF through which server is reachable.


### 65.3 src_port column

Reference to the routed port on which packets are receive.


### 65.4 ipv4_ucast_server column

List of IPv4 unicast server destinations to which matching UDP broadcast packets
received on the port are duplicated and forwarded.


## 66. Package_Info table

Each entry contains metadata related to package which is part of the image


### 66.1 src_type column

Corresponds to the type of source pointed to by src_url. Depending on the
src_url, some of the values it can take are - git, https, http, ftp, svn, cvs
etc.


### 66.2 src_url column

This denotes the download location for the source-code of the package. For
example: ops-openvswitch: https://git.openswitch.net/openswitch/ops-openvswitch
sed: http://ftp.gnu.org/gnu/sed/sed-4.2.2.tar.gz


### 66.3 name column

Name of the package. Example: ops-openvswitch, sed, ops-quagga, openssh etc.


### 66.4 version column

If the src_type is a git repository, this will contain the git hash. Otherwise
it will contain the version string (depending on the package). For example: ops-
openvswitch: ac19ac49778adf6cf011a3ef6e0675025f1945b5 sed: 4.2.2


## 67. Syslog_Remote table

Each entry contains the configuration of the remote syslog server to forward
syslog messages.


### 67.1 remote_host column

FQDN or host name or IPv4 address or IPv6 address of the syslog server.


### 67.2 port_number column

Port number on which syslog server is listening. Default is `514` for UDP
protocol and `1470` for TCP protocol.


### 67.3 severity column

Filter syslog messages with severity.  Only messages with severity higher than
or equal to the specified value will be sent to the remote server. Default is
`debug`.


### 67.4 transport column

Transport layer protocol used to forward messages to the server. Default is
`udp`


## 68. SNMP_Trap table



### 68.1 community_name column

SNMPv1/SNMPv2c community strings. The default community string is "public".


### 68.2 receiver_address column

The IP address of the trap receiver.


### 68.3 version column

Trap/inform version. The default version is "v2c".


### 68.4 type column

Trap type. The default type is "trap".


### 68.5 receiver_udp_port column

The UDP port of the trap receiver.


## 69. SNMPv3_User table



### 69.1 auth_protocol column

The authentication protocol to be used for authenticating the user. The default
is "none".


### 69.2 auth_pass_phrase column

The key to be used by authentication protocol.


### 69.3 priv_protocol column

The privacy protocol to be used for encrypting the user requests. The default is
"none".


### 69.4 user_name column

User name that should contain alphanumeric characters.


### 69.5 priv_pass_phrase column

The key to be used by privacy protocol.


## 70. ACL table



### 70.1 in_progress_aces column

The in flight version of the Access Control List.  Access Control Entries (ACE)
specified in this ACL are defined in [ACL_Entry](ACL_Entry)


### 70.2 status column



### 70.3 other_config column



### 70.4 name column

Name of an Access Control List (ACL).


### 70.5 in_progress_version column

The version of the 'in_progress' Access Control List.  This value is copied from
the cfg_version column when the ACL processing begins. This value is cleared
when the ACL status is updated to 'applied' or 'rejected.'


### 70.6 cfg_version column

The version of the 'cfg_aces' column. This value is incremented by the
management interface - CLI/REST/Web UI, etc. every time it changes the
'cfg_aces' value.


### 70.7 list_type column

Type of an Access Control List  Accepted values: 'ipv4'


### 70.8 cur_aces column

The currently configured version of the Access Control List.  Access Control
Entries (ACE) specified in this version of the ACL are defined in
[ACL_Entry](ACL_Entry)


### 70.9 external_ids column



### 70.10 cfg_aces column

The desired version of the Access Control List.  Access Control Entries (ACE)
specified in this version of the ACL are defined in [ACL_Entry](ACL_Entry)


## 71. ACL_Entry table



### 71.1 comment column

Comment to associate with the specified ACE. Optional parameter.


### 71.2 count column

Count Action: enable hit counts in hardware for packets that match this ACL
entry Optional parameter for IPv4 ACL entries The following value is accepted:
true


### 71.3 protocol column

IPv4 Protocol Optional parameter.  If no protocol is specified the ACE will not
match on protocol.


### 71.4 log column

Log Action: enable ACL logging for packets that match this ACL entry Optional
parameter for IPv4 ACL entries The following value is accepted: true


### 71.5 src_l4_port_range_reverse column

Specifies if the values in src_l4_port_min and src_l4_port_max should be treated
as specifying values not to be matched. Optional parameter for IPv4 ACL entries.
Applicable to TCP and UDP protocols.


### 71.6 other_config column



### 71.7 src_ip column

Source IPv4 Address: Optional parameter.  If no IP address is specified the ACE
will not match on source IP address.  The following IPv4 address formats are
accepted: X.X.X.X/X.X.X.X


### 71.8 dst_l4_port_max column

Destination L4 Port Max: specifies the maximum value It is used in conjunction
with dst_l4_port_min and dst_l4_port_range_reverse to determine the desired
destination L4 port functionality.  Optional parameter for IPv4 ACL entries.


### 71.9 src_l4_port_max column

Source L4 Port Max: specifies the maximum value It is used in conjunction with
src_l4_port_min and src_l4_port_range_reverse to determine the desired source L4
port functionality.  Optional parameter for IPv4 ACL entries.


### 71.10 action column

Match Action: Optional parameter for IPv4 ACL entries. There are two types:
"permit" and "deny" If no action is specified the ACE will not be programmed in
hw.


### 71.11 dst_ip column

Destination IPv4 Address: Optional parameter.  If no IP address is specified the
ACE will not match on destination IP address  The following IPv4 address formats
are accepted: X.X.X.X/X.X.X.X


### 71.12 dst_l4_port_range_reverse column

Specifies if the values in dst_l4_port_min and dst_l4_port_max should be treated
as specifying values not to be matched. Optional parameter for IPv4 ACL entries.
Applicable to TCP and UDP protocols.


### 71.13 src_l4_port_min column

Source L4 Port: specifies the IPv4 L4 source port to be used as the minimum
value.  It is used in conjunction with src_l4_port_max and
src_l4_port_range_reverse to determine the desired source L4 port functionality.
Optional parameter for IPv4 ACL entries.


### 71.14 dst_l4_port_min column

Source L4 Port: specifies the IPv4 L4 source port to be used as the minimum
value.  It is used in conjunction with dst_l4_port_max and
dst_l4_port_range_reverse to determine the desired destination L4 port
functionality.  Optional parameter for IPv4 ACL entries.


### 71.15 external_ids column



## 72. Notification_Subscriber table



### 72.1 notification_subscriptions column

List of notification subscriptions by name for this subscriber.


### 72.2 type column

Notification transport type. For WebSockets the type is "ws".


### 72.3 name column

Name of the notification subscriber.


## 73. Notification_Subscription table



### 73.1 resource column

URI of the resource being subscribed to for notifications.
