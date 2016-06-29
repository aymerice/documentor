# DHCPSrv_Range

![DHCPSrv_Range_table_img](http://www.plantuml.com/plantuml/img/0Hu1uVv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo14I4DGNrDbSdPbSWfZR65pSo1GRt9q2cDiONDp84H8Gr1JSdPVKc5kPsKAVGf4I4DGKt9sNr9XRcTb82vaBZuWK6zoT0f4I4DGKt9sNr9XRcTb83mjTIqWH4X3K5zJPN9sPN8AQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

Dynamic IP address ranges configuration of the DHCP server.

## 1. Ungrouped

### 1.1 is_static

**Type**: _boolean_

Set this value to `true` to assign static IP addresses to DHCP clients that have
static host configuration. If the value is set to `false`, then the IP addresses
in this range would be use for dynamic allocation. If not specifed, the IP
address range would be used for dynamic allocation.

### 1.2 name

**Type**: _string_

Identifier for DHCP Server IP address range configuration. This has to be unique
across all DHCP ranges and across all VRFs.

### 1.3 start_ip_address

**Type**: _string_

Specifies the start IPv4/IPv6 address of the dynamic IP address range.

### 1.4 set_tag

**Type**: _string_

Sets an alphanumeric label that marks the network so that dhcp options would be
specified on a per-network basis.

### 1.5 broadcast

**Type**: _string_

This is used only in IPv4 address ranges configuration. Specifies the broadcast
address that would be used for the assigned IP addresses in this range and this
would be sent to DHCP clients. If not specified, broadcast address of the switch
interface that received the DHCP request would be used.

### 1.6 netmask

**Type**: _string_

This is used only in IPv4 address ranges configuration. Specifies the netmask
that would be used for the assigned IP addresses in this range and this would be
sent to DHCP clients. If end ip address is not configured for this range, then
end ip address would be chosen based on the netmask. If netmask is not
specified, then netmask of the switch interface that received the DHCP request
would be used.

### 1.7 lease_duration

**Type**: _integer_

Specifies the lease expiry time in minutes. If not specified, default value of
one hour (60) would be used.

### 1.8 constructor

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



This is used only in IPv6 address ranges configuration. Specifies the interface
whose IP address would be used to calculate the end IP address for this range.
This is used when end ip address is not specified.

### 1.9 prefix_len

**Type**: _integer_

This is used only in IPv6 address ranges configuration. Specifies the prefix
length that would be used for the assigned IPv6 addresses. If not specifed,
default value of 64 would be used.

### 1.10 match_tags

**Type**: _string_

Specifies the list of the tags that would be matched for the incoming DHCP
request on the interfaces whose IP addresses are in the configured range.

### 1.11 end_ip_address

**Type**: _string_

Specifies the end IPv4/IPv6 address of the dynamic IP address range. If not
specifed, then for IPv4 address family - end ip address would be calculated
based on the configured netmask for this range or based on the netmask of the
interface that received the DHCP request and for IPv6 family - end ip address
would be calculated based on the constructor template configuration.

