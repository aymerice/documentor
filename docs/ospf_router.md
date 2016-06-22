# OSPF_Router

## 1. Configuration group

### 1.1 router_id : router_id_val key

The OSPFv2 router identifier. The router ID for the OSPFv2 instance. The router
ID may be an IPv4 address of the router. It can be any arbitrary 32bit number.
However it MUST be non-zero and unique within the entire Autonomus System
domain.

### 1.2 router_id : router_id_static key

This determines whether the router-ID is configured statically on this router
instance or not. The default is false.

### 1.3 distance : all key

The administrative distance applies to all types of routes if not configured
specifically for certain types. The default value is 110.

### 1.4 distance : inter_area key

The administrative distance applies to routes of type inter-area. The default is
110.

### 1.5 distance : external key

The administrative distance applies to routes of type external. The default is
110.

### 1.6 distance : intra_area key

The administrative distance applies to routes of type intra-area. The default is
110.

### 1.7 redistribute column

Redistributes the different types of routes into OSPFv2 network.

### 1.8 default_information column

The configurations related to the default routes advertisement. The router
should originate an AS-External (type-5) LSA describing a default route into the
Autonomus Sytem's all external-routing capable areas.

### 1.9 default_information : always key

The default route must be advertised always, even if the default route doesn't
exist in the local system or VRF RIB. The default value is false.

### 1.10 default_information : default_info_originate key

The router should advertise the default route into the Autonomus System. The
default value is false, that is, router should not advertise the default route.

### 1.11 spf_calculation : spf_holdtime key

The minimum hold time, in milliseconds, between the SPF calculation schedules.
The SPF hold time itself will be adaptive and increasing and bounded by max wait
time. The default value is 1000 milliseconds.

### 1.12 spf_calculation : spf_max_wait key

The the maximum wait time or hold time, in milliseconds, between the SPF
calculation schedules. The default value is 10000 milliseconds.

### 1.13 spf_calculation : spf_delay key

The initial delay time, in milliseconds, for SPF calculation schedule. The
default value is 200 milliseconds.

### 1.14 stub_router_adv : admin_set key

This determines whether the stub router router_lsa advertisement is set
administratively. The default value is false.

### 1.15 stub_router_adv : startup key

This determines whether the router should advertise stub router router_lsa on
start-up. The delay, in seconds, is the duration for how long, after the reboot,
stub router router_lsa should be advertised.

### 1.16 passive_interface_default column

This determines whether all interfaces should be set to passive by default. The
default value is false.

### 1.17 nbma_nbrs column

The list of all the "OSPF_NBMA_Neighbor" for the OSPFv2 router instance, which
contains the OSPFv2 configurations related to non-broadcast multi-access
networks.

### 1.18 other_config : log_adjacency_details key

This determines whether to log changes in adjacency in detail or not. If the
flag is not set then only changes to full or regressions are shown. The default
value is false.

### 1.19 other_config : default_metric key

The default cost metric for the redistributed routes. The default value is 20.

### 1.20 other_config : log_adjacency_changes key

This determines whether to log changes in adjacency or not. The default value is
false.

### 1.21 other_config : ospf_rfc1583_compatible key

This determines whether RFC1583 compatibility mode is enabled or not. If value
is false then the path preference algorithm is calculated as per RFC 2328. The
default value is false.

### 1.22 other_config : auto_cost_ref_bw key

1.The reference bandwidth, Mbits/second, for default cost calculations. This
bandwidth is considered equivalent to an OSPFv2 cost of
1. The allowed range is 1 to 4000000 Mbps, that is 1 Mbps to 4000 Gbps. The
default value is 40000 Mbps, that is 40 Gbps.

### 1.23 other_config : enable_ospf_opaque_lsa key

This  determines if the OSPFv2 Opaque LSA capability is enabled or not. The
default value is false.

### 1.24 active_interfaces column

The list of the active-interfaces. If "passive_interface_default" is set
"false", then this list should be empty.

### 1.25 networks column

The list of all the IPv4 networks configured to run OSPFv2 protocol. The key is
the network prefix in A.B.C.D/M format.

### 1.26 passive_interfaces column

The list of the passive-interfaces. If "passive_interface_default" is set
"true", then this list should be empty.

### 1.27 areas column

The list of all the "OSPF_Area" for the OSPFv2 router instance, which contains
the OSPFv2 area related configurations.

### 1.28 lsa_timers : lsa_arrival_interval key

The minimum interval, in milliseconds, between accepting the same LSA. The
default value is 1000 milliseconds.

### 1.29 lsa_timers : lsa_group_pacing key

The LSA group pacing timer. This is the interval, in seconds, between group of
LSA being refreshed or maxaged. The default value is 10 seconds.

## 2. Status group

### 2.1 status : asbr key

The Router is a OSPFv2 Autonomus System Boundary Router (ASBR). The default
value is false.

### 2.2 status : opaque_origination_blocked key

This describes if the Opaque LSA origination is blocked. The default value is
false.

### 2.3 status : spf_hold_multiplier key

This is current value of adaptive multiplier of the initial-holdtime and used in
determining the hold time. The default value is 1.

### 2.4 status : capability_restart key

This describes if the device has support for Graceful OSPFv2 Restart. The
default value is false.

### 2.5 status : as_ext_lsas_sum_cksum key

The sum of checksum of list of AS External LSAs. The default value is 0.

### 2.6 status : opaque_as_lsas_sum_cksum key

The sum of checksum of list of AS scope Opaque LSAs. The default value is 0.

### 2.7 status : capability_opaque key

This describes if the device has support for Opaque lsa capability. The default
value is true.

### 2.8 status : abr key

The Router is a OSPFv2 Area Border Router (ABR). The default value is false.

### 2.9 status : opaque_status key

This describes if the device has support for Opaque LSA enabled. The default
value is false.

### 2.10 status : stub_router_support key

This describes if the device has support for stub router advertisement as per
RFC 3137. The default value is true.

### 2.11 status : ospf_rfc1583_compatibility key

This describes if the device has support for rfc1583 compatibility. The default
value is true.

### 2.12 ext_ospf_routes column

The list of all the ospf external routes.

### 2.13 opaque_as_lsas column

The list of all the AS scope Opaque_LSAs.

### 2.14 as_ext_lsas column

The list of all the AS External LSAs.
