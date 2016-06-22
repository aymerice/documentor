# MCLAG

## 1. MCLAG Device configuration group

### 1.1 device_priority column

Configures MCLAG device priority. The default value is `1`. Device with the
lower value of priority will be the primary in the case of split brain handling.

### 1.2 split_brain_handling column

Configures how MCLAG split-brain is handled. "one-fragment-active" means in case
of a split, MCLAG links of primary will be active and secondary will be
disabled. "dual-active" means in case of a split, MCLAG links of both primary
and secondary will be active. The default value is `one-fragment-active`.

## 2. MCLAG Port configuraiton group

### 2.1 isl_port column

References port to be used as inter switch link.

## 3. MCLAG Keepalive status group

### 3.1 keepalive_status : state key

State of the protocol.

### 3.2 keepalive_port column

Specifies L3 port for keepalive [Port](port.html).

## 4. MCLAG Port statistics group

### 4.1 isl_statistics : hello_tx key

Number of ISLP hello packets transmitted.

### 4.2 isl_statistics : pdu_rx key

Number of ISLP PDUs received.

### 4.3 isl_statistics : hello_rx key

Number of ISLP hello packets received.

### 4.4 isl_statistics : pdu_tx key

Number of ISLP PDUs transmitted.

## 5. MCLAG Operational status group

### 5.1 oper_status : oper_device_priority key

Operational device priority. Determines primary and secondary MCLAG role.

### 5.2 oper_status : islp_state key

ISL protocol state. in_sync means ISLP link is established. out_of_sync means
ISLP link is not established. Default value is `out_of_sync`.

### 5.3 oper_status : oper_system_id key

Operational system id.

## 6. MCLAG ISL timer configuration group

### 6.1 isl_timers : hold_time key

Configures ISL port-flap hold time in seconds. The default value is `0`.

### 6.2 isl_timers : timeout key

Configures the amount of time to wait for hellos from peer in seconds. The
default value is `3`.

### 6.3 isl_timers : hello_interval key

ISLP hello interval in seconds. The default value is `1`.

## 7. MCLAG Keepalive configuration group

### 7.1 keepalive_vrf column

VRF to be used for keepalive routing. If not configured, keepalive functionality
is disabled.

### 7.2 keepalive_udp_port column

UDP port number of peer device. The default value is `7678`.

### 7.3 keepalive_src_ip column

IPv4 address of the device. If not configured, keepalive functionality is
disabled.

### 7.4 keepalive_peer_ip column

IPv4 address of the peer device. If not configured, keepalive functionality is
disabled.

## 8. MCLAG Keepalive packet statistics group

### 8.1 keepalive_statistics : rx key

Number of packets received.

### 8.2 keepalive_statistics : tx key

Number of packets transmitted.

## 9. MCLAG Peer status group

### 9.1 peer_status : peer_device_priority key

Device priority of the peer switch.

### 9.2 peer_status : peer_isl_port key

Name of the logical port on the peer switch configured as ISL port.

### 9.3 peer_status : peer_system_id key

System ID of the peer switch.

## 10. MCLAG Keepalive timer configuration group

### 10.1 keepalive_timers : timeout key

Configures the amount of time to wait for keepalive packets from a peer in
seconds. The default value is `90`.

### 10.2 keepalive_timers : hello_interval key

Keepalive hello interval in seconds. The default value is `30`.

