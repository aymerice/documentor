# Mirror

![Mirror_table_img](http://www.plantuml.com/plantuml/img/0UK06lz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo12ScbaPsKAOsnXStCWK6zoT0fZR65pSo1DQN9oRt8AVGfDQN9oRt8WF2rrBI12ScbaPsKAJMboSczo82vaBZuWK6zoT0feQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

Mirror sessions referenced from a [Bridge](bridge.html).

A mirror configures a bridge to send copies of selected packets to special
"mirrored" ports, in addition to their normal destinations. Mirroring traffic
may also be referred to as SPAN.

## 1. Mirroring Source(s) Configuration group

To be selected for mirroring, a given packet must enter or leave the bridge
through a selected port.  If a source port is in both the select_src_port and
select_dst_port sets, then both transmitted and received packets will be
mirrored.

### 1.1 select_src_port column

Set of Ethernet port or LAG references in [Port](port.html) on which received packets
are selected to be mirrored.

### 1.2 select_dst_port column

Set of Ethernet port or LAG references in [Port](port.html) on which transmitted
packets are selected to be mirrored.

## 2. Mirroring Destination Configuration group

### 2.1 output_port column

Ethernet port or LAG reference in [Port](port.html) used to transmit the mirror
packets.  There must be a valid Ethernet port or LAG for the session operation
state to become active.

The output port should be reserved exclusively for transmitting mirror packets
for this session.  It should not pariticapte in any other network activity (e.g.
Spanning Tree, LLDP etc).

## 3. Mirror Session Statistics group

Key-value pairs that report mirror statistics.  The counts are reset to zero
whenever the operation state transitions to active. The update period is
controlled by [System](system.html) [stats-update-interval](system.html#other-config-stats-update-interval-key).
No counts may be available initally until the first
update period has elasped.  If any key-value pairs remains missing, the hardware
does not support that count.

### 3.1 statistics : tx_bytes key

Number of bytes transmitted through this mirror.

### 3.2 statistics : tx_packets key

Number of packets transmitted through this mirror.

## 4. Mirror Session Status group

### 4.1 mirror_status column

Key-value pair(s) that report mirror status in hardware.

### 4.2 mirror_status : operation_state key

Operational state of the mirror session in hardware. Only the value "active"
means the hardware mirroring is running. Any other value, or if the key is
missing, means the session is not running.

