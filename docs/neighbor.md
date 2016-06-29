# Neighbor

![Neighbor_table_img](http://www.plantuml.com/plantuml/img/0Vy00Fz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJcLfPsXYRt8AVGfqRsTbT6XbSY1x2cDiONDp85PIHWfZR65pSo1GRt9q2dqAJcLfPsXYRt8WBcGkFY1GRt9q2avbQMTeOczo82raBJuWLb962cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

List of all the connected neighbors.

## 1. Neighbor information group

### 1.1 status column

### 1.2 status : dp_hit key

Indicates if there is active traffic to the neighbor. This value is periodically
updated. If the value is set to `false`, it indicates that there was no traffic
to this neighbor recently. Default is `true`

### 1.3 address_family column

Address family of the neighbor.

### 1.4 mac column

MAC address learned for this neighbor.

### 1.5 state column

Current state of the neighbor entry.

### 1.6 vrf column

Reference to the VRF table, to which this neighbor belongs.

### 1.7 ip_address column

The IPv4 address or the IPv6 address of neighbor

### 1.8 port column

Port on which this neighbor was learned.

