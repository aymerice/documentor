# OSPF_Area

![OSPF_Area_table_img](http://www.plantuml.com/plantuml/img/0N01Z_v0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16NrDrRMrXSdbVGMHaScLpSmfZR65pSo1FKr16Nr9lTNHb2cDiONDp84zJK4PVGN9bOGfZR65pSo1FKr16NqbkT6LoPc5ZPGfZR65pSo1FKr16NqnJGGfz2azJK4PVGN9bOI0jP2q-84zJK4PVIMvqPN9cOMDb2azJK4PVGN9bOI0jP2q-84zJK4PVJ5D12azJK4PVGN9bOI0jP2q-84zJK4PVKtLjRM5oULz1P6HoPNDp2azJK4PVGN9bOI0jP2q-84zJK4PVKczrT6KAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

The configurations and other details of and OSPFv2 Area entity.

## 1. status group

### 1.1 status : transit_capability key

This describes the transit capability for virtual links. The default value is
false.

### 1.2 status : asbr_summary_lsas_sum_cksum key

The sum of checksums of list of Type 4 ASBR Summary LSAs. The default value is
0.

### 1.3 status : NSSA translator role key

This describes the NSSA translator state. The default value is disable.

### 1.4 status : full_virtual_nbrs key

This describes the number of adjacent virtual neighbors. The default value is 0.

### 1.5 status : stub_router_admin_set key

This describes the status of the stub_router if it is set administratively. The
default value is false.

### 1.6 status : spf_last_run_timestamp key

This describes the time when the last time SPF algorithm had run for this area.

### 1.7 status : opaque_link_lsas_sum_cksum key

The sum of checksums of list of Link scope Opaque LSAs. The default value is 0.

### 1.8 status : stub_router_startup key

This describes the status of the stub_router if it is set "startup". The default
value is false.

### 1.9 status : router_lsas_sum_cksum key

The sum of checksums of list of Router LSAs. The default value is 0.

### 1.10 status : stub_router_state_active key

This describes the status of the stub_router. The default value is false.

### 1.11 status : abr_summary_lsas_sum_cksum key

The sum of checksums of list of Type 3 ABR Summary LSAs. The default value is 0.

### 1.12 status : full_nbrs key

This describes the the number of adjacent neighbors in the area. The default
value is 0.

### 1.13 status : opaque_area_lsas_sum_cksum key

The sum of checksums of list of  Area scope Opaque LSAs. The default value is 0.

### 1.14 status : network_lsas_sum_cksum key

The sum of checksums of list of Network LSAs. The default value is 0.

### 1.15 status : active_interfaces key

This describes the number of active OSPFv2 interfaces in the area. The default
value is 0.

### 1.16 status : as_nssa_lsas_sum_cksum key

The sum of checksums of list of Type 7 NSSA External LSAs. The default value is
0.

### 1.17 intra_area_ospf_routes column

The list of all the OSPFv2 intra area routes.

### 1.18 opaque_link_lsas column

The list of all the Link scope Opaque LSAs.

### 1.19 network_lsas column

The list of all the Network LSAs.

### 1.20 inter_area_ospf_routes column

The list of all the OSPFv2 inter area routes.

### 1.21 router_lsas column

The list of all the Router LSAs.

### 1.22 abr_summary_lsas column

The list of all the Type 3 ABR Summary LSAs.

### 1.23 asbr_summary_lsas column

The list of all the Type 4 ASBR Summary LSAs.

### 1.24 opaque_area_lsas column

The list of all the Area scope Opaque LSAs.

### 1.25 as_nssa_lsas column

The list of all the Type 7 NSSA External LSAs.

### 1.26 router_ospf_routes column

The list of all the OSPFv2 routes to the routers.

## 2. statistics group

### 2.1 statistics : abr_count key

The number of Area Border Routers (ABR) in the area.

### 2.2 statistics : asbr_count key

The number of autonomous system border routers (ASBR) in the area.

### 2.3 statistics : spf_calc key

The number of times the SPF calculations has run.

## 3. Configuration group

### 3.1 ospf_auth_type column

The type of OSPFv2 authentication. If not set, the OSPFv2 protocol packets
excahges are not authenticated.

### 3.2 ospf_area_summary_addresses column

The list of all OSPFv2 summary aAddresses for this OSPFv2 area. If area range
addresses are configured, then ABR may advertise summarized prefixes to other
areas.

### 3.3 ospf_interfaces column

The list of all the "OSPF_Interface" for the OSPFv2 Area, which contains the
OSPFv2 interface realted configurations, statuses, and statistics.

### 3.4 area_type column

This defines how the external routing and summary lsas for this area will be
handled. The default value is "default".

### 3.5 nssa_translator_role column

If value is set to "always", then NSSA ABR always translates NSSA External (type
5) LSAs to AS External (type 7) LSAs. If value is set to "never", then NSSA ABR
will not translate NSSA External (type 5) LSAs to AS External (type 7) LSAs. If
value is set to "candidate", then  this ABR router participates in the
translator election to determine if it will perform the translation duties. If
this NSSA router is not an ABR, then this option has no effect. The default
value is "candidate".

### 3.6 ospf_vlinks column

The list of all the "OSPF_Vlink" for the OSPFv2 Area, which contains the OSPFv2
Virtual link related configurations.

### 3.7 prefix_lists column

The ABR filters the  Type-3 summary-LSAs to or from area using prefix lists.

