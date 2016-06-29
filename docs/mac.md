# MAC

![MAC_table_img](http://www.plantuml.com/plantuml/img/0H01x_v0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJK532dqAT6zdPNHePN8WUmfZR65pSo12ScbaPsKAOsnXStCWK6zoT0fz2ar1Go0kP2u-849oQMHdPGfDGKCWBcGkFY1GRt9q2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Configuration for consolidated MAC table which can potentially be learnt from
ASIC, from the hw-vtep controller or statically configured.

## 1. status

This column specifies the status of this entry in the table.

### 1.1 status

**Type**: _string->string_

### 1.2 status : no_memory

**Type**: _string_

Memory exhaustion

### 1.3 status : ok

**Type**: _string_

Properly configured

### 1.4 status : invalid

**Type**: _string_

Invalid parameters

### 1.5 status : error

**Type**: _string_

Unspecified error.

## 2. Ungrouped

### 2.1 bridge

**Type**: _uuid_ **refTable**: [Bridge](bridge.html) **refType**: _weak_



Specifies the bridge [Bridge](bridge.html) on which this MAC address is associated.

### 2.2 from

**Type**: _string_

This specifies whether this MAC address has been added by the hw-vtep controller
or dynamically learnt from the ASIC.

### 2.3 vlan

**Type**: _integer_

VLAN associated with MAC address.

### 2.4 mac_addr

**Type**: _string_

MAC address.

### 2.5 tunnel_key

**Type**: _integer_

If this MAC address is learnt from the tunnel port, then the tunnel_key will be
populated/configured. Otherwise, for static entries not having tunnel as port,
this column should not be populated.

### 2.6 expiry_time

**Type**: _integer_

POSIX Time at which this MAC entry expires.

### 2.7 port

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



Specifies the port [Port](port.html) on which this MAC address is associated.

