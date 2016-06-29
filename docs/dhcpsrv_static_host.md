# DHCPSrv_Static_Host

![DHCPSrv_Static_Host_table_img](http://www.plantuml.com/plantuml/img/0GS1-Fv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo14I4DGNrDbSdPbSWfZR65pSo14I4DGKt9sNrDqONHfOrz8RtDq2dqAH4X3K5DoTbzJT65qQMDVI6zpT20yBNKj84H8Gr1VKsLoTcLo2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Static leases configured by the user.

## 1. Ungrouped

### 1.1 set_tags

**Type**: _string_

Specifies the list of tags associated with the DHCP request. When a DHCP request
from the specific DHCP client is received, the list of configured tags would be
set and used to selectively send DHCP options for the client.

### 1.2 client_hostname

**Type**: _string_

Specifies the client hostname of the DHCP client to which the configured static
IP address would be assigned.

### 1.3 mac_addresses

**Type**: _string_

Specifies the list of MAC addresses of the DHCP hosts to which the static IP
address would be assigned. If more than one MAC addresses are specified, it
would work reliably only if one MAC address is active at a time.

### 1.4 lease_duration

**Type**: _integer_

Specifies the lease expiry time in minutes. If not specified, default value of
one hour (60) would be used.

### 1.5 client_id

**Type**: _string_

Specifies the client id of the DHCP client to which the configured static IP
address would be assigned,

### 1.6 ip_address

**Type**: _string_

Specifies the static IP address that should be assigned to the specific
host.This ip address may contain an IPv4 address or an IPv6 address, or both.

