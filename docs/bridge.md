# Bridge

![Bridge_table_img](http://www.plantuml.com/plantuml/img/XP5D2eCm48NtSuhWgeLw0n6jgu8MgTAjf374qFoK9AMKqhlNe0jRWirovdkJDsyowx1nTodWXiaLCugYazOEjVWYg8tG2z3uYC3MeYelK9AWJRiJd0sE6KhL5gNf0ccUrb7vZoerumIBhdbmHuOm_GQOuBtX_MWh24t4kSoFQ_rQ6xVMhvgsxWejfLRTGOs1ABBwNyMDqIPCm9n07AUpSvWNy9L9kQnuR_2JHrZhj_oQ5N0D_aGBEMHKzVwu)

Configuration for a bridge within an [System](system.html).

A [Bridge](bridge.html) record represents an Ethernet switch with one or more
``ports,'' which are the [Port](port.html) records pointed to by the
[Bridge](bridge.html)'s [ports](bridge.html#ports-column) column. In the first release, only one
default bridge (bridge_normal) is supported

## 1. MSTP Status group

MSTP global status for all MSTIs.

### 1.1 status column

Key-value pairs that report bridge status.

### 1.2 status : mstp_config_digest key

The configuration digest for the MSTP bridge that is derived based on the VLAN
membership of MST instances.

## 2. Bridge Status group

Status information about bridges.

### 2.1 status column

Key-value pairs that report bridge status.

### 2.2 status : actual-mac-table-size key

Actual size of the mac table. If mac-table-size exceeds hardware capability,
then this field will show the real size used.

## 3. Core Features group

### 3.1 name column

Bridge identifier.  Should be alphanumeric and no more than about 8 bytes long.
Must be unique among the names of ports, interfaces, and bridges on a host.

### 3.2 mstp_instances column

MSTP configuration for individual instance.

### 3.3 vlans column

VLANs included in the bridge.

### 3.4 ports column

Ports included in the bridge.

### 3.5 mstp_common_instance column

MSTP configuration for CIST(Common Instance Spanning Tree).

## 4. Other Features group

### 4.1 mirrors column

[Mirror](mirror.html) references for sessions configured in this bridge.

### 4.2 other_config : hwaddr key

An Ethernet address in the form _xx_:_xx_:_xx_:_xx_:_xx_:_xx_ to set the
hardware address of the local port and influence the datapath ID.

### 4.3 other_config : mac-table-size key

The maximum number of MAC addresses to learn.  The default is currently 16K.
The value, if specified, is forced into a reasonable range, currently 10 to
256K.

### 4.4 other_config : mac-aging-time key

The maximum number of seconds to retain a MAC learning entry for which no
packets have been seen.  The default is currently 300 seconds (5 minutes).  The
value, if specified, is forced into a reasonable range, currently 15 to 3600
seconds.

A short MAC aging time allows a network to more quickly detect that a host is no
longer connected to a switch port.  However, it also makes it more likely that
packets will be flooded unnecessarily, when they are addressed to a connected
host that rarely transmits packets.  To reduce the incidence of unnecessary
flooding, use a MAC aging time longer than the maximum interval at which a host
will ordinarily transmit packets.

### 4.5 datapath_type column

Name of datapath provider.

## 5. MSTP Configurations group

MSTP global configurations for all MSTIs.

### 5.1 other_config : mstp_config_name key

Set this value to specify the MSTP configuration name. Default value is system
MAC address.

### 5.2 other_config : mstp_config_revision key

Set this value to specify the configuration revision number. Default value is 0.

### 5.3 mstp_enable column

Set this value to `true`, to enable MSTP. Default value is `false`.

