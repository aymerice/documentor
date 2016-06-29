# MCLAG_Remote_Interface

![MCLAG_Remote_Interface_table_img](http://www.plantuml.com/plantuml/img/0Ha1vlv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJKDCGKTVKcLjRtHbNqbkT6LoPc5ZPGfz2dHlPsLqQ6Lo87iAOsnXStCWK6zoT0fz2ar3J457Nr9bRMzqPLz9RdHbScPXOsKWF2rrBI1GRt9q2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Each entry contains the information about a physical interface on the peer
switch which is configured for MCLAG. This information is determined by
exchanging packets over the ISL link between the MLAG switches.

## 1. partner information

### 1.1 lacp_partner_system_id

**Type**: _string_

Peer interface's LACP partner system ID.

### 1.2 name

**Type**: _string_

Name of the peer interface.

### 1.3 lacp_partner_port_id

**Type**: _integer_

Peer interface's LACP partner port ID.

### 1.4 lacp_partner_key

**Type**: _integer_

Peer interface's LACP partner key.

## 2. partner link status

### 2.1 duplex

**Type**: _string_

The duplex mode of the physical network link.

### 2.2 link_state

**Type**: _string_

The observed state of the physical network link.  This is ordinarily the link's
carrier status.

### 2.3 link_speed

**Type**: _integer_

The negotiated speed of the physical network link in bits per second. Valid
values are positive integers greater than 0.

### 2.4 admin_state

**Type**: _string_

The administrative state of the physical network link.

### 2.5 lacp_partner_state

**Type**: _string_

LACP partner state.

