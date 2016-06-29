# OSPF_LSA

![OSPF_LSA_table_img](http://www.plantuml.com/plantuml/img/0Ha1vlv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16NqnJGGfZR65pSo1FKr16Nq5oPM4AOsnXStCWJrDGHbzIRtLqPN8AVGfFKr16NqnJGI0yBNKj84zJK4PVKczrT6Lo2azJK4PVJ5D183mjTIqWJrDGHbz1ScLX2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

## 1. status

### 1.1 area_id

**Type**: _integer_

The OSPFv2 Area ID. This is for area scope LSAs. The default value is 0.

### 1.2 ls_seq_num

**Type**: _integer_

The sequence number of the OSPFv2 LSA.

### 1.3 lsa_data

**Type**: _string_

The OSPFv2 LSA specific data.

### 1.4 ls_birth_time

**Type**: _integer_

The OSPFv2 LSA birth time, number of seconds elapsed since Epoch, which can be
used to compute LSA age.

### 1.5 num_router_links

**Type**: _integer_

Total number of router links. This is applicable in case of Router LSA. The
default value is 0.

### 1.6 prefix

**Type**: _string_

The prefix in A.B.C.D/M format. This is applicable in case of the type 3 and 4
Summary LSAs.

### 1.7 lsa_type

**Type**: _string_

The type of the OSPFv2 LSA.

### 1.8 ls_id

**Type**: _integer_

The OSPFv2 LS_ID.

### 1.9 chksum

**Type**: _integer_

The checksum in the OSPFv2 LSA. The default value is 0.

### 1.10 length

**Type**: _integer_

The length of the OSPFv2 LSA in bytes. The default value is 20 bytes.

### 1.11 adv_router

**Type**: _integer_

The Router ID of the advertising router.

### 1.12 options

**Type**: _string_

The options in the OSPFv2 LSA.

### 1.13 flags

**Type**: _string_

The flags in the OSPFv2 Router LSA.

