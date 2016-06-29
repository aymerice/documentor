# Interface

![Interface_table_img](http://www.plantuml.com/plantuml/img/0LO1gVv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo19RdHbScPXOsKAOsnXStCWKtLYStbpT6Lj2cDiONDp8497K5zEPMbdQ69lSWfZR65pSo1GRt9q2dqAIMvqPN9cOMDb83mjTIqWGaTGNqvbQMTeOczo2abkT6LoPc5ZPI0yBNKj85DrOdDvStHbRGf9RdHbScPXOsKWF2rrBI1GRt9q2abkT6LoPc5ZPI0yBNKj84bkT6LoPc5ZPGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

An interface within a [Port](port.html).

## 1. Interface Status

Status information about interfaces attached to bridges, updated every 5
seconds.  Not all interfaces have all of these properties; virtual interfaces
don't have a link speed, for example.  Non-applicable columns will have empty
values.

### 1.1 hw_bond_config

**Type**: _string->string_

Key-value pairs that configure the interface as a member of bond.

### 1.2 hw_bond_config : bond_hw_handle

**Type**: _string_

Identifies the LAG to which this interface should be attached in hardware. This
value is directly copied from [bond_hw_handle](port.html#status-bond-hw-handle).

### 1.3 hw_bond_config : tx_enabled

**Type**: _string_

A state flag to indicate that the transmit logic is enabled for this interface
in hardware LAG. Defaults to `false` if unset.

### 1.4 hw_bond_config : rx_enabled

**Type**: _string_

A state flag to indicate that this interface is attached to a hardware LAG and
receive logic is enabled. Defaults to `false` if unset.

### 1.5 link_state

**Type**: _string_

The observed state of the physical network link.  This is ordinarily the link's
carrier status.

### 1.6 mclag_status

**Type**: _string->string_

### 1.7 mclag_status : actor_port_id

**Type**: _string_

Actor port ID is in the form of device priority (2 bytes) followed by port id (2
bytes) encoded as string in which each byte value is separated by a colon.
Example: 00:08:00:12

### 1.8 mclag_status : actor_key

**Type**: _string_

The actor key in use (2 bytes) encoded as a string in which each byte value is
separated by a colon. Example: 80:00

### 1.9 mclag_status : actor_system_id

**Type**: _string_

Actor system ID is in the form of device priority (2 bytes) followed by device
MAC address (6 bytes) encoded as string in which each byte value is separated by
a colon.  Example:  00:08:00:02:82:1f:60:4a Device priority range is 0 to 15.
Default device priority value is `8`.

### 1.10 kernel_interface_ready

**Type**: _boolean_

Indicates whether kernel interface is provisioned.  Default is false.

### 1.11 link_resets

**Type**: _integer_

The number of times OpenSwitch has observed the
[link_state](interface.html#link-state) of this [Interface](interface.html) change.

### 1.12 duplex

**Type**: _string_

The duplex mode of the physical network link.

### 1.13 hw_status

**Type**: _string->string_

### 1.14 hw_status : ready

**Type**: _boolean_

Status information about hardware resource allocation on the interface. It is
set as false if there are not enough hardware resources or if the resources
required to configure features like ACLs in the interface have not been
allocated yet.  It is set as true when all the resources have been allocated.
The default value is `false`.

### 1.15 hw_status : ready_state_blocked_reason

**Type**: _string_

Enumeration that identifies the asserting protocol that causes the ready to be
"false".

### 1.16 lacp_current

**Type**: _boolean_

Boolean value indicating LACP status for this interface.  If true, this
interface has current LACP information about its LACP partner.  This information
may be used to monitor the health of interfaces in a LACP enabled port.  This
column will be empty if LACP is not enabled.

### 1.17 status

**Type**: _string->string_

Key-value pairs that report port status.  Supported status values are
[type](interface.html#type)-dependent; some interfaces may not have a valid
[driver_name](interface.html#status-driver-name), for example.

### 1.18 status : driver_version

**Type**: _string_

The version string of the device driver controlling the network adapter.

### 1.19 status : kernel_interface_error

**Type**: _string_

Human readable kernel interface provisioning error description.

### 1.20 status : driver_name

**Type**: _string_

The name of the device driver controlling the network adapter.

### 1.21 status : firmware_version

**Type**: _string_

The version string of the network adapter's firmware, if available.

### 1.22 lacp_status

**Type**: _string->string_

Key-value pairs that report LACP protocol status.

### 1.23 lacp_status : lacp_blocked

**Type**: _boolean_

lacp_blocked is set to 'true' if LACP decides to block the interface. Default
value is `false`.

### 1.24 lacp_status : actor_system_id

**Type**: _string_

The LACP actor system ID in the form of priority and mac address tuple.

### 1.25 lacp_status : partner_state

**Type**: _string_

The LACP partner protocol state information in an abbreviated form reporting
status/state bit values. For example,
(Actv:1,TmOut:1,Aggr:1,Sync:1,Col:1,Dist:1,Def:0,Exp:0)

### 1.26 lacp_status : partner_port_id

**Type**: _string_

The LACP partner port ID in the form of priority and port number tuple.

### 1.27 lacp_status : actor_key

**Type**: _string_

The LACP actor key in use.

### 1.28 lacp_status : partner_key

**Type**: _string_

The LACP partner key in use.

### 1.29 lacp_status : partner_system_id

**Type**: _string_

The LACP partner system ID in the form of priority and mac address tuple.

### 1.30 lacp_status : actor_port_id

**Type**: _string_

The LACP actor port ID in the form of priority and port number tuple.

### 1.31 lacp_status : actor_state

**Type**: _string_

The LACP actor protocol state information in an abbreviated form reporting
status/state bit values. For example,
(Actv:1,TmOut:1,Aggr:1,Sync:1,Col:1,Dist:1,Def:0,Exp:0)

### 1.32 mac_in_use

**Type**: _string_

The MAC address in use by this [Interface](interface.html).

### 1.33 link_speed

**Type**: _integer_

The negotiated speed of the physical network link in bits per second. Valid
values are positive integers greater than 0.

### 1.34 pause

**Type**: _string_

The status of the Ethernet PAUSE (link-level flow control) mode of the physical
network link.

### 1.35 admin_state

**Type**: _string_

The administrative state of the physical network link.

### 1.36 bond_status

**Type**: _string->string_

Key-value pairs that report the status of a bond.  This applies to both static
or LACP bonds.

### 1.37 bond_status : state

**Type**: _string_

Enumeration indicating the forwarding state of the interface when it is
configured as a member of a LAG. * Up: The interface is eligible and should be
fowarding traffic according to LACP * Blocked:  The interface is either not
eligible or should be blocked according to LACP.  If an interface is Rx disable,
it is also Tx disable, thus, it is blocked * Down:  The interface is configured
to be a member of a LAG, but it is either administratively or operatively down

### 1.38 mtu

**Type**: _integer_

The MTU (maximum transmission unit); i.e. the largest amount of data that can
fit into a single Ethernet frame. The standard Ethernet MTU is 1500 bytes.  Some
physical media and many kinds of virtual interfaces can be configured with
higher MTUs.

This column will be empty for an interface that does not have an MTU as, for
example, some kinds of tunnels do not.

### 1.39 forwarding_state

**Type**: _string->string_

### 1.40 forwarding_state : interface_aggregation_forwarding

**Type**: _boolean_

Interface aggregation is set based on the information provided by protocols
related to link aggregation. The asserting protocol setting the value of this
key to be defined in the interface_aggregation_blocked_reason key. Default value
is `false`.

### 1.41 forwarding_state : interface_aggregation_blocked_reason

**Type**: _string_

Enumeration that identifies the asserting protocol that causes the interface
aggregation to be different from "forwarding".

### 1.42 forwarding_state : forwarding

**Type**: _boolean_

Enumeration that summarizes the state of the interface. Default value is
`false`.

### 1.43 error

**Type**: _string_

If the configuration of the [Interface](interface.html) failed, OpenSwitch sets this
column to an error description in human readable form.  Otherwise, OpenSwitch
clears this column.

### 1.44 LLDP Neighbor Info

#### 1.44.1 lldp_neighbor_info

**Type**: _string->string_

Keys-value pairs of neighbor's port info as discovered by LLDP.

#### 1.44.2 lldp_neighbor_info : port_description

**Type**: _string_

The port description field shall contain an alpha-numeric string that indicates
the port's description.

#### 1.44.3 lldp_neighbor_info : port_mfs

**Type**: _string_

Port maximum frame size.

#### 1.44.4 lldp_neighbor_info : mgmt_ip_list

**Type**: _string_

A comma-seperated list of management IP addresses.

#### 1.44.5 lldp_neighbor_info : port_lastupdate

**Type**: _string_

Time (posix seconds) of last update received.

#### 1.44.6 lldp_neighbor_info : chassis_capability_available

**Type**: _string_

The chassis capabilities field contains a bit-map of the capabilities that
define the primary function(s) of the system. A binary one in the associated bit
indicates the existence of that capability. Individual systems may indicate more
than one implemented functional capability (for example, both a bridge and
router capability).

#### 1.44.7 lldp_neighbor_info : port_lastchange

**Type**: _string_

Time (posix seconds) of last change of values.

#### 1.44.8 lldp_neighbor_info : port_id

**Type**: _string_

The Port ID is a mandatory TLV that identifies the port component of the MSAP
identifier associated with the transmitting LLDP agent.

#### 1.44.9 lldp_neighbor_info : chassis_refcount

**Type**: _string_

Chassis reference count.

#### 1.44.10 lldp_neighbor_info : pids_len_list

**Type**: _string_

A comma-seperated list of length of protocol ID names.

#### 1.44.11 lldp_neighbor_info : power_powertype

**Type**: _string_

Power type or LLDP_DOT3_POWER_8023AT_OFF indicating source, priority, requested
and allocated have no meaning.

#### 1.44.12 lldp_neighbor_info : power_supported

**Type**: _string_

Power value is the power the neighbor supports.

#### 1.44.13 lldp_neighbor_info : power_paircontrol

**Type**: _string_

Describes the capability of controlling the power pairs functionality to switch
pins for sourcing power. The value true indicate that the device has the
capability to control the power pairs.  When false the PSE Pinout Alternative
used cannot be controlled through the PethPsePortAdminEnable attribute.

#### 1.44.14 lldp_neighbor_info : chassis_id

**Type**: _string_

The Chassis ID identifies the chassis containing the IEEE 802 LAN station
associated with the transmitting LLDP agent.

#### 1.44.15 lldp_neighbor_info : port_id_subtype

**Type**: _string_

The port ID subtype field shall contain an integer value indicating the basis
for the identifier that is listed in the port ID field.

#### 1.44.16 lldp_neighbor_info : chassis_capability_enabled

**Type**: _string_

The enabled capabilities field contains a bit map of the primary functions of
the system. A binary one in a bit position indicates that the function is
currently enabled.

#### 1.44.17 lldp_neighbor_info : macphy_autoneg_enabled

**Type**: _string_

Link autonegotiation enabled.

#### 1.44.18 lldp_neighbor_info : chassis_index

**Type**: _string_

The interface index value used to identify the chassis.

#### 1.44.19 lldp_neighbor_info : chassis_name

**Type**: _string_

The system name field contains an alpha-numeric string that indicates the
administratively assigned name.

#### 1.44.20 lldp_neighbor_info : port_hidden_in

**Type**: _string_

Considered as hidden for reception.

#### 1.44.21 lldp_neighbor_info : port_id_len

**Type**: _string_

Port ID length.

#### 1.44.22 lldp_neighbor_info : mgmt_iface_list

**Type**: _string_

A comma-seperated list of management IP interfaces.

#### 1.44.23 lldp_neighbor_info : pids_name_list

**Type**: _string_

A comma-seperated list of protocol ID name.

#### 1.44.24 lldp_neighbor_info : power_priority

**Type**: _string_

Power priority configured on the neighbor port.

#### 1.44.25 lldp_neighbor_info : chassis_ttl

**Type**: _string_

The Time To Live TLV indicates the number of seconds that the recipient LLDP
agent is to regard the information associated with this MSAP identifier to be
valid.

#### 1.44.26 lldp_neighbor_info : vlan_name_list

**Type**: _string_

A comma-seperated list of vlan names.

#### 1.44.27 lldp_neighbor_info : port_hidden_out

**Type**: _string_

Considered as hidden for transmission.

#### 1.44.28 lldp_neighbor_info : macphy_mau_type

**Type**: _string_

Common enumeration values for repeater and interface MAU jack types.

#### 1.44.29 lldp_neighbor_info : chassis_id_len

**Type**: _string_

Chassis ID TLV length.

#### 1.44.30 lldp_neighbor_info : power_source

**Type**: _string_

Power Source code indicates neighbor Primary Power Source or the Backup Power
Source.

#### 1.44.31 lldp_neighbor_info : chassis_protocol

**Type**: _string_

Chassis protocol name (LLDP).

#### 1.44.32 lldp_neighbor_info : chassis_description

**Type**: _string_

The chassis description field contains an alpha-numeric string that is the
textual description of the network entity. It includes the full name and version
identification of the hardware type, software operating system, and networking
software.

#### 1.44.33 lldp_neighbor_info : vlan_id_list

**Type**: _string_

A comma-seperated list of vlan IDs.

#### 1.44.34 lldp_neighbor_info : power_allocated

**Type**: _string_

The power value is the power the neighbor allocates.

#### 1.44.35 lldp_neighbor_info : port_protocol

**Type**: _string_

Protocol used to get this port (LLDP).

#### 1.44.36 lldp_neighbor_info : ppvids_ppvid_list

**Type**: _string_

A comma-seperated list of port and protocol vlan IDs.

#### 1.44.37 lldp_neighbor_info : port_pvid

**Type**: _string_

The port VLAN identifier field shall contain the VLAN ID for the bridge port as
defined in 8.4.4 of IEEE Std 802.1Q.

#### 1.44.38 lldp_neighbor_info : macphy_autoneg_advertised

**Type**: _string_

Link autonegotiation advertized.

#### 1.44.39 lldp_neighbor_info : macphy_autoneg_support

**Type**: _string_

Link autonnegotiation supported.

#### 1.44.40 lldp_neighbor_info : ppvids_cap_list

**Type**: _string_

A comma-seperated list of port and protocol vlan capablity.

#### 1.44.41 lldp_neighbor_info : chassis_id_subtype

**Type**: _string_

The chassis ID subtype field contains an integer value indicating the basis for
the chassis ID entity listed in the chassis ID field.

#### 1.44.42 lldp_neighbor_info : power_pairs

**Type**: _string_

Describes or controls the pairs in use. A value of signal(1) means that the
signal pairs only are in use. A value of spare(2) means that the spare pairs
only are in use.

#### 1.44.43 lldp_neighbor_info : power_requested

**Type**: _string_

The power value is the power the neighbor requests.

### 1.45 LLDP status info

#### 1.45.1 status

**Type**: _string->string_

Key-value pairs that report port status.  Supported status values are
[type](interface.html#type)-dependent; some interfaces may not have a valid
[driver_name](interface.html#status-driver-name), for example.

#### 1.45.2 status : lldp_local_port_vlan

**Type**: _string_

Information about port VLAN config.

#### 1.45.3 status : lldp_local_port_description

**Type**: _string_

Description of LLDP port in alpha-numeric format.

### 1.46 IKE Status: ipsec_gre_ike only

#### 1.46.1 status : ipsec_bytes_out

**Type**: _integer_

Reports output bytes processed.

#### 1.46.2 status : ipsec_sa_spi_out

**Type**: _integer_

Reports the Security Parameter Index used for SA outbound traffics.

#### 1.46.3 status : ipsec_bytes_in

**Type**: _integer_

Reports input bytes processed.

#### 1.46.4 status : ipsec_packets_out

**Type**: _integer_

Reports output packets processed.

#### 1.46.5 status : ipsec_ike_reauth_time

**Type**: _integer_

Reports the epoch time when this connection re-authenticates.

#### 1.46.6 status : ipsec_sa_spi_in

**Type**: _integer_

Reports the Security Parameter Index used for SA inbound traffics.

#### 1.46.7 status : ipsec_ike_responder_spi

**Type**: _integer_

Reports the IKE responder SPI.

#### 1.46.8 status : ipsec_ike_initiator_spi

**Type**: _integer_

Reports the IKE initiator SPI.

#### 1.46.9 status : ipsec_sa_expiration_time

**Type**: _integer_

Reports the epoch time when this SA expires.

#### 1.46.10 status : ipsec_ike_established_time

**Type**: _integer_

Reports the epoch time when this connection is established.

#### 1.46.11 status : ipsec_packets_in

**Type**: _integer_

Reports input packets processed.

#### 1.46.12 status : ipsec_sa_rekey_time

**Type**: _integer_

Reports the epoch time when this SA re-keys.

#### 1.46.13 status : ipsec_sa_state

**Type**: _string_

Reports the this SA state.

#### 1.46.14 status : ipsec_ike_conn_state

**Type**: _string_

Reports this connection state.

## 2. Hardware Interface Information

The following fields describes the hardware information of
[Interface](interface.html). These values do not change through the life of the
system.

### 2.1 split_parent

**Type**: _uuid_ **refTable**: [Interface](interface.html) **refType**: _strong_



For a split child interface, this is the reference to the parent
[Interface](interface.html).

### 2.2 subintf_parent

**Type**: _integer->uuid_ **refTable**: [Interface](interface.html) **refType**: _strong_



For a subinterface, this column holds the reference to the parent interface
[Interface](interface.html). The key is the dot1q encapsulation vlan id and the value
is the uuid of parent interface.

### 2.3 split_children

**Type**: _uuid_ **refTable**: [Interface](interface.html) **refType**: _strong_



For a split parent interface, this is the reference to the list of children
[Interface](interface.html)s.

### 2.4 hw_intf_info

**Type**: _string->string_

Key-value pairs that show the information about a physical interface.

### 2.5 hw_intf_info : bridge

**Type**: _boolean_

Boolean value indicating interface is a `bridge` interface which is created for
every bridge instance. The `bridge` interface receives all VLAN traffic and
distributes to the vlan interfaces based on the VLAN tags. The default value is
`false`

### 2.6 hw_intf_info : capability_split_4

**Type**: _string_

+ Boolean value indicating whether or not the interface supports being split
into four split ports. For example, a QSFP
+ port can run as a single port or can be split into four 10G split ports using
a QSFP
+ splitter cable.

### 2.7 hw_intf_info : switch_unit

**Type**: _string_

The hardware switch chip unit identifier. This value is applicable only to
interfaces on physical switch devices.

### 2.8 hw_intf_info : pluggable

**Type**: _string_

Boolean value indicating whether or not the interface has a fixed connector or a
pluggable module socket.

### 2.9 hw_intf_info : connector

**Type**: _string_

The form factor of the interface socket. The possible values are "SFP_PLUS" and
"QSFP_PLUS".

### 2.10 hw_intf_info : capability_enet10G

**Type**: _string_

Boolean value indicating whether or not the interface supports Ethernet 10G
speed.

### 2.11 hw_intf_info : switch_intf_id

**Type**: _string_

The hardware switch chip interface identifier. This value is applicable only to
interfaces on physical switch devices.

### 2.12 hw_intf_info : max_speed

**Type**: _string_

The maximum speed of the interface in units of megabits per second.

### 2.13 hw_intf_info : mac_addr

**Type**: _string_

The MAC Address for the interface.

### 2.14 hw_intf_info : capability_enet40G

**Type**: _string_

Boolean value indicating whether or not the interface supports Ethernet 40G
speed.

### 2.15 hw_intf_info : capability_enet1G

**Type**: _string_

Boolean value indicating whether or not the interface supports Ethernet 1G
speed.

### 2.16 hw_intf_info : speeds

**Type**: _string_

The list of supported speeds of the interface in units of megabits per second.

## 3. User Configuration

The following fields are meant to be configured by the user. It represents the
configuration of the interface in the bridge.

### 3.1 user_config

**Type**: _string->string_

Key-value pairs that stores the user configuration of [Interface](interface.html).

### 3.2 user_config : pause

**Type**: _string_

The user-configured Ethernet PAUSE (link-level flow control) mode of
[Interface](interface.html). The possible values are "none", "rx", "tx", and "rxtx".

### 3.3 user_config : admin

**Type**: _string_

The user-configured administrative state of [Interface](interface.html). The possible
values are "up" and "down".  Default is "down" if not specified.

### 3.4 user_config : lane_split

**Type**: _string_

+ The user-configured split mode of [Interface](interface.html). This is only
applicable if an interface can be split into multiple interfaces, e.g. QSFP
+ ports. The possible values are "split" and "no-split".

### 3.5 user_config : mtu

**Type**: _string_

The user-configured MTU of [Interface](interface.html).

### 3.6 user_config : duplex

**Type**: _string_

The user-configured duplex mode of [Interface](interface.html). The possible values
are "half" and "full".

### 3.7 user_config : autoneg

**Type**: _string_

The user-configured auto-negotiation state of [Interface](interface.html). The
possible values are "default", "on", and "off".

### 3.8 user_config : speeds

**Type**: _string_

The list of user-configured interface speeds in megabits per second. When
autoneg is disabled, the first speed value in the list is applied.

## 4. Statistics

Key-value pairs that report interface statistics.  The current implementation
updates these counters periodically.  The update period is controlled by [stats-
update-interval](system.html#other-config-stats-update-interval) in the
[System](system.html) table.

If an interface does not support a given statistic, then that pair is omitted.

### 4.1 Statistics: Interface Queue Transmit Statistics

#### 4.1.1 queue_tx_bytes

**Type**: _integer->integer_

For each outbound queue, a count of the queue's total bytes transmitted.

#### 4.1.2 queue_tx_errors

**Type**: _integer->integer_

For each outbound queue, a count of the queue's total transmit errors or drops.

#### 4.1.3 queue_tx_packets

**Type**: _integer->integer_

For each outbound queue, a count of the queue's total packets transmitted.

### 4.2 Statistics: Successful transmit and receive counters

#### 4.2.1 statistics

**Type**: _string->integer_

#### 4.2.2 statistics : tx_packets

**Type**: _integer_

Number of transmitted packets.

#### 4.2.3 statistics : rx_packets

**Type**: _integer_

Number of received packets.

#### 4.2.4 statistics : tx_bytes

**Type**: _integer_

Number of transmitted bytes.

#### 4.2.5 statistics : rx_bytes

**Type**: _integer_

Number of received bytes.

### 4.3 Statistics: Receive errors

#### 4.3.1 statistics

**Type**: _string->integer_

#### 4.3.2 statistics : rx_over_err

**Type**: _integer_

Number of packets with RX overrun.

#### 4.3.3 statistics : rx_dropped

**Type**: _integer_

Number of packets dropped by RX.

#### 4.3.4 statistics : rx_frame_err

**Type**: _integer_

Number of frame alignment errors.

#### 4.3.5 statistics : rx_crc_err

**Type**: _integer_

Number of CRC errors.

#### 4.3.6 statistics : rx_errors

**Type**: _integer_

Total number of receive errors, greater than or equal to the sum of the above.

### 4.4 Statistics: Transmit errors

#### 4.4.1 statistics

**Type**: _string->integer_

#### 4.4.2 statistics : collisions

**Type**: _integer_

Number of collisions.

#### 4.4.3 statistics : tx_dropped

**Type**: _integer_

Number of packets dropped by TX.

#### 4.4.4 statistics : tx_errors

**Type**: _integer_

Total number of transmit errors, greater than or equal to the sum of the above.

### 4.5 Layer3 - IP Statistics

#### 4.5.1 statistics

**Type**: _string->integer_

#### 4.5.2 statistics : ipv6_mc_tx_packets

**Type**: _integer_

Number of transmitted ipv6 multicast packets.

#### 4.5.3 statistics : ipv6_mc_rx_packets

**Type**: _integer_

Number of received ipv6 multicast packets.

#### 4.5.4 statistics : ipv6_uc_rx_packets

**Type**: _integer_

Number of received ipv6 unicast packets.

#### 4.5.5 statistics : ipv4_uc_rx_packets

**Type**: _integer_

Number of received ipv4 unicast packets.

#### 4.5.6 statistics : ipv4_uc_tx_packets

**Type**: _integer_

Number of transmitted ipv4 unicast packets.

#### 4.5.7 statistics : ipv6_mc_rx_bytes

**Type**: _integer_

Number of received ipv6 multicast bytes.

#### 4.5.8 statistics : ipv6_mc_tx_bytes

**Type**: _integer_

Number of transmitted ipv6 multicast bytes.

#### 4.5.9 statistics : ipv4_mc_rx_bytes

**Type**: _integer_

Number of received ipv4 multicast bytes.

#### 4.5.10 statistics : ipv4_mc_tx_bytes

**Type**: _integer_

Number of transmitted ipv4 multicast bytes.

#### 4.5.11 statistics : ipv4_uc_tx_bytes

**Type**: _integer_

Number of transmitted ipv4 unicast bytes.

#### 4.5.12 statistics : ipv6_uc_tx_packets

**Type**: _integer_

Number of transmitted ipv6 unicast packets.

#### 4.5.13 statistics : ipv4_mc_rx_packets

**Type**: _integer_

Number of received ipv4 multicast packets.

#### 4.5.14 statistics : ipv4_mc_tx_packets

**Type**: _integer_

Number of transmitted ipv4 multicast packets.

#### 4.5.15 statistics : ipv6_uc_rx_bytes

**Type**: _integer_

Number of received ipv6 unicast bytes.

#### 4.5.16 statistics : ipv6_uc_tx_bytes

**Type**: _integer_

Number of transmitted ipv6 unicast bytes.

#### 4.5.17 statistics : ipv4_uc_rx_bytes

**Type**: _integer_

Number of received ipv4 unicast bytes.

### 4.6 sFlow Statistics

#### 4.6.1 statistics

**Type**: _string->integer_

#### 4.6.2 statistics : sflow_ingress_bytes

**Type**: _integer_

Number of ingress bytes sampled on an interface.

#### 4.6.3 statistics : sflow_egress_bytes

**Type**: _integer_

Number of egress bytes sampled on an interface.

#### 4.6.4 statistics : sflow_egress_packets

**Type**: _integer_

Number of egress packets sampled on an interface.

#### 4.6.5 statistics : sflow_ingress_packets

**Type**: _integer_

Number of ingress packets sampled on an interface.

### 4.7 LLDP Interface Level Statistics

#### 4.7.1 lldp_statistics

**Type**: _string->integer_

#### 4.7.2 lldp_statistics : lldp_rx_discard

**Type**: _integer_

Number of lldp packet received and discarded because of missing, out-of-order or
incorrect TLVs.

#### 4.7.3 lldp_statistics : lldp_rx_tlv_discard

**Type**: _integer_

Number of lldp TLVs discarded because of errors.

#### 4.7.4 lldp_statistics : lldp_tx_len_err

**Type**: _integer_

Number of lldp packet transmit error because of length.

#### 4.7.5 lldp_statistics : lldp_rx_tlv_unknown

**Type**: _integer_

Number of lldp TLVs discarded because of unknown tlv.

#### 4.7.6 lldp_statistics : lldp_rx_err

**Type**: _integer_

Number of lldp packets received with one or more detectable errors.

#### 4.7.7 lldp_statistics : lldp_tx

**Type**: _integer_

Number of lldp packets transmitted.

#### 4.7.8 lldp_statistics : lldp_rx

**Type**: _integer_

Number of lldp packets received.

## 5. System-Specific Details

### 5.1 type

**Type**: _string_

The interface type, one of:

+ __`system`__:  An ordinary network device, e.g. `eth0` on Linux. Sometimes
referred to as ``external interfaces'' since they are generally connected to
hardware external to that on which the OpenSwitch is running.  The empty string
is a synonym for `system`.
+ __`internal`__:  A simulated network device that sends and receives traffic.
An internal interface whose [name](interface.html#name) is the same as its bridge's
[name](bridge.html#name) is called the ``local interface.''  It does not make sense
to bond an internal interface, so the terms ``port'' and ``interface'' are often
used imprecisely for internal interfaces.
+ __`vlansubint`__:  A sub-interface created for a physical interface. Sub-
interfaces are used for router-on-stick configurations and to allow separation
of traffic on a L3 physical interface based on dot1q encapsulation VLAN and
apply policies on them.
+ __`loopback`__:  A loopback interface is a virtual interface, supporting
IPv4/IPv6 address configuration, that remains up until it is deleted by
administrator. Loopback interface IP address is used as router-id and source
address by many protocols.
+ __`vxlan`__:  This is a vitual interface of type vxlan (L2 overlay over L3
network RFC 7348).

## 6. Hardware Interface Configuration

The following fields are not meant to be configured by the user, but rather by
`intfd` daemon that is responsible to consider user configuration or the port
admin_state configuration and business logic in order to determine hardware
configuration. When port associated with the interface is configured to down the
hardware configuration is forced to down.

### 6.1 hw_intf_config

**Type**: _string->string_

Key-value pairs that represent the configuration passed down to hardware.

### 6.2 hw_intf_config : pause

**Type**: _string_

The possible values are "none", "rx", "tx", and "rxtx".

### 6.3 hw_intf_config : duplex

**Type**: _string_

The possible values are "half" and "full".

### 6.4 hw_intf_config : interface_type

**Type**: _string_

Physical layer interface type of [Interface](interface.html). The possible values are
"unknown", "backplane", "1GBASE_SX", "1GBASE_T", "10GBASE_CR", "10GBASE_SR",
"10GBASE_LR", "10GBASE_LRM", "40GBASE_CR4", "40GBASE_SR4" and "40GBASE_LR4".

### 6.5 hw_intf_config : mtu

**Type**: _string_

Maximum transmission unit (MTU) of [Interface](interface.html).

### 6.6 hw_intf_config : enable

**Type**: _string_

The possible values are "true" and "false".

### 6.7 hw_intf_config : autoneg

**Type**: _string_

The possible values are "on" and "off".

### 6.8 hw_intf_config : speeds

**Type**: _string_

The list of possible interface speeds, in megabits per second. If autoneg is
true, this is the list of advertised speeds. If not, the first speed in the list
is the fixed speed of [Interface](interface.html).

## 7. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 7.1 external_ids

**Type**: _string->string_

### 7.2 other_config

**Type**: _string->string_

### 7.3 LLDP Interface configurations

#### 7.3.1 other_config

**Type**: _string->string_

#### 7.3.2 other_config : lldp_enable_dir

**Type**: _string_

LLDP interface level config.

## 8. Core Features

### 8.1 name

**Type**: _string_

Interface name.  Should be alphanumeric and no more than about 8 bytes long.
May be the same as the port name, for non-bonded ports.  Must otherwise be
unique among the names of ports, interfaces, and bridges on a host.

## 9. Bonding Configuration

### 9.1 other_config

**Type**: _string->string_

### 9.2 other_config : lacp-port-priority

**Type**: _integer_

The LACP port priority of this [Interface](interface.html).  In LACP negotiations
[Interface](interface.html)s with numerically lower priorities are preferred for
aggregation.

### 9.3 other_config : lacp-port-id

**Type**: _integer_

The LACP port ID of this [Interface](interface.html).  Port IDs are used in LACP
negotiations to identify individual ports participating in a bond.

### 9.4 other_config : lacp-aggregation-key

**Type**: _integer_

The LACP aggregation key of this [Interface](interface.html). [Interface](interface.html)s
with different aggregation keys may not be active within a given [Port](port.html) at
the same time.

## 10. Module Information

Information about the pluggable module inserted into the physical interface
socket.

### 10.1 pm_info

**Type**: _string->string_

Key-value pairs that report pluggable module information.

### 10.2 pm_info : tx_power_high_alarm_threshold

**Type**: _real_

+ Alarm high threshold value of output power, ranging from 0 to 6.5535, in units
of milliwatts. This is a factory preset value in DOM supporting SFP
+ module.

### 10.3 pm_info : rx3_power_low_alarm

**Type**: _string_

+ Flag to indicate received average optical power in channel 3 of QSFP
+ module is below low alarm level. This value is from DOM supporting QSFP
+ module.

### 10.4 pm_info : tx_bias_high_warning_threshold

**Type**: _real_

+ Warning high threshold value of TX bias current, ranging from 0 to 131, in
units of milliamps. This is a factory preset value in DOM supporting SFP
+ module.

### 10.5 pm_info : rx_power_high_warning

**Type**: _string_

+ Flag to indicate received average optical power exceeds high warning level.
This value is from DOM supporting SFP
+ module.

### 10.6 pm_info : rx1_power_high_warning

**Type**: _string_

+ Flag to indicate received average optical power in channel 1 of QSFP
+ module exceeds high warning level. This value is from DOM supporting QSFP
+ module.

### 10.7 pm_info : rx4_power_high_warning

**Type**: _string_

+ Flag to indicate received average optical power in channel 4 of QSFP
+ module exceeds high warning level. This value is from DOM supporting QSFP
+ module.

### 10.8 pm_info : rx_power_low_warning_threshold

**Type**: _real_

+ Warning low threshold value of received average optical power. The valid value
range is 0 to 6.5535, in units of milliwatts. This is a factory preset value in
DOM supporting SFP
+ module.

### 10.9 pm_info : vcc_low_warning

**Type**: _string_

+ Flag to indicate internal supply voltage is below low warning level. This
value is from DOM supporting SFP
+ module.

### 10.10 pm_info : vcc_high_warning

**Type**: _string_

+ Flag to indicate internal supply voltage exceeds high warning level. This
value is from DOM supporting SFP
+ module.

### 10.11 pm_info : vcc_low_alarm

**Type**: _string_

+ Flag to indicate internal supply voltage is below low alarm level. This value
is from DOM supporting SFP
+ module.

### 10.12 pm_info : tx_power_high_warning

**Type**: _string_

+ Flag to indicate output power exceeds high warning level. This value is from
DOM supporting SFP
+ module.

### 10.13 pm_info : rx_power_low_warning

**Type**: _string_

+ Flag to indicate received average optical power is below low warning level.
This value is from DOM supporting SFP
+ module.

### 10.14 pm_info : vcc_high_alarm

**Type**: _string_

+ Flag to indicate internal supply voltage exceeds high alarm level. This value
is from DOM supporting SFP
+ module.

### 10.15 pm_info : rx4_power_high_alarm

**Type**: _string_

+ Flag to indicate received average optical power in channel 4 of QSFP
+ module exceeds high alarm level. This value is from DOM supporting QSFP
+ module.

### 10.16 pm_info : rx4_power_low_alarm

**Type**: _string_

+ Flag to indicate received average optical power in channel 4 of QSFP
+ module is below low alarm level. This value is from DOM supporting QSFP
+ module.

### 10.17 pm_info : temperature_low_alarm

**Type**: _string_

+ Flag to indicate internal temperature is below low alarm level. This value is
from DOM supporting SFP
+ module.

### 10.18 pm_info : rx4_power_low_warning

**Type**: _string_

+ Flag to indicate received average optical power in channel 4 of QSFP
+ module is below low warning level. This value is from DOM supporting QSFP
+ module.

### 10.19 pm_info : rx_power_high_alarm_threshold

**Type**: _real_

+ Alarm high threshold value of received average optical power. The valid value
range is 0 to 6.5535, in units of milliwatts. This is a factory preset value in
DOM supporting SFP
+ module.

### 10.20 pm_info : tx_bias_low_alarm_threshold

**Type**: _real_

+ Alarm low threshold value of TX bias current, ranging from 0 to 131, in units
of milliamps. This is a factory preset value in DOM supporting SFP
+ module.

### 10.21 pm_info : tx4_bias_high_warning

**Type**: _string_

+ Flag to indicate TX bias current in channel 4 of QSFP
+ module exceeds high warning level. This value is from DOM supporting QSFP
+ module.

### 10.22 pm_info : tx_power_low_warning

**Type**: _string_

+ Flag to indicate output power is below low warning level. This value is from
DOM supporting SFP
+ module.

### 10.23 pm_info : tx4_bias

**Type**: _real_

+ Transceiver TX bias current in channel 4 of QSFP
+ module, ranging from 0 to 131, in units of milliamps. This value is from DOM
supporting QSFP
+ module.

### 10.24 pm_info : tx2_bias_low_alarm

**Type**: _string_

+ Flag to indicate TX bias current in channel 2 of QSFP
+ module is below low alarm level. This value is from DOM supporting QSFP
+ module.

### 10.25 pm_info : rx3_power

**Type**: _real_

+ Transceiver received average optical power in channel 3 of QSFP
+ module. The valid value range is 0 to 6.5535, in units of milliwatts. This
value is from DOM supporting QSFP
+ module.

### 10.26 pm_info : rx2_power_low_alarm

**Type**: _string_

+ Flag to indicate received average optical power in channel 2 of QSFP
+ module is below low alarm level. This value is from DOM supporting QSFP
+ module.

### 10.27 pm_info : connector_status

**Type**: _string_

The status of the connector to indicate whether it is supported by the hardware
platform. The possible values are "unrecognized", "unsupported" and "supported".

### 10.28 pm_info : temperature_low_alarm_threshold

**Type**: _real_

+ Alarm low threshold value of internal temperature, ranging from -128 to 128,
in units of Celsius. This is a factory preset value in DOM supporting SFP
+ module.

### 10.29 pm_info : tx_power_high_warning_threshold

**Type**: _real_

+ Warning high threshold value of output power, ranging from 0 to 6.5535, in
units of milliwatts. This is a factory preset value in DOM supporting SFP
+ module.

### 10.30 pm_info : tx2_bias_high_alarm

**Type**: _string_

+ Flag to indicate TX bias current in channel 2 of QSFP
+ module exceeds high alarm level. This value is from DOM supporting QSFP
+ module.

### 10.31 pm_info : vcc

**Type**: _real_

+ Internally measured transceiver supply voltage, ranging from 0 to 6.55, in
units of Volts. This value is from DOM supporting SFP+/QSFP
+ module.

### 10.32 pm_info : vendor_oui

**Type**: _string_

The Organizationally Unique Identifier (OUI) of the module vendor.

### 10.33 pm_info : rx4_power

**Type**: _real_

+ Transceiver received average optical power in channel 4 of QSFP
+ module. The valid value range is 0 to 6.5535, in units of milliwatts. This
value is from DOM supporting QSFP
+ module.

### 10.34 pm_info : temperature_high_alarm_threshold

**Type**: _real_

+ Alarm high threshold value of internal temperature, ranging from -128 to 128,
in units of Celsius. This is a factory preset value in DOM supporting SFP
+ module.

### 10.35 pm_info : rx1_power_low_alarm

**Type**: _string_

+ Flag to indicate received average optical power in channel 1 of QSFP
+ module is below low alarm level. This value is from DOM supporting QSFP
+ module.

### 10.36 pm_info : tx2_bias

**Type**: _real_

+ Transceiver TX bias current in channel 2 of QSFP
+ module, ranging from 0 to 131, in units of milliamps. This value is from DOM
supporting QSFP
+ module.

### 10.37 pm_info : temperature_low_warning

**Type**: _string_

+ Flag to indicate internal temperature is below low warning level. This value
is from DOM supporting SFP
+ module.

### 10.38 pm_info : rx3_power_high_alarm

**Type**: _string_

+ Flag to indicate received average optical power in channel 3 of QSFP
+ module exceeds high alarm level. This value is from DOM supporting QSFP
+ module.

### 10.39 pm_info : cable_technology

**Type**: _string_

This indicates whether a copper pluggable module is active or passive. The
possible values are "active" and "passive".

### 10.40 pm_info : max_speed

**Type**: _string_

The maximum speed supported by the transceiver, in units of megabits per second.

### 10.41 pm_info : rx_power

**Type**: _real_

+ Transceiver received average optical power, ranging from 0 to 6.5535, in units
of milliwatts. This value is from DOM supporting SFP
+ module.

### 10.42 pm_info : tx_bias_high_warning

**Type**: _string_

+ Flag to indicate TX bias current exceeds high warning level. This value is
from DOM supporting SFP
+ module.

### 10.43 pm_info : vcc_high_warning_threshold

**Type**: _real_

+ Warning high threshold value of internal supply voltage, ranging from 0 to
6.55, in units of Volts. This is a factory preset value in DOM supporting SFP
+ module.

### 10.44 pm_info : tx1_bias_low_warning

**Type**: _string_

+ Flag to indicate TX bias current in channel 1 of QSFP
+ module is below low warning level. This value is from DOM supporting QSFP
+ module.

### 10.45 pm_info : temperature

**Type**: _real_

+ Internally measured transceiver temperature, ranging from -128 to 128, in
units of Celsius. This value is from DOM supporting SFP+/QSFP
+ module.

### 10.46 pm_info : vendor_revision

**Type**: _string_

The vendor's module revision number.

### 10.47 pm_info : tx3_bias_low_warning

**Type**: _string_

+ Flag to indicate TX bias current in channel 3 of QSFP
+ module is below low warning level. This value is from DOM supporting QSFP
+ module.

### 10.48 pm_info : tx3_bias_high_alarm

**Type**: _string_

+ Flag to indicate TX bias current in channel 3 of QSFP
+ module exceeds high alarm level. This value is from DOM supporting QSFP
+ module.

### 10.49 pm_info : tx1_bias

**Type**: _real_

+ Transceiver TX bias current in channel 1 of QSFP
+ module, ranging from 0 to 131, in units of milliamps. This value is from DOM
supporting QSFP
+ module.

### 10.50 pm_info : tx1_bias_low_alarm

**Type**: _string_

+ Flag to indicate TX bias current in channel 1 of QSFP
+ module is below low alarm level. This value is from DOM supporting QSFP
+ module.

### 10.51 pm_info : rx3_power_high_warning

**Type**: _string_

+ Flag to indicate received average optical power in channel 3 of QSFP
+ module exceeds high warning level. This value is from DOM supporting QSFP
+ module.

### 10.52 pm_info : vcc_high_alarm_threshold

**Type**: _real_

+ Alarm high threshold value of internal supply voltage, ranging from 0 to 6.55,
in units of Volts. This is a factory preset value in DOM supporting SFP
+ module.

### 10.53 pm_info : tx_power_low_alarm_threshold

**Type**: _real_

+ Alarm low threshold value of output power, ranging from 0 to 6.5535, in units
of milliwatts. This is a factory preset value in DOM supporting SFP
+ module.

### 10.54 pm_info : tx_bias_low_alarm

**Type**: _string_

+ Flag to indicate TX bias current is below low alarm level. This value is from
DOM supporting SFP
+ module.

### 10.55 pm_info : rx1_power_high_alarm

**Type**: _string_

+ Flag to indicate received average optical power in channel 1 of QSFP
+ module exceeds high alarm level. This value is from DOM supporting QSFP
+ module.

### 10.56 pm_info : tx2_bias_low_warning

**Type**: _string_

+ Flag to indicate TX bias current in channel 2 of QSFP
+ module is below low warning level. This value is from DOM supporting QSFP
+ module.

### 10.57 pm_info : rx_power_low_alarm

**Type**: _string_

+ Flag to indicate received average optical power is below low alarm level. This
value is from DOM supporting SFP
+ module.

### 10.58 pm_info : rx_power_high_alarm

**Type**: _string_

+ Flag to indicate received average optical power exceeds high alarm level. This
value is from DOM supporting SFP
+ module.

### 10.59 pm_info : vendor_serial_number

**Type**: _string_

The vendor's module serial number.

### 10.60 pm_info : tx3_bias_low_alarm

**Type**: _string_

+ Flag to indicate TX bias current in channel 3 of QSFP
+ module is below low alarm level. This value is from DOM supporting QSFP
+ module.

### 10.61 pm_info : vcc_low_alarm_threshold

**Type**: _real_

+ Alarm low threshold value of internal supply voltage, ranging from 0 to 6.55,
in units of Volts. This is a factory preset value in DOM supporting SFP
+ module.

### 10.62 pm_info : tx2_bias_high_warning

**Type**: _string_

+ Flag to indicate TX bias current in channel 2 of QSFP
+ module exceeds high warning level. This value is from DOM supporting QSFP
+ module.

### 10.63 pm_info : cable_length

**Type**: _string_

The length of the cable in meters. This is only applicable to transceivers with
built-in cable or the maximum cable length for a transceiver restricted by
length.

### 10.64 pm_info : supported_speeds

**Type**: _string_

The list of speeds, in megabits per second, supported by this pluggable module.

### 10.65 pm_info : power_mode

**Type**: _string_

The power mode for the pluggable module. The possible values are "low" or
"high". This typically applies to QSFP pluggable modules.

### 10.66 pm_info : tx1_bias_high_warning

**Type**: _string_

+ Flag to indicate TX bias current in channel 1 of QSFP
+ module exceeds high warning level. This value is from DOM supporting QSFP
+ module.

### 10.67 pm_info : tx4_bias_high_alarm

**Type**: _string_

+ Flag to indicate TX bias current in channel 4 of QSFP
+ module exceeds high alarm level. This value is from DOM supporting QSFP
+ module.

### 10.68 pm_info : connector

**Type**: _string_

The type of pluggable module connector inserted into the socket. The possible
values are "absent", "unknown", "SFP_RJ45", "SFP_SX", "SFP_LX", "SFP_CX",
"SFP_SR", "SFP_LR", "SFP_LRM", "SFP_DAC", "SFP_FC", "QSFP_CR4", "QSFP_SR4" and
"QSFP_LR4".

### 10.69 pm_info : temperature_low_warning_threshold

**Type**: _real_

+ Warning low threshold value of internal temperature, ranging from -128 to 128,
in units of Celsius. This is a factory preset value in DOM supporting SFP
+ module.

### 10.70 pm_info : rx1_power

**Type**: _real_

+ Transceiver received average optical power in channel 1 of QSFP
+ module. The valid value range is 0 to 6.5535, in units of milliwatts. This
value is from DOM supporting QSFP
+ module.

### 10.71 pm_info : rx2_power_high_alarm

**Type**: _string_

+ Flag to indicate received average optical power in channel 2 of QSFP
+ module exceeds high alarm level. This value is from DOM supporting QSFP
+ module.

### 10.72 pm_info : tx_power_high_alarm

**Type**: _string_

+ Flag to indicate output power exceeds high alarm level. This value is from DOM
supporting SFP
+ module.

### 10.73 pm_info : rx3_power_low_warning

**Type**: _string_

+ Flag to indicate received average optical power in channel 3 of QSFP
+ module is below low warning level. This value is from DOM supporting QSFP
+ module.

### 10.74 pm_info : tx_bias_low_warning

**Type**: _string_

+ Flag to indicate TX bias current is below low warning level. This value is
from DOM supporting SFP
+ module.

### 10.75 pm_info : temperature_high_alarm

**Type**: _string_

+ Flag to indicate internal temperature exceeds high alarm level. This value is
from DOM supporting SFP
+ module.

### 10.76 pm_info : rx1_power_low_warning

**Type**: _string_

+ Flag to indicate received average optical power in channel 1 of QSFP
+ module is below low warning level. This value is from DOM supporting QSFP
+ module.

### 10.77 pm_info : rx_power_high_warning_threshold

**Type**: _real_

+ Warning high threshold value of received average optical power. The valid
value range is 0 to 6.5535, in units of milliwatts. This is a factory preset
value in DOM supporting SFP
+ module.

### 10.78 pm_info : rx2_power_high_warning

**Type**: _string_

+ Flag to indicate received average optical power in channel 2 of QSFP
+ module exceeds high warning level. This value is from DOM supporting QSFP
+ module.

### 10.79 pm_info : tx1_bias_high_alarm

**Type**: _string_

+ Flag to indicate TX bias current in channel 1 of QSFP
+ module exceeds high alarm level. This value is from DOM supporting QSFP
+ module.

### 10.80 pm_info : tx_bias_low_warning_threshold

**Type**: _real_

+ Warning low threshold value of TX bias current, ranging from 0 to 131, in
units of milliamps. This is a factory preset value in DOM supporting SFP
+ module.

### 10.81 pm_info : tx_power_low_warning_threshold

**Type**: _real_

+ Warning low threshold value of output power, ranging from 0 to 6.5535, in
units of milliwatts. This is a factory preset value in DOM supporting SFP
+ module.

### 10.82 pm_info : rx_power_low_alarm_threshold

**Type**: _real_

+ Alarm low threshold value of received average optical power. The valid value
range is 0 to 6.5535, in units of milliwatts. This is a factory preset value in
DOM supporting SFP
+ module.

### 10.83 pm_info : tx3_bias

**Type**: _real_

+ Transceiver TX bias current in channel 3 of QSFP
+ module, ranging from 0 to 131, in units of milliamps. This value is from DOM
supporting QSFP
+ module.

### 10.84 pm_info : vendor_part_number

**Type**: _string_

The vendor's module part number.

### 10.85 pm_info : temperature_high_warning_threshold

**Type**: _real_

+ Warning high threshold value of internal temperature, ranging from -128 to
128, in units of Celsius. This is a factory preset value in DOM supporting SFP
+ module.

### 10.86 pm_info : tx_bias

**Type**: _real_

+ Transceiver TX bias current, ranging from 0 to 131, in units of milliamps.
This value is from DOM supporting SFP
+ module.

### 10.87 pm_info : tx_bias_high_alarm

**Type**: _string_

+ Flag to indicate TX bias current exceeds high alarm level. This value is from
DOM supporting SFP
+ module.

### 10.88 pm_info : temperature_high_warning

**Type**: _string_

+ Flag to indicate internal temperature exceeds high warning level. This value
is from DOM supporting SFP
+ module.

### 10.89 pm_info : tx4_bias_low_alarm

**Type**: _string_

+ Flag to indicate TX bias current in channel 4 of QSFP
+ module is below low alarm level. This value is from DOM supporting QSFP
+ module.

### 10.90 pm_info : rx2_power

**Type**: _real_

+ Transceiver received average optical power in channel 2 of QSFP
+ module. The valid value range is 0 to 6.5535, in units of milliwatts. This
value is from DOM supporting QSFP
+ module.

### 10.91 pm_info : tx_power_low_alarm

**Type**: _string_

+ Flag to indicate output power is below low alarm level. This value is from DOM
supporting SFP
+ module.

### 10.92 pm_info : vcc_low_warning_threshold

**Type**: _real_

+ Warning low threshold value of internal supply voltage, ranging from 0 to
6.55, in units of Volts. This is a factory preset value in DOM supporting SFP
+ module.

### 10.93 pm_info : rx2_power_low_warning

**Type**: _string_

+ Flag to indicate received average optical power in channel 2 of QSFP
+ module is below low warning level. This value is from DOM supporting QSFP
+ module.

### 10.94 pm_info : tx_power

**Type**: _real_

+ Transceiver output power, ranging from 0 to 6.5535, in units of milliwatts.
This value is from DOM supporting SFP
+ module.

### 10.95 pm_info : tx3_bias_high_warning

**Type**: _string_

+ Flag to indicate TX bias current in channel 3 of QSFP
+ module exceeds high warning level. This value is from DOM supporting QSFP
+ module.

### 10.96 pm_info : tx_bias_high_alarm_threshold

**Type**: _real_

+ Alarm high threshold value of TX bias current, ranging from 0 to 131, in units
of milliamps. This is a factory preset value in DOM supporting SFP
+ module.

### 10.97 pm_info : tx4_bias_low_warning

**Type**: _string_

+ Flag to indicate TX bias current in channel 4 of QSFP
+ module is below low warning level. This value is from DOM supporting QSFP
+ module.

### 10.98 pm_info : vendor_name

**Type**: _string_

The name of the vendor of the module.

## 11. Tunnel Options

These options apply to interfaces with [type](interface.html#type) of `vxlan`.

Each tunnel must be uniquely identified by the combination of
[type](interface.html#type), [remote_ip](interface.html#options-remote-ip),
[local_ip](interface.html#options-local-ip), and [in_key](interface.html#options-in-key).
If two ports are defined that are the same except one has an optional identifier
and the other does not, the more specific one is matched first.
[in_key](interface.html#options-in-key) is considered more specific than
[local_ip](interface.html#options-local-ip) if a port defines one and another port
defines the other.

### 11.1 options

**Type**: _string->string_

### 11.2 options : key

**Type**: _string_

Optional.  Shorthand to set `in_key` and `out_key` at the same time.

### 11.3 options : local_ip

**Type**: _string_

The tunnel destination IP that received packets must match.

+ An IPv4 address (not a DNS name), e.g. `192.168.12.3`.

### 11.4 options : tos

**Type**: _string_

Optional.  The value of the ToS bits to be set on the encapsulating packet.  ToS
is interpreted as DSCP and ECN bits, ECN part must be zero.  It may also be the
word `inherit`, in which case the ToS will be copied from the inner packet if it
is IPv4 or IPv6 (otherwise it will be 0).  The ECN fields are always inherited.
Default is 0.

### 11.5 options : out_key

**Type**: _string_

Optional.  The key to be set on outgoing packets, one of:

+ `0`.  Packets sent through the tunnel will have no key. This is equivalent to
specifying no [out_key](interface.html#options-out-key) at all.
+ A 32-bit (for GRE).  The tunnel sends packets only with the specified key.
+ A positive 24-bit (VXLAN). The tunnel sends packets only with the specified
key.

### 11.6 options : in_key

**Type**: _string_

Optional.  The key that received packets must contain, one of:

+ `0`.  The tunnel receives packets with no key or with a key of 0.  This is
equivalent to specifying no [in_key](interface.html#options-in-key) at all.
+ A 32-bit (for GRE).  The tunnel receives only packets with the specified key.
+ A positive 24-bit (VXLAN). The tunnel receives only packets with the specified
key.

### 11.7 options : df_default

**Type**: _boolean_

Optional.  If enabled, the Don't Fragment bit will be set on tunnel outer
headers to allow path MTU discovery. Default is enabled; set to `false` to
disable.

### 11.8 options : ttl

**Type**: _string_

Optional.  The TTL to be set on the encapsulating packet.  It may also be the
word `inherit`, in which case the TTL will be copied from the inner packet if it
is IPv4 or IPv6 (otherwise it will be the system default, typically 64).
Default is the system default TTL.

### 11.9 options : remote_ip

**Type**: _string_

Required.  The remote tunnel endpoint, one of:

+ An IPv4 address (not a DNS name), e.g. `192.168.0.123`. Only unicast endpoints
are supported.

### 11.10 Tunnel Options: ipsec_gre only

#### 11.10.1 options : psk

**Type**: _string_

Required for pre-shared key authentication.  Specifies a pre-shared key for
authentication that must be identical on both sides of the tunnel.

#### 11.10.2 options : private_key

**Type**: _string_

Optional for certificate authentication.  The name of a PEM file containing the
private key associated with `certificate`. If `certificate` contains the private
key, this option may be omitted.

#### 11.10.3 options : certificate

**Type**: _string_

Required for certificate authentication.  The name of a PEM file containing a
certificate that will be presented to the peer during authentication.

#### 11.10.4 options : peer_cert

**Type**: _string_

Required for certificate authentication.  A string containing the peer's
certificate in PEM format.  Additionally the host's certificate must be
specified with the `certificate` option.

