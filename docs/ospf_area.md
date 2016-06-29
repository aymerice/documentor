# OSPF_Area

![OSPF_Area_table_img](http://www.plantuml.com/plantuml/img/0Oe1TVv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16NrDrRMrXSdbVGMHaScLpSmfZR65pSo1FKr16Nr9lTNHb2cDiONDp84zJK4PVGN9bOGfZR65pSo1FKr16NqbkT6LoPc5ZPGfZR65pSo1FKr16NqnJGGfz2azJK4PVGN9bOI0jP2q-84zJK4PVIMvqPN9cOMDb2azJK4PVGN9bOI0jP2q-84zJK4PVJ5D12azJK4PVGN9bOI0jP2q-84zJK4PVKtLjRM5oULz1P6HoPNDp2azJK4PVGN9bOI0jP2q-84zJK4PVKczrT6KAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

The configurations and other details of and OSPFv2 Area entity.

## 1. status

### 1.1 status

**Type**: _string->string_

### 1.2 status : transit_capability

**Type**: _string_

This describes the transit capability for virtual links. The default value is
false.

### 1.3 status : asbr_summary_lsas_sum_cksum

**Type**: _integer_

The sum of checksums of list of Type 4 ASBR Summary LSAs. The default value is
0.

### 1.4 status : NSSA translator role

**Type**: _string_

This describes the NSSA translator state. The default value is disable.

### 1.5 status : full_virtual_nbrs

**Type**: _integer_

This describes the number of adjacent virtual neighbors. The default value is 0.

### 1.6 status : stub_router_admin_set

**Type**: _boolean_

This describes the status of the stub_router if it is set administratively. The
default value is false.

### 1.7 status : spf_last_run_timestamp

**Type**: _string_

This describes the time when the last time SPF algorithm had run for this area.

### 1.8 status : opaque_link_lsas_sum_cksum

**Type**: _integer_

The sum of checksums of list of Link scope Opaque LSAs. The default value is 0.

### 1.9 status : stub_router_startup

**Type**: _boolean_

This describes the status of the stub_router if it is set "startup". The default
value is false.

### 1.10 status : router_lsas_sum_cksum

**Type**: _integer_

The sum of checksums of list of Router LSAs. The default value is 0.

### 1.11 status : stub_router_state_active

**Type**: _boolean_

This describes the status of the stub_router. The default value is false.

### 1.12 status : abr_summary_lsas_sum_cksum

**Type**: _integer_

The sum of checksums of list of Type 3 ABR Summary LSAs. The default value is 0.

### 1.13 status : full_nbrs

**Type**: _integer_

This describes the the number of adjacent neighbors in the area. The default
value is 0.

### 1.14 status : opaque_area_lsas_sum_cksum

**Type**: _integer_

The sum of checksums of list of  Area scope Opaque LSAs. The default value is 0.

### 1.15 status : network_lsas_sum_cksum

**Type**: _integer_

The sum of checksums of list of Network LSAs. The default value is 0.

### 1.16 status : active_interfaces

**Type**: _integer_

This describes the number of active OSPFv2 interfaces in the area. The default
value is 0.

### 1.17 status : as_nssa_lsas_sum_cksum

**Type**: _integer_

The sum of checksums of list of Type 7 NSSA External LSAs. The default value is
0.

### 1.18 intra_area_ospf_routes

**Type**: _uuid_ **refTable**: [OSPF_Route](ospf_route.html) **refType**: _strong_



The list of all the OSPFv2 intra area routes.

### 1.19 opaque_link_lsas

**Type**: _uuid_ **refTable**: [OSPF_LSA](ospf_lsa.html) **refType**: _strong_



The list of all the Link scope Opaque LSAs.

### 1.20 network_lsas

**Type**: _uuid_ **refTable**: [OSPF_LSA](ospf_lsa.html) **refType**: _strong_



The list of all the Network LSAs.

### 1.21 inter_area_ospf_routes

**Type**: _uuid_ **refTable**: [OSPF_Route](ospf_route.html) **refType**: _strong_



The list of all the OSPFv2 inter area routes.

### 1.22 router_lsas

**Type**: _uuid_ **refTable**: [OSPF_LSA](ospf_lsa.html) **refType**: _strong_



The list of all the Router LSAs.

### 1.23 abr_summary_lsas

**Type**: _uuid_ **refTable**: [OSPF_LSA](ospf_lsa.html) **refType**: _strong_



The list of all the Type 3 ABR Summary LSAs.

### 1.24 asbr_summary_lsas

**Type**: _uuid_ **refTable**: [OSPF_LSA](ospf_lsa.html) **refType**: _strong_



The list of all the Type 4 ASBR Summary LSAs.

### 1.25 opaque_area_lsas

**Type**: _uuid_ **refTable**: [OSPF_LSA](ospf_lsa.html) **refType**: _strong_



The list of all the Area scope Opaque LSAs.

### 1.26 as_nssa_lsas

**Type**: _uuid_ **refTable**: [OSPF_LSA](ospf_lsa.html) **refType**: _strong_



The list of all the Type 7 NSSA External LSAs.

### 1.27 router_ospf_routes

**Type**: _uuid_ **refTable**: [OSPF_Route](ospf_route.html) **refType**: _strong_



The list of all the OSPFv2 routes to the routers.

## 2. statistics

### 2.1 statistics

**Type**: _string->integer_

### 2.2 statistics : abr_count

**Type**: _integer_

The number of Area Border Routers (ABR) in the area.

### 2.3 statistics : asbr_count

**Type**: _integer_

The number of autonomous system border routers (ASBR) in the area.

### 2.4 statistics : spf_calc

**Type**: _integer_

The number of times the SPF calculations has run.

## 3. Configuration

### 3.1 ospf_auth_type

**Type**: _string_

The type of OSPFv2 authentication. If not set, the OSPFv2 protocol packets
excahges are not authenticated.

### 3.2 ospf_area_summary_addresses

**Type**: _uuid_ **refTable**: [OSPF_Summary_Address](ospf_summary_address.html) **refType**: _strong_



The list of all OSPFv2 summary aAddresses for this OSPFv2 area. If area range
addresses are configured, then ABR may advertise summarized prefixes to other
areas.

### 3.3 ospf_interfaces

**Type**: _uuid_ **refTable**: [OSPF_Interface](ospf_interface.html) **refType**: _strong_



The list of all the "OSPF_Interface" for the OSPFv2 Area, which contains the
OSPFv2 interface realted configurations, statuses, and statistics.

### 3.4 area_type

**Type**: _string_

This defines how the external routing and summary lsas for this area will be
handled. The default value is "default".

### 3.5 nssa_translator_role

**Type**: _string_

If value is set to "always", then NSSA ABR always translates NSSA External (type
5) LSAs to AS External (type 7) LSAs. If value is set to "never", then NSSA ABR
will not translate NSSA External (type 5) LSAs to AS External (type 7) LSAs. If
value is set to "candidate", then  this ABR router participates in the
translator election to determine if it will perform the translation duties. If
this NSSA router is not an ABR, then this option has no effect. The default
value is "candidate".

### 3.6 ospf_vlinks

**Type**: _integer->uuid_ **refTable**: [OSPF_Vlink](ospf_vlink.html) **refType**: _strong_



The list of all the "OSPF_Vlink" for the OSPFv2 Area, which contains the OSPFv2
Virtual link related configurations.

### 3.7 prefix_lists

**Type**: _string->uuid_ **refTable**: [Prefix_List](prefix_list.html) **refType**: _strong_



The ABR filters the  Type-3 summary-LSAs to or from area using prefix lists.

## 4. Ungrouped

### 4.1 other_config

**Type**: _string->string_

### 4.2 other_config : stub_default_cost

**Type**: _integer_

The cost metric for the default summary route sent into the stub area. The
default value is 1.

