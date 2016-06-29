# System

![System_table_img](http://www.plantuml.com/plantuml/img/0Te39Vn0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKLzGSczcQMnb2cDiONDp855lKmfZR65pSo1JUNDqPMqAOsnXStCWSqPiRtSAVGfqRsTbT6XbSY1x2cDiONDp85DrOdDvStHbRGfZR65pSo12ScbaPsKAOsnXStCWH65bRMzk2cDiONDp855lKrz4KqDGNqrXS5z5RdHoUGfZR65pSo1JUNDiRsTVKcLjRtHb2cDiONDp8453J0fZR65pSo1JKqmAOsnXStCWJM5kOMTbSWfZR65pSo1HRrDVGqzJNqrXS5z5RdHoUGfZR65pSo1MKaOAOsnXStCWKc5aQNLpNrDbSdPbSWfz2bDvStHbRI0jP2q-859XP6brSrzJPN9sPN8AKtbpT6Lj82raBJuWLb962bDvStHbRI0jTIq-855VK79lPcbiPGfJUNDqPMqWBMGjFY1DOMvXPsLo2bDvStHbRI0jP2q-85DvSsnlPrzIPMrlT6KAKtbpT6Lj82raBJuWKtLYStbpT6Lj2bDvStHbRI0jTIq-855lKmfJUNDqPMqWBMGjFY12ScbaPsKAKtbpT6Lj82raBJuWGKDC2bDvStHbRI0jP2q-84HXPMrlRWfJUNDqPMqWBNKjFY1pHcnlTmfJUNDqPMqWBMGjFY1HRrDVGqzJNqrXS5z5RdHoUGfJUNDqPMqWBMGjFY1JKqmAKtbpT6Lj82raBJuWKMzJNqHJGr1VJM5mNqLkT79v2bDrOdDvStHbRI0jMsXfP6HbRbqj849oQMHdPGf2ScbaPsKWBLjeQMHaPMvTBI14OMLjRsuAH65bRMzk82rRQ6baP6LkNIqWKtLYStbpT6Lj2b5lKrz4KqDGNqrXS5z5RdHoUI0jMsXfP6HbRbqj85DvSsnlPrzIPMrlT6KAKtbpR6zdNr9bRMzqPI0jMsXfP6HbRbqj8453J0f1GqmWBLjeQMHaPMvTBI1HRrDVH5D3K5zDON1VHMvqSdaAKrDC82rRQ6baP6LkNIqWJM5kOMTbSWfDOMvXPsLo82rRQ6baP6LkNIqWKMzJNqDFKrzDON1VHMvqSdaAKMzJNqDFKrzDON1VHMvqSdaWBLjeQMHaPMvTBI1JKqmAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Configuration for an OpenSwitch system. There must be exactly one record in the
[System](system.html) table.

## 1. Version Reporting group

These columns report the types and versions of the hardware and software running
OpenSwitch.  We recommend in general that software should test whether specific
features are supported instead of relying on version number checks.  These
values are primarily intended for reporting to human administrators.

### 1.1 db_version column

The database schema version number in the form `_major_._minor_._tweak_`, e.g.
`1.2.3`.  Whenever the database schema is changed in a non-backward compatible
way (e.g. deleting a column or a table), _major_ is incremented.  When the
database schema is changed in a backward compatible way (e.g. adding a new
column), _minor_ is incremented.  When the database schema is changed
cosmetically (e.g. reindenting its syntax), _tweak_ is incremented.

The schema version is part of the database schema, so it can also be retrieved
by fetching the schema using the Open vSwitch database protocol.

### 1.2 switch_version column

The OpenSwitch version number, e.g. `0.1.0`.

### 1.3 software_info column

### 1.4 software_info : boot_loader_version key

### 1.5 software_info : diag_version key

### 1.6 software_info : os_name key

This column is used for the software info. The value of the key 'os_name' will
identify the operating system, without a version component, and suitable for
presentation to the user. If not set, defaults to `os_name=OpenSwitch`. Example:
`os_name=Fedora` or `os_name="Debian GNU/Linux"`.  This is equivalent of `NAME`
variable of the `/etc/os-release` file.  Please refer to
`http://www.freedesktop.org/software/systemd/man/os-release.html` for more
detailed information.

### 1.7 software_info : bios_vendor key

### 1.8 software_info : install_env_version key

### 1.9 software_info : bios_release_date key

### 1.10 software_info : bios_version key

### 1.11 software_info : install_env key

### 1.12 software_info : boot_loader key

## 2. Configuration group

### 2.1 dns_servers column

### 2.2 asset_tag_number column

### 2.3 bridges column

Set of bridges.

### 2.4 subsystems column

### 2.5 hostname column

### 2.6 domain_name column

Domain name as configured by the user.

### 2.7 vrfs column

### 2.8 router_id column

### 2.9 router_id : router_id_val key

The system global router identifier. Any routing protocol may pick up this as
router id, if it doesn't have a specific one configured. The router-ID may be an
IPv4 address of the router. It can be any arbitrary 32bit number. However it
MUST be non-zero and unique within the entire Autonomus System domain.

### 2.10 router_id : router_id_static key

This determines whether the system global router-ID is configured statically or
selected by Routing Manager dynamically. The default value is false.

### 2.11 management_mac column

Ethernet MAC address for the management interface port for this system.

### 2.12 ssl column

### 2.13 daemons column

### 2.14 snmp_communities column

Community strings to be used by the system when communicating over
SNMPv1/SNMPv2c.

### 2.15 system_mac column

Ethernet MAC address available to use anywhere a non-unique MAC is needed.

### 2.16 sflow column

sFlow(R) configuration.

### 2.17 other_config column

### 2.18 other_config : banner_exec key

Banner to be displayed on CLI login. Maximum length 4095.

No banner by default.

### 2.19 other_config : internal_vlan_policy key

This key indicates order of assignment of internal VLAN ID (ascending or
descending).

Default option is ascending order.

### 2.20 other_config : cli_session_timeout key

This key specifies cli idle session timeout in minutes. Set this value to 0 to
disable session timeout.

Default value is 30.

### 2.21 other_config : min_internal_vlan key

This key specifies a lower bound of the VLAN range, which is being used for
internal system purposes.

Default value is 1024.

### 2.22 other_config : acl_log_timer_interval key

This key specifies the interval in seconds of the ACL logging timer.

Default value is 300 seconds.

### 2.23 other_config : max_internal_vlan key

This key specifies an upper bound of the VLAN range, which is being used for
internal system purposes.

Default value is 4094.

### 2.24 other_config : banner key

Banner to be displayed on CLI start. Maximum length 4095.

No banner by default.

### 2.25 other_config : stats-update-interval key

Update interval for the statistics, in milliseconds. This option will affect the
update of `statistics`, `DHCP-Relay Statistics` columns in the `Port` table,
`statistics` column in the `Interface` table.

Default value is 5000 ms.

### 2.26 Syslog Remotes Configurations group

#### 2.26.1 syslog_remotes column

List of syslog servers to which syslog messages will be forwarded.
[Syslog_Remote](syslog_remote.html)

### 2.27 LACP Configurations group

#### 2.27.1 lacp_config column

#### 2.27.2 lacp_config : lacp-system-id key

The LACP system ID of this [Bridge](bridge.html).  The system ID of a LACP bond is
used to identify itself to its partners.  Must be a nonzero MAC address.
Defaults to the bridge Ethernet address if unset.

#### 2.27.3 lacp_config : lacp-system-priority key

The LACP system priority of this [Bridge](bridge.html).  In LACP negotiations, link
status decisions are made by the system with the numerically lower priority.
Defaults to 65534.

### 2.28 TFTP Server Configurations group

#### 2.28.1 other_config column

#### 2.28.2 other_config : tftp_server_enable key

Set this value to `true` to enable TFTP server and set to `false` to disable it.
If not set, TFTP server would be enabled.

#### 2.28.3 other_config : tftp_server_secure key

Set this value to `true` to enable TFTP secure mode and set to `false` to
disable it. If not set, TFTP secure mode would be enabled. This config is valid
only if TFTP server is enabled.

### 2.29 SFTP Server Configurations group

#### 2.29.1 other_config column

#### 2.29.2 other_config : sftp_server_enable key

Set this value to `true` to enable SFTP server and to set to `false` to disable
it. If not set, SFTP server would be disabled by default.

### 2.30 Source Interface Selection Configurations group

#### 2.30.1 other_config column

#### 2.30.2 other_config : tftp_source key

Provides source interface or IP address for tftp client. If not present, regular
routing rules take place.

#### 2.30.3 other_config : protocols_source key

Overrides source interface or IP address for all the protocols that support it.
If not present, regular routing rules take place.

### 2.31 UDP Broadcast Forwarder Configurations group

#### 2.31.1 other_config column

#### 2.31.2 other_config : udp_bcast_forwarder_enabled key

Set this value to `true` to enable UDP-Broadcast-Forwarder functionality
globally and set it to `false` to disable it. UDP-Broadcast-Forwarder is
disabled by default. If the key is missing, the configuration is assumed to be
disabled. UDP-Broadcast-Forwarder port level configuration is present in
[UDP_Bcast_Forwarder_Server](udp_bcast_forwarder_server.html).

### 2.32 LLDP Configurations group

#### 2.32.1 other_config column

#### 2.32.2 other_config : lldp_tlv_port_desc_enable key

Set this value to `true` to enable transmission of LLDP Port Description TLV or
set it to `false` to disable transmitting it. Default is `enable`.

#### 2.32.3 other_config : lldp_enable key

Set this value to `true` to enable System level LLDP or to `false` to explicitly
disable it. Default is `disable`.

#### 2.32.4 other_config : lldp_tlv_sys_cap_enable key

Set this value to `true` to enable transmission of LLDP System Capabilities TLV
or set it to `false` to disable transmitting it. Default is `enable`.

#### 2.32.5 other_config : lldp_reinit key

The amount of time in seconds to wait before performing LLDP initialization on
any interface.

Default value is 2.

#### 2.32.6 other_config : lldp_tlv_port_vlan_enable key

Set this value to `true` to enable transmission of LLDP Port VLAN TLV or set it
to `false` to disable transmitting it. Default is `enable`.

#### 2.32.7 other_config : lldp_tx_interval key

The interval in seconds at which LLDP status updates are transmitted to
neighbors in seconds.

Default value is 30 sec.

#### 2.32.8 other_config : lldp_mgmt_addr key

LLDP Management IP Address to be sent in TLV.

#### 2.32.9 other_config : lldp_tlv_mgmt_addr_enable key

Set this value to `true` to enable transmission of LLDP Management Address TLV
or set it to `false` to disable transmitting it. Default is `enable`.

#### 2.32.10 other_config : lldp_hold key

The amount of time a receiving device should hold the information sent by your
device before discarding it. This variable is used as a multiplier of
lldp_tx_interval, to determine the value of TTL that is carried in LLDP frames.

Default value is 4.

#### 2.32.11 other_config : lldp_tlv_sys_name_enable key

Set this value to `true` to enable transmission of LLDP System Name TLV or set
it to `false` to disable transmitting it. Default is `enable`.

#### 2.32.12 other_config : lldp_tlv_sys_desc_enable key

Set this value to `true` to enable transmission of LLDP System Description TLV
or set it to `false` to disable transmitting it. Default is `enable`.

### 2.33 SNMP configuration group

#### 2.33.1 other_config column

#### 2.33.2 other_config : snmp_agent_port key

The port on which the SNMP agent listens for SNMP requests. The default port is
161.

#### 2.33.3 other_config : system_description key

This key represents the system description.

#### 2.33.4 other_config : system_location key

This key represents the system location.

#### 2.33.5 other_config : system_contact key

This key represents the system contact.

## 3. QoS configuration group

Specifies QoS (Quality of Service) configuration options that are global or are
the configured default to use if no per-port override has been specified.

### 3.1 qos column

Specifies the schedule profile for ports that do not specify their own schedule
profile (see [Port](port.html) qos column). When missing, the [QoS](qos.html) row with
[hw_default](qos.html#hw-default-column) true will be used.

### 3.2 qos_cos_map_entries column

Contains references to each entry in the global COS map used by port trust mode
COS. (see [QoS_DSCP_Map_Entry](qos_dscp_map_entry.html))

### 3.3 qos_config column

### 3.4 qos_config : qos_trust key

Specifies the QoS Trust Mode for ports that do not specify their own Trust Mode
(see [Port](port.html) qos_config column).

`none` - no fields are inspected on arriving packets.  The initial local-
priority and color meta-data values are taken from PCP 0 entry of the COS Map
table (see [QoS_COS_Map_Entry](qos_cos_map_entry.html)).

`cos` - will use the PCP of the outermost 802.1 VLAN tag to index the COS Map
entry to initialize the local-priority and color meta-data values of the packet.
For untagged packets, the initial local-priority and color meta-data values are
taken from PCP 0 entry of the COS Map table (see
[QoS_COS_Map_Entry](qos_cos_map_entry.html)).

`dscp` - will use the DSCP value of IP packets to index the DSCP Map entry to
initialize the local-priority and color meta-data values of the packet.  For
non-IP packets, what meta-data values are assigned is hardware dependent.

If the key is not specified, then the system will use 'none'.

### 3.5 q_profile column

Specifies the queue profile for ports that do not specify their own queue
profile (see [Port](port.html) q_profile column). When missing, the
[Q_Profile](q_profile.html) row with [hw_default](q_profile.html#hw-default-column) true will be
used.

### 3.6 qos_dscp_map_entries column

Contains references to each entry in the global DSCP map used by port trust mode
DSCP. (see [QoS_DSCP_Map_Entry](qos_dscp_map_entry.html))

## 4. NTP configuration group

Specifies the NTP global configuration.

### 4.1 ntp_config column

### 4.2 ntp_config : authentication_enable key

Determines whether NTP Authentication is enabled in the system. Default is
false.

## 5. Status group

### 5.1 next_cfg column

Sequence number for client to increment.  When a client modifies any part of the
database configuration and wishes to wait for OpenSwitch to finish applying the
changes, it may increment this sequence number.

### 5.2 ntp_status column

This column holds the global status information for NTP.

### 5.3 ntp_status : uptime key

Time in hours since the system was last rebooted.

### 5.4 next_hw column

Sequence number to indicate that a change has occurred in the hardware
configuration (e.g., a subsystem has been added or removed).

### 5.5 cur_hw column

Sequence number that indicates the current change level for the h/w
configuration. When [cur_hw](system.html#cur-hw-column) is the same as
[next_hw](system.html#next-hw-column), then all platform daemon processing has completed in
response to the hardware addition or removal. This is not used for transceiver
pluggable module insertion/removal.

### 5.6 boot_time column

Boot time of the machine, represented in seconds since 1970-01-01 00:00:00 UTC.
OVSDB integers are 64 bit, which means it will take some time until we roll
over.

### 5.7 mgmt_intf_status column

This column holds the status of the management interface IP parameters. This
column contains key-value pairs that report the mangement interface IP
attributes like IP address, subnet, default gateway, primary and secondary name
server. These values are either statically configured by the user or populated
by the DHCP client. The keys of this column is same as that of mgmt_intf column.

### 5.8 mgmt_intf_status : dhcp_domain_name key

The domain name as it was received from dhcp.

### 5.9 mgmt_intf_status : hostname key

Hostname the system is configured with. Hostname can be configured through CLI,
or specified in DHCP messages. If none of these are available, it defaults to
"switch".

### 5.10 mgmt_intf_status : domain_name key

This key contains the domain name configured for the system. It can be
configured by the user or through dhcp messages. If none of these are present
the key itself ceases to exist.

### 5.11 mgmt_intf_status : dhcp_hostname key

Holds hostname configured by dhcp client.

### 5.12 status column

System level status information per service like `LLDP`, etc.

### 5.13 cur_cfg column

Sequence number that OpenSwitch sets to the current value of
[next_cfg](system.html#next-cfg-column) after it finishes applying a set of configuration
changes.

### 5.14 LLDP Status Info group

#### 5.14.1 status column

System level status information per service like `LLDP`, etc.

#### 5.14.2 status : lldp_last_clear_counters_performed key

Last time when clear statistic counters was perfomed.

#### 5.14.3 status : lldp_local_system_name key

System Name currently being advertised by LLDP.

#### 5.14.4 status : lldp_local_system_desc key

System Description info currently being advertised by LLDP.

#### 5.14.5 status : lldp_local_system_cap key

System Capabilities currently being advertised by LLDP.

#### 5.14.6 status : lldp_num_clear_counters_requested key

Number of times clear statistic counters was requested by user.

#### 5.14.7 status : lldp_last_table_change_time key

Last time when LLDP neighbor table was changed.

#### 5.14.8 status : lldp_last_clear_table_performed key

Last time when neighbor table was cleared.

#### 5.14.9 status : lldp_num_clear_table_requested key

Number of times clearing of neighbor table was requested by user.

#### 5.14.10 status : lldp_local_mgmt_ip key

Management IP Address currently being advertised by LLDP.

## 6. BroadView configuration group

The parameters in this group are used to configure BroadView agent. Parameter
enabled is used to enable/disable BroadView. Agent sends asynch reports to the
application at client_ip and client_port. Parameter agent_port is the port
number on which agent listens for client connections. The communication on agent
port is of request - response style.

### 6.1 broadview_config column

### 6.2 broadview_config : client_ip key

Specifies BroadView client ip address. This is the IP that BroadView Agent tries
to reach out to send async reports. If the value is not configured then default
is 127.0.0.1.

### 6.3 broadview_config : enabled key

Specifies whether the BroadView feature is enabled on the system. False, if the
value is not present.

### 6.4 broadview_config : client_port key

Specifies BroadView client tcp port number. This is the port number along with
client_ip that BroadView agent shoud try to reach out to send async reports. If
no value is set, the default is 9070.

### 6.5 broadview_config : agent_port key

Specifies BroadView agent tcp port number. Agent listens on this port for client
connections. If no value is set, the default is 8080.

## 7. Database Configuration group

These columns primarily configure the OpenSwitch database (`ovsdb-server`), not
the OpenSwitch switch (`pswitchd`).  The OVSDB database also uses the
[ssl](system.html#ssl-column) settings.

The OpenSwitch switch does read the database configuration to determine remote
IP addresses to which in-band control should apply.

### 7.1 manager_options column

Database clients to which the OpenSwitch database server should connect or to
which it should listen, along with options for how these connection should be
configured.  See the [Manager](manager.html) table for more information.

### 7.2 auto_provisioning_status column

### 7.3 auto_provisioning_status : url key

Specifies the URL that was used to fetch auto-provisioning script. Would not be
present if auto-provisioning was not performed.

### 7.4 auto_provisioning_status : performed key

Specifies whether auto-provisioning was performed. False if not specified.

### 7.5 acls column

List of all Access Control Lists (ACLs) in the system.  The existence of the
list is not an indication that it has been applied.

### 7.6 mgmt_intf column

This column is a map of string-string pairs Management interface column contains
the attributes of management interface. The keys are name, mode, ip, subnet
mask, default gateway, dns server IPv4 addresses. This column holds values that
are configured by the user.

### 7.7 mgmt_intf : name key

The value for this key is a valid interface name that is to be configured as
management interface

### 7.8 mgmt_intf : default_gateway key

The value for this key is default gateway IPv4 address.

### 7.9 mgmt_intf : ip key

The value for this key is interface IPv4 address of the management interface.

### 7.10 mgmt_intf : default_gateway_v6 key

The value for this key is default gateway IPv6 address

### 7.11 mgmt_intf : subnet_mask key

The value for this key is subnet mask of the interface IP of management
interface in CIDR format. The valid value range is 1 to 31.

### 7.12 mgmt_intf : dns_server_2 key

The value for this key is Secondary nameserver IPv4 address.

### 7.13 mgmt_intf : mode key

The value is static or dhcp based on the mode in which the management ip is to
be obtained. Default value is dhcp.

### 7.14 mgmt_intf : ipv6 key

The value for this key is IPv6 address of the management interface. Possible
value X:X::X:X/M.

### 7.15 mgmt_intf : dns_server_1 key

The value for this key is Primary nameserver IPv4 address.

### 7.16 radius_servers column

Specifies radius servers configuration. See the [Radius_Server](radius_server.html)
table for more information.

### 7.17 aaa column

### 7.18 aaa : radius_auth key

Specifies encoding to be used for the user password for radius based
authentication. By default `pap` is used.

### 7.19 aaa : fallback key

This column used for AAA feature. The valid values for the key 'fallback' are
true or false based on the user request for authentication. If fallback=true,
fall to local authentication if radius server is not reachable.

### 7.20 aaa : radius key

This column used for AAA feature. The valid values for the key 'radius' are true
or false based on the user request for authentication. If radius=true, radius
based authentication is enabled. By default authentication is local.

### 7.21 aaa : ssh_publickeyauthentication_enable key

Controls whether ssh public key authentication is enabled. Default is true.

### 7.22 aaa : ssh_passkeyauthentication_enable key

Controls whether ssh password based authentication is enabled. Default is true.

## 8. Statistics group

The `statistics` column contains key-value pairs that report statistics about a
system running OpenSwitch.  These are updated periodically (by default, every 5
seconds).  Key-value pairs that cannot be determined or that do not apply to a
platform are omitted.

### 8.1 statistics column

### 8.2 statistics : load_average key

A comma-separated list of three floating-point numbers, representing the system
load average over the last 1, 5, and 15 minutes, respectively.

### 8.3 statistics : process_NAME key

One such key-value pair, with `NAME` replaced by a process name, will exist for
each running OpenSwitch daemon process, with _name_ replaced by the daemon's
name (e.g. `process_sysd`).  The value is a comma-separated list of integers.
The integers represent the following, with memory measured in kilobytes and
durations in milliseconds:

1. The process's virtual memory size.
1. The process's resident set size.
1. The amount of user and system CPU time consumed by the process.
1. The number of times that the process has crashed and been automatically
restarted by the monitor.
1. The duration since the process was started.
1. The duration for which the process has been running.

The interpretation of some of these values depends on whether the process was
started with the `--monitor`.  If it was not, then the crash count will always
be 0 and the two durations will always be the same.  If `--monitor` was given,
then the crash count may be positive; if it is, the latter duration is the
amount of time since the most recent crash and restart.

There will be one key-value pair for each file in OpenSwitch's ``run directory''
(usually `/var/run/openvswitch`) whose name ends in `.pid`, whose contents are a
process ID, and which is locked by a running process.  The _name_ is taken from
the pidfile's name.

### 8.4 statistics : cpu key

Number of CPU processors, threads, or cores currently online and available to
the operating system, as an integer.  This may be less than the number
installed, if some are not online or if they are not available to the operating
system.

### 8.5 statistics : file_systems key

A space-separated list of information on local, writable file systems.  Each
item in the list describes one file system and consists in turn of a comma-
separated list of the following:

1. Mount point, e.g. `/` or `/var/log`. Any spaces or commas in the mount point
are replaced by underscores.
1. Total size, in kilobytes, as an integer.
1. Amount of storage in use, in kilobytes, as an integer.

This key-value pair is omitted if there are no local, writable file systems or
if OpenSwitch cannot obtain the needed information.

### 8.6 statistics : memory key

A comma-separated list of integers, each of which represents a quantity of
memory in kilobytes that describes the operating system.  In respective order,
these values are:

1. Total amount of RAM allocated to the OS.
1. RAM allocated to the OS that is in use.
1. RAM that can be flushed out to disk or otherwise discarded if that space is
needed for another purpose.  This number is necessarily less than or equal to
the previous value.
1. Total disk space allocated for swap.
1. Swap space currently in use.

### 8.7 other_config column

### 8.8 other_config : enable-statistics key

Statistics are disabled by default to avoid overhead in the common case when
statistics gathering is not useful.  Set this value to `true` to enable
populating the [statistics](system.html#statistics-column) column or to `false` to
explicitly disable it.

### 8.9 NTP Statistics group

#### 8.9.1 ntp_statistics column

#### 8.9.2 ntp_statistics : ntp_pkts_declined key

Number of packets denied access for any reason.

#### 8.9.3 ntp_statistics : ntp_pkts_with_older_version key

Number of packets matching the previous NTP version.

#### 8.9.4 ntp_statistics : ntp_pkts_with_auth_failed key

Number of packets not verified as authentic.

#### 8.9.5 ntp_statistics : ntp_pkts_with_bad_length_or_format key

Number of packets with invalid length, format or port number.

#### 8.9.6 ntp_statistics : ntp_pkts_restricted key

Number of packets restricted for any reason.

#### 8.9.7 ntp_statistics : ntp_pkts_rate_limited key

Number of packets discarded due to rate limitation.

#### 8.9.8 ntp_statistics : ntp_pkts_with_current_version key

Number of packets matching the current NTP version.

#### 8.9.9 ntp_statistics : ntp_pkts_kod_responses key

Number of KoD packets from the server.

#### 8.9.10 ntp_statistics : ntp_pkts_received key

Total number of packets received.

### 8.10 LLDP Statistics group

#### 8.10.1 lldp_statistics column

#### 8.10.2 lldp_statistics : lldp_table_inserts key

Number of neighbor entries inserted to LLDP neighbor table. Default is 0.

#### 8.10.3 lldp_statistics : lldp_table_ageouts key

Number of times neighbor info was deleted from LLDP neighbor table because of
the TTL timer associated with a neighbor has expired. Default is 0.

#### 8.10.4 lldp_statistics : lldp_table_drops key

Number of neighbor entries that could not be added to LLDP neighbor table and
dropped. Default is 0.

#### 8.10.5 lldp_statistics : lldp_table_deletes key

Number of neighbor entries deleted from LLDP neighbor table. Default is 0.

## 9. ECMP configuration group

Specifies the various ECMP (Equal Cost Multi-Path) configuration options.

### 9.1 ecmp_config column

### 9.2 ecmp_config : resilient_hash_enabled key

Determines whether ECMP hashing preserves traffic flows when ECMP group
membership changes. Default is true.

### 9.3 ecmp_config : enabled key

Determines whether ECMP is enabled in the system. Default is true.

### 9.4 ecmp_config : hash_dstport_enabled key

Determines whether destination TCP/UDP port participates in ECMP hash
calculation. Default is true.

### 9.5 ecmp_config : hash_srcport_enabled key

Determines whether source TCP/UDP port participates in ECMP hash calculation.
Default is true.

### 9.6 ecmp_config : hash_srcip_enabled key

Determines whether source IP participates in ECMP hash calculation. Default is
true.

### 9.7 ecmp_config : hash_dstip_enabled key

Determines whether destination IP participates in ECMP hash calculation. Default
is true.

## 10. DHCP Configurations group

### 10.1 dhcp_config column

### 10.2 dhcp_config : v4relay_option82_remote_id key

Specifies the remote ID suboption that the switch uses in Option 82 fields added
or appended to DHCP client packets. The type of remote ID defines DHCP policy
areas in the client requests sent to the DHCP server.

`ip` - Specifies the IP address of the interface on which the client DHCP packet
enters the switch.

`mac` - Specifies the router's MAC address. (The MAC address used is the same
MAC address that is assigned to all interfaces configured on the routing
switch.)

If the key is not specified, configuration is assumed to be "mac".

### 10.3 dhcp_config : v6relay_option79_enabled key

Set this value to `true` to enable the DHCPv6-Relay Option 79 and set it to
`false` otherwise. This configuration is disabled by default.

### 10.4 dhcp_config : v4relay_option82_policy key

Specifies the forwarding policy of DHCP-Relay Option 82.

`drop` - Drop an inbound dhcp-client request with an Option 82 field already
appended. If no Option 82 fields are present, drop causes the router to add an
Option 82 field to dhcp request and forward.

`keep` - If the relay agent receives a client request that already has one or
more Option 82 fields, keep causes the relay agent to retain such fields and
forward the request without adding another Option 82 field. But if the incoming
client request does not already have any Option 82 fields, the relay agent
appends an Option 82 field and forwards the dhcp request.

`replace` - Replace any existing Option 82 fields from downstream relay agents
(and/or the originating client) with an Option 82 field for the current relay
agent.

If the keys is missing, Option 82 configuration is assumed to be disabled.

### 10.5 dhcp_config : v4relay_hop_count_increment_disabled key

Set this value to `true` to disable the hop count increment in the relayed DHCP
requests and set it to `false` otherwise. This configuration is enabled by
default. If the key is missing, the configuration is assumed to be enabled.

### 10.6 dhcp_config : v4relay_disabled key

Set this value to `true` to disable DHCP-Relay functionality globally and set it
to `false` to enable it. DHCP-Relay is enabled by default. If the key is
missing, the configuration is assumed to be enabled. Though DHCP-Relay
configuration is enabled globally, the functionality is effective only after the
port level server configuration.

### 10.7 dhcp_config : v4relay_option82_enabled key

Set this value to `true` to enable the DHCP-Relay Option 82 and set it to
`false` otherwise. This configuration is disabled by default. If the key is
missing, the configuration is assumed to be disabled.

### 10.8 dhcp_config : v4relay_option82_validation_enabled key

Set this value to `true` to validate server response packets and set it to
`false` otherwise. This configuration is disabled by default. If the key is
missing, the configuration is assumed to be disabled. This configuration is
valid only for drop or replace dhcp-relay Option 82 policy.

### 10.9 dhcp_config : v6relay_enabled key

Set this value to `true` to enable DHCPv6-Relay functionality globally and set
it to `false` to disable it. This configuration is disabled by default. Though
DHCPv6-Relay configuration is enabled globally, the functionality is effective
only after the port level server configuration.

## 11. Ungrouped group

### 11.1 management_vrf column

## 12. ACL Limits group

### 12.1 other_info column

### 12.2 other_info : max_acls key

Total number of ACLs that may be configured in the system.

### 12.3 other_info : max_aces_per_acl key

Total number of ACL entries that may be configured in one ACL.

### 12.4 other_info : max_aces key

Total number of ACL entries that may be configured in the system.

## 13. COPP Statistics group

Contains key-value pairs that report overall Control Plane Policing statistics
regarding packets/bytes delivered to the management CPU or packets/bytes dropped
due to excessive rate.

### 13.1 copp_statistics column

### 13.2 copp_statistics : total_packets_dropped key

Total number of protocol packets dropped due to excessive rate.

### 13.3 copp_statistics : total_bytes_passed key

Total number of protocol bytes delivered to the management CPU.

### 13.4 copp_statistics : total_bytes_dropped key

Total number of protocol bytes dropped due to excessive rate.

### 13.5 copp_statistics : total_packets_passed key

Total number of protocol packets delivered to the management CPU.

## 14. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 14.1 external_ids column

### 14.2 other_config column

## 15. Logrotate configuration group

### 15.1 logrotate_config column

### 15.2 logrotate_config : maxsize key

Log size (in megabytes), which would trigger rotation. 10 megabytes if not
specified

### 15.3 logrotate_config : period key

The user configured period of logrotation. The possible values are
'hourly','daily','weekly'or 'monthly'. Default value is 'daily'

### 15.4 logrotate_config : target key

The user configured URI of the remote host .The valid value is
'tftp://A.B.C.D'.If not specified log files will be rotated locally.

## 16. Loop-protect Configuration group

Contains global configuration for the Loop-protect feature.

### 16.1 loop_protect_disable_timer column

This specifies the time in seconds for which the ports are to be disabled on
detecting a loop. Default value is `0` i.e the port is disabled indefinitely.

### 16.2 loop_protect_transmit_interval column

This specifies the time interval in seconds between successive transmissions of
loop-protect packets. Default value is `5` seconds.

## 17. QoS Status group

### 17.1 qos_status column

Key-value pairs that report the Quality of Service status in hardware for ports
that do not specify their own configuration.

### 17.2 qos_status : schedule_profile key

This key's value contains the [QoS](qos.html) [name](qos.html#name-column) that is currently
operating in hardware for ports that do not specify their own queue profile
configuration.

The value may be different than the name in [qos](system.html#qos-column) when that schedule
profile cannot be supported in hardware.  In this case, this key's value may be
the name of the last successfully configured system schedule profile.

### 17.3 qos_status : queue_profile key

This key's value contains the [Q_Profile](q_profile.html) [name](q_profile.html#name-column) that is
currently operating in hardware for ports that do not specify their own queue
profile configuration.

The value may be different than the name in [q_profile](system.html#q-profile-column) when
that queue profile cannot be supported in hardware.  In this case, this key's
value is the name of the last successfully configured system queue profile.

## 18. Information group

### 18.1 bufmon_info column

### 18.2 bufmon_info : cap_mode_current key

Specifies whether the system is capable of collecting current values of the
counters. False, if the value is not present.

### 18.3 bufmon_info : cap_snapshot_on_threshold_trigger key

Specifies whether the system is capable of freezing counters values on threshold
crossing. False, if the value is not present.

### 18.4 bufmon_info : cap_threshold_trigger_collection key

Specifies whether the system is capable of immediately collecting values on
threshold crossing. False, if the value is not present.

### 18.5 bufmon_info : cap_mode_peak key

Specifies whether the system is capable of collecting peak values of the
counters. False, if the value is not present.

### 18.6 bufmon_info : last_collection_timestamp key

Specifies the timestamp of the last collection in seconds from Jan 1, 1970.

## 19. Bufmon configuration group

### 19.1 bufmon_config column

### 19.2 bufmon_config : collection_period key

Specifies the period of collection in seconds. Five, if the value is not
present.

### 19.3 bufmon_config : threshold_trigger_rate_limit key

Specifies maximum number of trigger generated reports per minute. The limit will
be averaged and imposed on a per second basis. For example, value of 600 will
allow report every 100ms. If no value is set, the default is 60 i.e. once per
second.

### 19.4 bufmon_config : periodic_collection_enabled key

Specifies whether periodic collection of the counters is enabled. False, if the
value is not present.

### 19.5 bufmon_config : counters_mode key

Specifies whether counters should report their current values or peak values
since last collection.

### 19.6 bufmon_config : enabled key

Specifies whether the bufmon feature is enabled on the system. False, if the
value is not present.

### 19.7 bufmon_config : snapshot_on_threshold_trigger key

Specifies whether counters should be frozen when one of the thresholds is
crossed. True, if the value is not present.

### 19.8 bufmon_config : threshold_trigger_collection_enabled key

Specifies whether counters should be collected immediately when one of the
thresholds is crossed. True, if the value is not present.

