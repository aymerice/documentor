# BGP_Router

![BGP_Router_table_img](http://www.plantuml.com/plantuml/img/0Qq0Klz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo12Hr1VKczrT6Lo2dqAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

## 1. Configuration group

BGP_router includes all bgp config related information. The entries are created
on per asn basis.

### 1.1 router_id column

Specifies the router-id for given ASN.

### 1.2 redistribute column

Specifies which protocol routes should be redistributed into BGP. The routes can
be filtered by specifying the route-map.

### 1.3 deterministic_med column

When enabled, selects the best-MED path among paths advertised from the
neighboring AS. Default is false.

### 1.4 bgp_neighbors column

BGP neighbors or neighbor groups, keyed by IP for the former or any     string
name for the latter.

### 1.5 always_compare_med column

Compares MED (Multi-Exit Discriminitor) from different neighbors. Default is
false.

### 1.6 gr_stale_timer column

Specifies the maximum time to hold onto restarting peer stale paths. Range:
1-3600 seconds. Default value is 360 seconds.

### 1.7 fast_external_failover column

Enables fast external failover for BGP directly connected peering sessions.
Default is false.

### 1.8 timers column

### 1.9 timers : holdtime key

Specifies BGP hold time in seconds. Default is 180 seconds.

### 1.10 timers : keepalive key

Specifies BGP keepalive time in seconds. Default is 60 seconds.

### 1.11 log_neighbor_changes column

Enables logging of BGP neighbor status changes. Default is false.

### 1.12 networks column

Announces networks for given bgp router.

### 1.13 maximum_paths column

Number of paths BGP may install into the routing table. If not specified, BGP
selects a single path. Default is 1.

## 2. Status group

### 2.1 status column

## 3. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 3.1 other_config column

### 3.2 external_ids column

