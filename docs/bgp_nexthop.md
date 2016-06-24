# BGP_Nexthop

![BGP_Nexthop_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuIf8JCvEJ4zLK0hApozH24bCoaajLbAevb80WkISnE9Y1IVtWFYW_DAIL0KR6mMD49sSpFICalIYrDGyJGKxEwvQBYw4Eh_KYfAC_0BiAhaG9kdgsY6hv-9oICrB0Ja7)

List of all nexthops used by BGP. Each entry in the BGP RIB can have a reference
to one or many (for ECMP) nexthop entries.

## 1. Status group

### 1.1 ip_address column

IP address of the nexthop device.

### 1.2 type column

Type of the nexthop. Default is `unicast`.

