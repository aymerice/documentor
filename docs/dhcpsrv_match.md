# DHCPSrv_Match

![DHCPSrv_Match_table_img](http://www.plantuml.com/plantuml/img/0Vi01Fz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo14I4DGNrDbSdPbSWfZR65pSo14I4DGKt9sNqrXT6De2dqAH4X3K5DoTbzDONHZQ20yBNKj84H8Gr1VKsLoTcLo2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Configuration to set tags for the incoming DHCP requests based on the options
and its value sent by the clients.

## 1. Ungrouped

### 1.1 option_number

**Type**: _integer_

Specifies the number of the extra option that should be sent by the client to
set the configured tag for DHCP requests. The option number would be ignored if
option name is specified.

### 1.2 option_name

**Type**: _string_

Specifies the name of the option that should be sent by the client to set the
configured tag for DHCP requests.

### 1.3 option_value

**Type**: _string_

Specifies the value of the option that should be sent by the client to set the
configured tag for DHCP requests. If the value is not specified, then the tag
would be set for any value of the option.

### 1.4 set_tag

**Type**: _string_

Specifies the name of the tag that would be set if the incoming DHCP request has
the configured option and the value.

