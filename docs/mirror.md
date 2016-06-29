# Mirror

![Mirror_table_img](http://www.plantuml.com/plantuml/img/0Vy00Fz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo12ScbaPsKAOsnXStCWK6zoT0fZR65pSo1DQN9oRt8AVGfDQN9oRt8WF2rrBI12ScbaPsKAJMboSczo82vaBZuWK6zoT0feQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Mirror sessions referenced from a [Bridge](bridge.html).

A mirror configures a bridge to send copies of selected packets to special
"mirrored" ports, in addition to their normal destinations. Mirroring traffic
may also be referred to as SPAN.

## 1. Mirroring Source(s) Configuration

To be selected for mirroring, a given packet must enter or leave the bridge
through a selected port.  If a source port is in both the select_src_port and
select_dst_port sets, then both transmitted and received packets will be
mirrored.

### 1.1 select_src_port

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



Set of Ethernet port or LAG references in [Port](port.html) on which received packets
are selected to be mirrored.

### 1.2 select_dst_port

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



Set of Ethernet port or LAG references in [Port](port.html) on which transmitted
packets are selected to be mirrored.

## 2. Mirroring Destination Configuration

### 2.1 output_port

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _weak_



Ethernet port or LAG reference in [Port](port.html) used to transmit the mirror
packets.  There must be a valid Ethernet port or LAG for the session operation
state to become active.

The output port should be reserved exclusively for transmitting mirror packets
for this session.  It should not pariticapte in any other network activity (e.g.
Spanning Tree, LLDP etc).

## 3. Mirror Session Statistics

Key-value pairs that report mirror statistics.  The counts are reset to zero
whenever the operation state transitions to active. The update period is
controlled by [System](system.html) [stats-update-interval](system.html#other-config-stats-update-interval).
No counts may be available initally until the first
update period has elasped.  If any key-value pairs remains missing, the hardware
does not support that count.

### 3.1 statistics

**Type**: _string->integer_

### 3.2 statistics : tx_bytes

**Type**: _integer_

Number of bytes transmitted through this mirror.

### 3.3 statistics : tx_packets

**Type**: _integer_

Number of packets transmitted through this mirror.

## 4. Ungrouped

### 4.1 name

**Type**: _string_

There must be a user-defined name of the mirror session.

### 4.2 active

**Type**: _boolean_

The intended state of the mirror session: active or inactive. The
[operation_state](mirror.html#mirror-status-operation-state) value contains the actual state
in hardware (e.g. active, inactive, or error). When missing or false, the state
is inactive.

## 5. Mirror Session Status

### 5.1 mirror_status

**Type**: _string->string_

Key-value pair(s) that report mirror status in hardware.

### 5.2 mirror_status : operation_state

**Type**: _string_

Operational state of the mirror session in hardware. Only the value "active"
means the hardware mirroring is running. Any other value, or if the key is
missing, means the session is not running.

## 6. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 6.1 other_config

**Type**: _string->string_

### 6.2 external_ids

**Type**: _string->string_

