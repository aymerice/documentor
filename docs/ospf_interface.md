# OSPF_Interface

![OSPF_Interface_table_img](http://www.plantuml.com/plantuml/img/0Ma1blv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1GRt9q2cDiONDp84zJK4PVJcLfPsXYRt8AOsnXStCWJrDGHbzMR6bkQmfZR65pSo1FKr16NqbkT6LoPc5ZPGfZR65pSo1FKr16Nq5oPM4AVGfFKr16NqbkT6LoPc5ZPI0kP2u-851lSdGAJrDGHbz9RdHbScPXOsKWBcGkFY1FKr16NrPiQMvh2azJK4PVIMvqPN9cOMDb82raBJuWJrDGHbzEPMbdQ69lSWfFKr16NqbkT6LoPc5ZPI0yBNKj84zJK4PVGN9bOGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. status group

### 1.1 neighbors column

The list of all the OSPFv2 neighbors on this OSPFv2 Interface.

### 1.2 status : active key

Updates status whether the interface is active. The default value is true.

### 1.3 status : hello_due_at key

Updates when the next hello is due on the interface in seconds. The default
value is hello_interval on this interface.

### 1.4 status : if_out_cost key

The interface out cost. If not configured, this is calculated as per the auto
cost bandwidth reference and interface speed.

### 1.5 ifsm_state column

OSPFv2 Interface FSM states. The default value is "depend_upon".

## 2. statistics group

### 2.1 statistics : ls_ack_rcvd key

The total number of Link State Ack packets received on the interface.

### 2.2 statistics : hello_rcvd key

The total number of hello packets received on the interface.

### 2.3 statistics : ls_req_sent key

The total number of Link State Request packets sent on the interface.

### 2.4 statistics : ls_req_rcvd key

The total number of Link State Request packets received on the interface.

### 2.5 statistics : ls_upd_rcvd key

The total number of Link State Update packets received on the interface.

### 2.6 statistics : ls_upd_sent key

The total number of Link State Update packets sent on the interface.

### 2.7 statistics : rx_discard key

The total number of  received packets discarded on the interface.

### 2.8 statistics : hello_sent key

The total number of hello packets sent on the interface.

### 2.9 statistics : state_changes key

The total number of state changes on the interface.

### 2.10 statistics : db_desc_sent key

The total number of DataBase Description packets sent on the interface.

### 2.11 statistics : db_desc_rcvd key

The total number of DataBase Description packets received on the interface.

### 2.12 statistics : ls_ack_sent key

The total number of Link State Ack packets sent on the interface.

## 3. Configuration group

### 3.1 ospf_vlink column

The virtual link related configurations. This is valid for the interface of type
"virtual link".

### 3.2 port column

The "Port" corresponding to the OSPFv2 Interface.

### 3.3 name column

The OSPFv2 Interface name.

