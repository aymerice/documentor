# OSPF_Router

![OSPF_Router_table_img](http://www.plantuml.com/plantuml/img/0Jy1mFv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16Nr9lTNHb2cDiONDp84zJK4PVJ5D12cDiONDp851lSdGAOsnXStCWJrDGHbzIRtLqPN8AVGfFKr16Nr9lTNHbSY0jP2q-84zJK4PVJ5D12azJK4PVKczrT6Lo82raBJuWJrDGHbzIRtLqPGfFKr16Nr9lTNHbSY0kP2u-851lSdGAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. Configuration

### 1.1 router_id

**Type**: _string->string_

### 1.2 router_id : router_id_val

**Type**: _integer_

The OSPFv2 router identifier. The router ID for the OSPFv2 instance. The router
ID may be an IPv4 address of the router. It can be any arbitrary 32bit number.
However it MUST be non-zero and unique within the entire Autonomus System
domain.

### 1.3 router_id : router_id_static

**Type**: _boolean_

This determines whether the router-ID is configured statically on this router
instance or not. The default is false.

### 1.4 distance

**Type**: _string->integer_

### 1.5 distance : all

**Type**: _integer_

The administrative distance applies to all types of routes if not configured
specifically for certain types. The default value is 110.

### 1.6 distance : inter_area

**Type**: _integer_

The administrative distance applies to routes of type inter-area. The default is
110.

### 1.7 distance : external

**Type**: _integer_

The administrative distance applies to routes of type external. The default is
110.

### 1.8 distance : intra_area

**Type**: _integer_

The administrative distance applies to routes of type intra-area. The default is
110.

### 1.9 redistribute

**Type**: _string_

Redistributes the different types of routes into OSPFv2 network.

### 1.10 default_information

**Type**: _string->string_

The configurations related to the default routes advertisement. The router
should originate an AS-External (type-5) LSA describing a default route into the
Autonomus Sytem's all external-routing capable areas.

### 1.11 default_information : always

**Type**: _boolean_

The default route must be advertised always, even if the default route doesn't
exist in the local system or VRF RIB. The default value is false.

### 1.12 default_information : default_info_originate

**Type**: _boolean_

The router should advertise the default route into the Autonomus System. The
default value is false, that is, router should not advertise the default route.

### 1.13 spf_calculation

**Type**: _string->integer_

### 1.14 spf_calculation : spf_holdtime

**Type**: _integer_

The minimum hold time, in milliseconds, between the SPF calculation schedules.
The SPF hold time itself will be adaptive and increasing and bounded by max wait
time. The default value is 1000 milliseconds.

### 1.15 spf_calculation : spf_max_wait

**Type**: _integer_

The the maximum wait time or hold time, in milliseconds, between the SPF
calculation schedules. The default value is 10000 milliseconds.

### 1.16 spf_calculation : spf_delay

**Type**: _integer_

The initial delay time, in milliseconds, for SPF calculation schedule. The
default value is 200 milliseconds.

### 1.17 stub_router_adv

**Type**: _string->string_

### 1.18 stub_router_adv : admin_set

**Type**: _boolean_

This determines whether the stub router router_lsa advertisement is set
administratively. The default value is false.

### 1.19 stub_router_adv : startup

**Type**: _integer_

This determines whether the router should advertise stub router router_lsa on
start-up. The delay, in seconds, is the duration for how long, after the reboot,
stub router router_lsa should be advertised.

### 1.20 passive_interface_default

**Type**: _boolean_

This determines whether all interfaces should be set to passive by default. The
default value is false.

### 1.21 nbma_nbrs

**Type**: _integer->uuid_ **refTable**: [OSPF_NBMA_Neighbor](ospf_nbma_neighbor.html) **refType**: _strong_



The list of all the "OSPF_NBMA_Neighbor" for the OSPFv2 router instance, which
contains the OSPFv2 configurations related to non-broadcast multi-access
networks.

### 1.22 other_config

**Type**: _string->string_

### 1.23 other_config : log_adjacency_details

**Type**: _boolean_

This determines whether to log changes in adjacency in detail or not. If the
flag is not set then only changes to full or regressions are shown. The default
value is false.

### 1.24 other_config : default_metric

**Type**: _integer_

The default cost metric for the redistributed routes. The default value is 20.

### 1.25 other_config : log_adjacency_changes

**Type**: _boolean_

This determines whether to log changes in adjacency or not. The default value is
false.

### 1.26 other_config : ospf_rfc1583_compatible

**Type**: _boolean_

This determines whether RFC1583 compatibility mode is enabled or not. If value
is false then the path preference algorithm is calculated as per RFC 2328. The
default value is false.

### 1.27 other_config : auto_cost_ref_bw

**Type**: _integer_

1.The reference bandwidth, Mbits/second, for default cost calculations. This
bandwidth is considered equivalent to an OSPFv2 cost of
1. The allowed range is 1 to 4000000 Mbps, that is 1 Mbps to 4000 Gbps. The
default value is 40000 Mbps, that is 40 Gbps.

### 1.28 other_config : enable_ospf_opaque_lsa

**Type**: _boolean_

This  determines if the OSPFv2 Opaque LSA capability is enabled or not. The
default value is false.

### 1.29 active_interfaces

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



The list of the active-interfaces. If "passive_interface_default" is set
"false", then this list should be empty.

### 1.30 networks

**Type**: _string->integer_

The list of all the IPv4 networks configured to run OSPFv2 protocol. The key is
the network prefix in A.B.C.D/M format.

### 1.31 passive_interfaces

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



The list of the passive-interfaces. If "passive_interface_default" is set
"true", then this list should be empty.

### 1.32 areas

**Type**: _integer->uuid_ **refTable**: [OSPF_Area](ospf_area.html) **refType**: _strong_



The list of all the "OSPF_Area" for the OSPFv2 router instance, which contains
the OSPFv2 area related configurations.

### 1.33 lsa_timers

**Type**: _string->integer_

### 1.34 lsa_timers : lsa_arrival_interval

**Type**: _integer_

The minimum interval, in milliseconds, between accepting the same LSA. The
default value is 1000 milliseconds.

### 1.35 lsa_timers : lsa_group_pacing

**Type**: _integer_

The LSA group pacing timer. This is the interval, in seconds, between group of
LSA being refreshed or maxaged. The default value is 10 seconds.

## 2. Status

### 2.1 status

**Type**: _string->string_

### 2.2 status : asbr

**Type**: _boolean_

The Router is a OSPFv2 Autonomus System Boundary Router (ASBR). The default
value is false.

### 2.3 status : opaque_origination_blocked

**Type**: _boolean_

This describes if the Opaque LSA origination is blocked. The default value is
false.

### 2.4 status : spf_hold_multiplier

**Type**: _integer_

This is current value of adaptive multiplier of the initial-holdtime and used in
determining the hold time. The default value is 1.

### 2.5 status : capability_restart

**Type**: _boolean_

This describes if the device has support for Graceful OSPFv2 Restart. The
default value is false.

### 2.6 status : as_ext_lsas_sum_cksum

**Type**: _integer_

The sum of checksum of list of AS External LSAs. The default value is 0.

### 2.7 status : opaque_as_lsas_sum_cksum

**Type**: _integer_

The sum of checksum of list of AS scope Opaque LSAs. The default value is 0.

### 2.8 status : capability_opaque

**Type**: _boolean_

This describes if the device has support for Opaque lsa capability. The default
value is true.

### 2.9 status : abr

**Type**: _boolean_

The Router is a OSPFv2 Area Border Router (ABR). The default value is false.

### 2.10 status : opaque_status

**Type**: _boolean_

This describes if the device has support for Opaque LSA enabled. The default
value is false.

### 2.11 status : stub_router_support

**Type**: _boolean_

This describes if the device has support for stub router advertisement as per
RFC 3137. The default value is true.

### 2.12 status : ospf_rfc1583_compatibility

**Type**: _boolean_

This describes if the device has support for rfc1583 compatibility. The default
value is true.

### 2.13 ext_ospf_routes

**Type**: _uuid_ **refTable**: [OSPF_Route](ospf_route.html) **refType**: _strong_



The list of all the ospf external routes.

### 2.14 opaque_as_lsas

**Type**: _uuid_ **refTable**: [OSPF_LSA](ospf_lsa.html) **refType**: _strong_



The list of all the AS scope Opaque_LSAs.

### 2.15 as_ext_lsas

**Type**: _uuid_ **refTable**: [OSPF_LSA](ospf_lsa.html) **refType**: _strong_



The list of all the AS External LSAs.

