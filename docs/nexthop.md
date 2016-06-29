# Nexthop

![Nexthop_table_img](http://www.plantuml.com/plantuml/img/0He1vVv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKczrT6KAVGfqRsTbT6XbSY1x2cDiONDp84vbU7HeRt0AOsnXStCWK6zoT0fz2avbU7HeRt0WBcGkFY1GRt9q2avbU7HeRt0WF2raBI1IRtLqPGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Global list of all the nexthops as used by the [Route](route.html) table. Each entry
in the [Route](route.html) can have a reference to one or many(for ECMP) entries in
this table.

## 1. Status

Status information to indicate the current state of the nexthop.

### 1.1 status

**Type**: _string->string_

### 1.2 status : arp_resolved

**Type**: _boolean_

Indicate if ARP is resolved for this entry. If the ARP entry is missing, this
value is `false`

### 1.3 status : error

**Type**: _string_

Human readable error string.

### 1.4 status : hw_configured

**Type**: _boolean_

Indicate if nexthop programmed in the asic. If the ARP entry is missing, this
value is `false`

## 2. Configuration

### 2.1 selected

**Type**: _boolean_

Indicates if this nexthop is actively participating in forwarding. Multiple
nexthops can exist for each route entry but the routing protocol can indicate if
a particular nexthop should not be used in forwarding. Default is `true`.

### 2.2 weight

**Type**: _integer_

Weight is used to differentially balance the packets. Example: For a route if
there are 2 nexthops nh1 with weight 5 and nh2 with weight 1, then for every 5
packets that uses nh1, one packet will use nh2. In the first release, the above
case is not supported. Only ECMP is supported. Default is 0 (for static routes).

### 2.3 type

**Type**: _string_

Type of the nexthop. Default is `unicast`.

### 2.4 ip_address

**Type**: _string_

IP address of the nexthop device.

### 2.5 ports

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



List of outgoing ports. Nexthop entries of type `unicast` can have atmost 1
port.

## 3. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 3.1 other_config

**Type**: _string->string_

### 3.2 external_ids

**Type**: _string->string_

