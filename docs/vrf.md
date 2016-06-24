# VRF

![VRF_table_img](http://www.plantuml.com/plantuml/img/XL9DRy8m3BtdLqISXZJ-0Qhu4kp0K5MwNICJh58H6XIxC3JjlwzHbwrYMvDJOZy_E-zvGWoEwvCHPz17A50ECcjPvh0pI0FvBcHpj04Y-JnVJrToF9OF-QCfYmCN3h4QoYJfW3BKjQFoWcg3RtomvsY1hHbZeEsD64ynr2PFrPJ8wXAuj5KC_h98rKm3iLfQTmMtHwUsw2xeOfMBftcgCZHmYuw4JMPdeuopLKFuln8VGdGwzmtPmbwpPLywjOx_pelMvD4eyHp2y_XxfwtuxV0zsjEBUpC2gADT2BKV3wyUMmBaHwqG-LgGyFoMFGJ41AkzN_DF)

Each entry in this table represents a single routing domain, commonly known as
Virtual Routing and Forwarding.

## 1. Status group

### 1.1 status : namespace_ready key

Indicates whether Linux namespace exists for this VRF. If not set, the assumed
value is false.

## 2. Configuration group

### 2.1 ospf_routers column

The list of all the OSPFv2 Router instances.

### 2.2 name column

VRF identifier. Should be alphanumeric. VRF names must be unique.

### 2.3 active_router_id column

Router-ID (in IPv4 format) that is currently used in the system, unless
overridden by protocol specific one.

### 2.4 ports column

Ports included in the VRF.

### 2.5 table_id column

Kernel table_id assigned for routing table of this VRF.

### 2.6 bgp_routers column

BGP routers keyed by ASN value.

### 2.7 dhcp_server column

DHCP Server in the VRF.

