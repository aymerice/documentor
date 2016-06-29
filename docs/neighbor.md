# Neighbor

![Neighbor_table_img](http://www.plantuml.com/plantuml/img/0Ha1vlv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJcLfPsXYRt8AVGfqRsTbT6XbSY1x2cDiONDp85PIHWfZR65pSo1GRt9q2dqAJcLfPsXYRt8WBcGkFY1GRt9q2avbQMTeOczo82raBJuWLb962cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

List of all the connected neighbors.

## 1. Neighbor information

### 1.1 status

**Type**: _string->string_

### 1.2 status : dp_hit

**Type**: _boolean_

Indicates if there is active traffic to the neighbor. This value is periodically
updated. If the value is set to `false`, it indicates that there was no traffic
to this neighbor recently. Default is `true`

### 1.3 address_family

**Type**: _string_

Address family of the neighbor.

### 1.4 mac

**Type**: _string_

MAC address learned for this neighbor.

### 1.5 state

**Type**: _string_

Current state of the neighbor entry.

### 1.6 vrf

**Type**: _uuid_ **refTable**: [VRF](vrf.html) **refType**: _strong_



Reference to the VRF table, to which this neighbor belongs.

### 1.7 ip_address

**Type**: _string_

The IPv4 address or the IPv6 address of neighbor

### 1.8 port

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



Port on which this neighbor was learned.

