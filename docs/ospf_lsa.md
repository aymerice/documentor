# OSPF_LSA

![OSPF_LSA_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuKhEIImkLl0F3d2BzmbsLB2nKT08qSd9JCyeIIzAJStJLB2pGrRZM9IQI51HK7vfIMeHTcK8KtHrxU3sSY7hGv5mICrB0ReJ)

## 1. status group

### 1.1 area_id column

The OSPFv2 Area ID. This is for area scope LSAs. The default value is 0.

### 1.2 ls_seq_num column

The sequence number of the OSPFv2 LSA.

### 1.3 lsa_data column

The OSPFv2 LSA specific data.

### 1.4 ls_birth_time column

The OSPFv2 LSA birth time, number of seconds elapsed since Epoch, which can be
used to compute LSA age.

### 1.5 num_router_links column

Total number of router links. This is applicable in case of Router LSA. The
default value is 0.

### 1.6 prefix column

The prefix in A.B.C.D/M format. This is applicable in case of the type 3 and 4
Summary LSAs.

### 1.7 lsa_type column

The type of the OSPFv2 LSA.

### 1.8 ls_id column

The OSPFv2 LS_ID.

### 1.9 chksum column

The checksum in the OSPFv2 LSA. The default value is 0.

### 1.10 length column

The length of the OSPFv2 LSA in bytes. The default value is 20 bytes.

### 1.11 adv_router column

The Router ID of the advertising router.

### 1.12 options column

The options in the OSPFv2 LSA.

### 1.13 flags column

The flags in the OSPFv2 Router LSA.

