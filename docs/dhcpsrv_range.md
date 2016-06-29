# DHCPSrv_Range

![DHCPSrv_Range_table_img](http://www.plantuml.com/plantuml/img/0GG1-_v0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo14I4DGNrDbSdPbSWfZR65pSo1GRt9q2cDiONDp84H8Gr1JSdPVKc5kPsKAVGf4I4DGKt9sNr9XRcTb82vaBZuWK6zoT0f4I4DGKt9sNr9XRcTb83mjTIqWH4X3K5zJPN9sPN8AQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Dynamic IP address ranges configuration of the DHCP server.

## 1. Ungrouped group

### 1.1 is_static column

Set this value to `true` to assign static IP addresses to DHCP clients that have
static host configuration. If the value is set to `false`, then the IP addresses
in this range would be use for dynamic allocation. If not specifed, the IP
address range would be used for dynamic allocation.

### 1.2 name column

Identifier for DHCP Server IP address range configuration. This has to be unique
across all DHCP ranges and across all VRFs.

### 1.3 start_ip_address column

Specifies the start IPv4/IPv6 address of the dynamic IP address range.

### 1.4 set_tag column

Sets an alphanumeric label that marks the network so that dhcp options would be
specified on a per-network basis.

### 1.5 broadcast column

This is used only in IPv4 address ranges configuration. Specifies the broadcast
address that would be used for the assigned IP addresses in this range and this
would be sent to DHCP clients. If not specified, broadcast address of the switch
interface that received the DHCP request would be used.

### 1.6 netmask column

This is used only in IPv4 address ranges configuration. Specifies the netmask
that would be used for the assigned IP addresses in this range and this would be
sent to DHCP clients. If end ip address is not configured for this range, then
end ip address would be chosen based on the netmask. If netmask is not
specified, then netmask of the switch interface that received the DHCP request
would be used.

### 1.7 lease_duration column

Specifies the lease expiry time in minutes. If not specified, default value of
one hour (60) would be used.

### 1.8 constructor column

This is used only in IPv6 address ranges configuration. Specifies the interface
whose IP address would be used to calculate the end IP address for this range.
This is used when end ip address is not specified.

### 1.9 prefix_len column

This is used only in IPv6 address ranges configuration. Specifies the prefix
length that would be used for the assigned IPv6 addresses. If not specifed,
default value of 64 would be used.

### 1.10 match_tags column

Specifies the list of the tags that would be matched for the incoming DHCP
request on the interfaces whose IP addresses are in the configured range.

### 1.11 end_ip_address column

Specifies the end IPv4/IPv6 address of the dynamic IP address range. If not
specifed, then for IPv4 address family - end ip address would be calculated
based on the configured netmask for this range or based on the netmask of the
interface that received the DHCP request and for IPv6 family - end ip address
would be calculated based on the constructor template configuration.

