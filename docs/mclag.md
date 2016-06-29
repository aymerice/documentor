# MCLAG

![MCLAG_table_img](http://www.plantuml.com/plantuml/img/0I01t_v0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJKDCGKSAVGfqRsTbT6XbSY1x2cDiONDp85PIHWfZR65pSo1GRt9q2dqAJKDCGKSWBcGkFY1MKaOAJKDCGKSWBMGjFY1GRt9q2ar3J45782vaBZuWK6zoT0feQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. MCLAG Device configuration

### 1.1 device_priority

**Type**: _integer_

Configures MCLAG device priority. The default value is `1`. Device with the
lower value of priority will be the primary in the case of split brain handling.

### 1.2 split_brain_handling

**Type**: _string_

Configures how MCLAG split-brain is handled. "one-fragment-active" means in case
of a split, MCLAG links of primary will be active and secondary will be
disabled. "dual-active" means in case of a split, MCLAG links of both primary
and secondary will be active. The default value is `one-fragment-active`.

## 2. MCLAG Port configuraiton

### 2.1 isl_port

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _strong_



References port to be used as inter switch link.

## 3. MCLAG Keepalive status

### 3.1 keepalive_status

**Type**: _string->string_

### 3.2 keepalive_status : state

**Type**: _string_

State of the protocol.

### 3.3 keepalive_port

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



Specifies L3 port for keepalive [Port](port.html).

## 4. MCLAG Port statistics

### 4.1 isl_statistics

**Type**: _string->integer_

### 4.2 isl_statistics : hello_tx

**Type**: _integer_

Number of ISLP hello packets transmitted.

### 4.3 isl_statistics : pdu_rx

**Type**: _integer_

Number of ISLP PDUs received.

### 4.4 isl_statistics : hello_rx

**Type**: _integer_

Number of ISLP hello packets received.

### 4.5 isl_statistics : pdu_tx

**Type**: _integer_

Number of ISLP PDUs transmitted.

## 5. MCLAG Operational status

### 5.1 oper_status

**Type**: _string->string_

### 5.2 oper_status : oper_device_priority

**Type**: _string_

Operational device priority. Determines primary and secondary MCLAG role.

### 5.3 oper_status : islp_state

**Type**: _string_

ISL protocol state. in_sync means ISLP link is established. out_of_sync means
ISLP link is not established. Default value is `out_of_sync`.

### 5.4 oper_status : oper_system_id

**Type**: _string_

Operational system id.

## 6. MCLAG ISL timer configuration

### 6.1 isl_timers

**Type**: _string->integer_

### 6.2 isl_timers : hold_time

**Type**: _integer_

Configures ISL port-flap hold time in seconds. The default value is `0`.

### 6.3 isl_timers : timeout

**Type**: _integer_

Configures the amount of time to wait for hellos from peer in seconds. The
default value is `3`.

### 6.4 isl_timers : hello_interval

**Type**: _integer_

ISLP hello interval in seconds. The default value is `1`.

## 7. MCLAG Keepalive configuration

### 7.1 keepalive_vrf

**Type**: _uuid_ **refTable**: [VRF](vrf.html) **refType**: _weak_



VRF to be used for keepalive routing. If not configured, keepalive functionality
is disabled.

### 7.2 keepalive_udp_port

**Type**: _integer_

UDP port number of peer device. The default value is `7678`.

### 7.3 keepalive_src_ip

**Type**: _string_

IPv4 address of the device. If not configured, keepalive functionality is
disabled.

### 7.4 keepalive_peer_ip

**Type**: _string_

IPv4 address of the peer device. If not configured, keepalive functionality is
disabled.

## 8. MCLAG Keepalive packet statistics

### 8.1 keepalive_statistics

**Type**: _string->integer_

### 8.2 keepalive_statistics : rx

**Type**: _integer_

Number of packets received.

### 8.3 keepalive_statistics : tx

**Type**: _integer_

Number of packets transmitted.

## 9. MCLAG Peer status

### 9.1 peer_status

**Type**: _string->string_

### 9.2 peer_status : peer_device_priority

**Type**: _string_

Device priority of the peer switch.

### 9.3 peer_status : peer_isl_port

**Type**: _string_

Name of the logical port on the peer switch configured as ISL port.

### 9.4 peer_status : peer_system_id

**Type**: _string_

System ID of the peer switch.

## 10. MCLAG Keepalive timer configuration

### 10.1 keepalive_timers

**Type**: _string->integer_

### 10.2 keepalive_timers : timeout

**Type**: _integer_

Configures the amount of time to wait for keepalive packets from a peer in
seconds. The default value is `90`.

### 10.3 keepalive_timers : hello_interval

**Type**: _integer_

Keepalive hello interval in seconds. The default value is `30`.

