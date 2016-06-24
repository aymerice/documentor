# OSPF_Route

![OSPF_Route_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuKhEIImkLl0F3d2B3yelBKbLiB5Hq0ZHoSbCpoX9BqfDpTDKiBD3LkLOb9f8K17Og2Biof0LwEhQ8MdWGbY09k6GcfS2T2q0)

## 1. status group

### 1.1 route_info : area_id key

The area ID of the route.

### 1.2 route_info : ext_tag key

The tag of the route.

### 1.3 route_info : ext_type key

External Type 1 or Type 2 Route. For External routes only. The default value is
"ext_type_1".

### 1.4 route_info : area_type_abr key

The area type ABR. The default value is false.

### 1.5 route_info : cost key

The cost metric of the route. The default value is `16777215`, which is maximum
metric value.

### 1.6 route_info : type2_cost key

The External Type 2 route cost. The default value is `16777215`, which is
maximum metric value.

### 1.7 route_info : asbr_router_id key

The ASBR router ID. The default value is 0, which is invalid router ID.

### 1.8 route_info : area_type_asbr key

The area type ASBR. The default value is false.

### 1.9 path_type column

The value indicates whether the path type is inter-area, intra-area, or
external.

### 1.10 prefix column

Specifies the prefix address in A.B.C.D/M format.

### 1.11 paths column

The list of paths.

