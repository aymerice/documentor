# Logical_Switch

![Logical_Switch_table_img](http://www.plantuml.com/plantuml/img/0Gq1ylv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJ6zdQMDXR5zJTsbqOsWAVGfqRsTbT6XbSY1x2cDiONDp849oQMHdPGfz2anlPsbZOMnVKtTfT6De82vaBZuWGd9fP6Tb2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Configuration for identifying overlay networks associated with bridges.

## 1. Ungrouped

### 1.1 tunnel_key

**Type**: _integer_

Tunnel key used in the overlay. For VXLAN, this is the VNI.

### 1.2 bridge

**Type**: _uuid_ **refTable**: [Bridge](bridge.html) **refType**: _weak_



Reference to a [Bridge](bridge.html) participating in the overlay.

### 1.3 from

**Type**: _string_

The entity managing the overlay.

### 1.4 name

**Type**: _string_

Name of the overlay network.

### 1.5 description

**Type**: _string_

Description of the overlay network.

