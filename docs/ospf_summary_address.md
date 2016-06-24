# OSPF_Summary_Address

![OSPF_Summary_Address_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuKhEIImkLl0F3d2B3oxDpKqigentJ4afIWKAsjWeQ8Jev6IcPvIa5wMcvcagsDaXgtSiIat4hWWXhQjhXzLmBeVKl1IW_G00)

## 1. Configuration group

### 1.1 prefix column

The prefix address in A.B.C.D/M format.

### 1.2 other_config : advertise key

This determines whether to advertise the summary address or not. If value is
false then the OSPFv2 router does not advertise this summary address. The
default value is true.

### 1.3 other_config : cost key

The cost of the summary address. The default value is 16777214.

### 1.4 other_config : tag key

The tag for the summarized prefix.

