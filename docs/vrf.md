# VRF

![VRF_table_img](http://www.plantuml.com/plantuml/img/XL9DJyCm3BtdLqGxWSJ-mLJjIni7cAgkS8sypEegidfotC64-E-qAe5gG9DJOZy_E-zvwWLOwgDJ9x0lKA0UPKIYSzWvz2FzhdHph0FlzUFYORRMauc-oUzSMHoaOCJgLYT93vIXhTcNPpGRV9C3dQ85L0l6GDkB5pp6K9iyDJFloPOW9LKn-DCoDNCBNioA-1LuZsoso6VaMENoVf6Q31rSeYDXazbHb76-RWZ_L-93zHeFpTZ1dhFLK3ebbh_pdSNZST9Ig9QclVUwgj_-NgDRTdLjHG3rb0kXxjlXDM1AWFne5I9Vwn6UtwA7m1IhVRFZ)

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

