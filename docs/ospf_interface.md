# OSPF_Interface

![OSPF_Interface_table_img](http://www.plantuml.com/plantuml/img/0OC1VFv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1GRt9q2cDiONDp84zJK4PVJcLfPsXYRt8AOsnXStCWJrDGHbzMR6bkQmfZR65pSo1FKr16NqbkT6LoPc5ZPGfZR65pSo1FKr16Nq5oPM4AVGfFKr16NqbkT6LoPc5ZPI0kP2u-851lSdGAJrDGHbz9RdHbScPXOsKWBcGkFY1FKr16NrPiQMvh2azJK4PVIMvqPN9cOMDb82raBJuWJrDGHbzEPMbdQ69lSWfFKr16NqbkT6LoPc5ZPI0yBNKj84zJK4PVGN9bOGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. status

### 1.1 neighbors

**Type**: _uuid_ **refTable**: [OSPF_Neighbor](ospf_neighbor.html) **refType**: _strong_



The list of all the OSPFv2 neighbors on this OSPFv2 Interface.

### 1.2 status

**Type**: _string->string_

### 1.3 status : active

**Type**: _boolean_

Updates status whether the interface is active. The default value is true.

### 1.4 status : hello_due_at

**Type**: _integer_

Updates when the next hello is due on the interface in seconds. The default
value is hello_interval on this interface.

### 1.5 status : if_out_cost

**Type**: _integer_

The interface out cost. If not configured, this is calculated as per the auto
cost bandwidth reference and interface speed.

### 1.6 ifsm_state

**Type**: _string_

OSPFv2 Interface FSM states. The default value is "depend_upon".

## 2. statistics

### 2.1 statistics

**Type**: _string->integer_

### 2.2 statistics : ls_ack_rcvd

**Type**: _integer_

The total number of Link State Ack packets received on the interface.

### 2.3 statistics : hello_rcvd

**Type**: _integer_

The total number of hello packets received on the interface.

### 2.4 statistics : ls_req_sent

**Type**: _integer_

The total number of Link State Request packets sent on the interface.

### 2.5 statistics : ls_req_rcvd

**Type**: _integer_

The total number of Link State Request packets received on the interface.

### 2.6 statistics : ls_upd_rcvd

**Type**: _integer_

The total number of Link State Update packets received on the interface.

### 2.7 statistics : ls_upd_sent

**Type**: _integer_

The total number of Link State Update packets sent on the interface.

### 2.8 statistics : rx_discard

**Type**: _integer_

The total number of  received packets discarded on the interface.

### 2.9 statistics : hello_sent

**Type**: _integer_

The total number of hello packets sent on the interface.

### 2.10 statistics : state_changes

**Type**: _integer_

The total number of state changes on the interface.

### 2.11 statistics : db_desc_sent

**Type**: _integer_

The total number of DataBase Description packets sent on the interface.

### 2.12 statistics : db_desc_rcvd

**Type**: _integer_

The total number of DataBase Description packets received on the interface.

### 2.13 statistics : ls_ack_sent

**Type**: _integer_

The total number of Link State Ack packets sent on the interface.

## 3. Configuration

### 3.1 ospf_vlink

**Type**: _uuid_ **refTable**: [OSPF_Vlink](ospf_vlink.html) **refType**: _weak_



The virtual link related configurations. This is valid for the interface of type
"virtual link".

### 3.2 port

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



The "Port" corresponding to the OSPFv2 Interface.

### 3.3 name

**Type**: _string_

The OSPFv2 Interface name.

