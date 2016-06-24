# DHCP_Server

![DHCP_Server_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuKhEIImkLd3nS0u8BYgBzqqiISvGiB5Hq0ZHoSbCpoX9BqfDpTDKiBD3KnYKc9UUYazXM90R8NFYWrEBobABYB4kk2In93CvtYE_k8GOvVu59PdvUTXL8jkigsk7wYESik20mIcBv3oSQY1kuWA52qmOgepB8JKl1HWN)

DHCP Server configuration.

## 1. Configuration group

### 1.1 matches column

Matching incoming DHCP options.

### 1.2 static_hosts column

Static leases.

### 1.3 ranges column

Dynamic IP address ranges.

### 1.4 dhcp_options column

DHCP options settings.

### 1.5 BOOTP Options Configuration group

#### 1.5.1 bootp column

Key-value pairs that specifies BOOTP options for the DHCP clients.

#### 1.5.2 bootp : match tag key

The filename is keyed by match tag. If no key is specified, default key is
no_matching_tag.

