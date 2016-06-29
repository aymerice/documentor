# DHCPSrv_Option

![DHCPSrv_Option_table_img](http://www.plantuml.com/plantuml/img/0UC07Fz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo14I4DGNrDbSdPbSWfZR65pSo14I4DGKt9sNqzmT6blRWfz2aH8Gr1JSdPVJt1qQMzk83mjTIqWH4X3K5zJPN9sPN8AQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Configuration to specify extra options (other than standard options) that would
be sent to the DHCP clients.

## 1. Ungrouped group

### 1.1 option_number column

Specifies the number of the extra option that should be sent to the DHCP
clients. The option number would be ignored if option name is specified.

### 1.2 option_name column

Specifies the name of the extra option that should be sent to the DHCP clients.

### 1.3 match_tags column

The option and option value specified in the configuration would be sent only if
the DHCP request from the client matches all the tags specified in this list.

### 1.4 option_value column

Specifies the value of the extra option that should be sent to the DHCP clients.

### 1.5 ipv6 column

Set this value to `true` if the configured option is for IPv6 and set to `false`
for IPv4 option. If not specifed, the configured option would be used for IPv4.

