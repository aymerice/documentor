# BGP_Router

![BGP_Router_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuKhEIImkLd1o3uWFoYyjIIrIiB5Hq0ZHoSbCpoX9BqfDpTDKiBFZSaZDIm6g1W00)

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

### 1.8 timers : holdtime key

Specifies BGP hold time in seconds. Default is 180 seconds.

### 1.9 timers : keepalive key

Specifies BGP keepalive time in seconds. Default is 60 seconds.

### 1.10 log_neighbor_changes column

Enables logging of BGP neighbor status changes. Default is false.

### 1.11 networks column

Announces networks for given bgp router.

### 1.12 maximum_paths column

Number of paths BGP may install into the routing table. If not specified, BGP
selects a single path. Default is 1.

