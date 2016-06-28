# BGP_Nexthop

![BGP_Nexthop_table_img](http://www.plantuml.com/plantuml/img/0VC03Fz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWGaTGNr9lTNHb2dqAT6zdPNHePN8WUmfZR65pSo12Hr1VJcLuT6XlS0fz2a97K5zEPNXqQ6zm83mjP2qWGaTGNr9lTNHb2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

List of all nexthops used by BGP. Each entry in the BGP RIB can have a reference
to one or many (for ECMP) nexthop entries.

## 1. Status group

### 1.1 ip_address column

IP address of the nexthop device.

### 1.2 type column

Type of the nexthop. Default is `unicast`.

