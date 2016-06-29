# DHCPSrv_Match

![DHCPSrv_Match_table_img](http://www.plantuml.com/plantuml/img/0U407lz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo14I4DGNrDbSdPbSWfZR65pSo14I4DGKt9sNqrXT6De2dqAH4X3K5DoTbzDONHZQ20yBNKj84H8Gr1VKsLoTcLo2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Configuration to set tags for the incoming DHCP requests based on the options
and its value sent by the clients.

## 1. Ungrouped group

### 1.1 option_number column

Specifies the number of the extra option that should be sent by the client to
set the configured tag for DHCP requests. The option number would be ignored if
option name is specified.

### 1.2 option_name column

Specifies the name of the option that should be sent by the client to set the
configured tag for DHCP requests.

### 1.3 option_value column

Specifies the value of the option that should be sent by the client to set the
configured tag for DHCP requests. If the value is not specified, then the tag
would be set for any value of the option.

### 1.4 set_tag column

Specifies the name of the tag that would be set if the incoming DHCP request has
the configured option and the value.

