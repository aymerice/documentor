# BGP_Nexthop

![BGP_Nexthop_table_img](http://www.plantuml.com/plantuml/img/0Gq1ylv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWGaTGNr9lTNHb2dqAT6zdPNHePN8WUmfZR65pSo12Hr1VJcLuT6XlS0fz2a97K5zEPNXqQ6zm83mjP2qWGaTGNr9lTNHb2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

List of all nexthops used by BGP. Each entry in the BGP RIB can have a reference
to one or many (for ECMP) nexthop entries.

## 1. Status

### 1.1 ip_address

**Type**: _string_

IP address of the nexthop device.

### 1.2 type

**Type**: _string_

Type of the nexthop. Default is `unicast`.

