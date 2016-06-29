# BGP_Router

![BGP_Router_table_img](http://www.plantuml.com/plantuml/img/0SS0EFz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo12Hr1VKczrT6Lo2dqAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. Configuration

BGP_router includes all bgp config related information. The entries are created
on per asn basis.

### 1.1 router_id

**Type**: _string_

Specifies the router-id for given ASN.

### 1.2 redistribute

**Type**: _string->uuid_ **refTable**: [Route_Map](route_map.html) **refType**: _strong_



Specifies which protocol routes should be redistributed into BGP. The routes can
be filtered by specifying the route-map.

### 1.3 deterministic_med

**Type**: _boolean_

When enabled, selects the best-MED path among paths advertised from the
neighboring AS. Default is false.

### 1.4 bgp_neighbors

**Type**: _string->uuid_ **refTable**: [BGP_Neighbor](bgp_neighbor.html) **refType**: _strong_



BGP neighbors or neighbor groups, keyed by IP for the former or any     string
name for the latter.

### 1.5 always_compare_med

**Type**: _boolean_

Compares MED (Multi-Exit Discriminitor) from different neighbors. Default is
false.

### 1.6 gr_stale_timer

**Type**: _integer_

Specifies the maximum time to hold onto restarting peer stale paths. Range:
1-3600 seconds. Default value is 360 seconds.

### 1.7 fast_external_failover

**Type**: _boolean_

Enables fast external failover for BGP directly connected peering sessions.
Default is false.

### 1.8 timers

**Type**: _string->integer_

### 1.9 timers : holdtime

**Type**: _integer_

Specifies BGP hold time in seconds. Default is 180 seconds.

### 1.10 timers : keepalive

**Type**: _integer_

Specifies BGP keepalive time in seconds. Default is 60 seconds.

### 1.11 log_neighbor_changes

**Type**: _boolean_

Enables logging of BGP neighbor status changes. Default is false.

### 1.12 networks

**Type**: _string_

Announces networks for given bgp router.

### 1.13 maximum_paths

**Type**: _integer_

Number of paths BGP may install into the routing table. If not specified, BGP
selects a single path. Default is 1.

## 2. Status

### 2.1 status

**Type**: _string->string_

## 3. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 3.1 other_config

**Type**: _string->string_

### 3.2 external_ids

**Type**: _string->string_

