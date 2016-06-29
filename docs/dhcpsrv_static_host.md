# DHCPSrv_Static_Host

![DHCPSrv_Static_Host_table_img](http://www.plantuml.com/plantuml/img/0Uq04lz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo14I4DGNrDbSdPbSWfZR65pSo14I4DGKt9sNrDqONHfOrz8RtDq2dqAH4X3K5DoTbzJT65qQMDVI6zpT20yBNKj84H8Gr1VKsLoTcLo2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Static leases configured by the user.

## 1. Ungrouped group

### 1.1 set_tags column

Specifies the list of tags associated with the DHCP request. When a DHCP request
from the specific DHCP client is received, the list of configured tags would be
set and used to selectively send DHCP options for the client.

### 1.2 client_hostname column

Specifies the client hostname of the DHCP client to which the configured static
IP address would be assigned.

### 1.3 mac_addresses column

Specifies the list of MAC addresses of the DHCP hosts to which the static IP
address would be assigned. If more than one MAC addresses are specified, it
would work reliably only if one MAC address is active at a time.

### 1.4 lease_duration column

Specifies the lease expiry time in minutes. If not specified, default value of
one hour (60) would be used.

### 1.5 client_id column

Specifies the client id of the DHCP client to which the configured static IP
address would be assigned,

### 1.6 ip_address column

Specifies the static IP address that should be assigned to the specific
host.This ip address may contain an IPv4 address or an IPv6 address, or both.

