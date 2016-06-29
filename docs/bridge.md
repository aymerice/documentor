# Bridge

![Bridge_table_img](http://www.plantuml.com/plantuml/img/0Ti19Fv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJK532cDiONDp85DvStHbRGfZR65pSo1CRsTfOs5iNrDtQNHZQ0fz2dHlPsLqQ6Lo87iAOsnXStCWGd9fP6Tb2cDiONDp85PCGKuAOsnXStCWK6zoT0fZR65pSo1DKrHGNqDlRMrlRbz9RdDqOMvZPGfZR65pSo1DQN9oRt8AVGf2ScbaPsKWF2vaBY1DGKCAGd9fP6Tb82raBJuWJMboSczo2a9oQMHdPI0jP2q-851lSdGAGd9fP6Tb83mkP2uWJ6zdQMDXR5zJTsbqOsWAGd9fP6Tb82raBJuWJLDKK5z3RsrjRsvVIMvpT65kOsKAGd9fP6Tb83mjP2qWKtbpT6Lj2a9oQMHdPI0jP2q-85PCGKuAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

Configuration for a bridge within an [System](system.html).

A [Bridge](bridge.html) record represents an Ethernet switch with one or more
``ports,'' which are the [Port](port.html) records pointed to by the
[Bridge](bridge.html)'s [ports](bridge.html#ports) column. In the first release, only one
default bridge (bridge_normal) is supported

## 1. MSTP Status

MSTP global status for all MSTIs.

### 1.1 status

**Type**: _string->string_

Key-value pairs that report bridge status.

### 1.2 status : mstp_config_digest

**Type**: _string_

The configuration digest for the MSTP bridge that is derived based on the VLAN
membership of MST instances.

## 2. Bridge Status

Status information about bridges.

### 2.1 status

**Type**: _string->string_

Key-value pairs that report bridge status.

### 2.2 status : actual-mac-table-size

**Type**: _string_

Actual size of the mac table. If mac-table-size exceeds hardware capability,
then this field will show the real size used.

## 3. Other Features

### 3.1 datapath_id

**Type**: _string_

### 3.2 mirrors

**Type**: _uuid_ **refTable**: [Mirror](mirror.html) **refType**: _strong_



[Mirror](mirror.html) references for sessions configured in this bridge.

### 3.3 other_config

**Type**: _string->string_

### 3.4 other_config : hwaddr

**Type**: _string_

An Ethernet address in the form _xx_:_xx_:_xx_:_xx_:_xx_:_xx_ to set the
hardware address of the local port and influence the datapath ID.

### 3.5 other_config : mac-table-size

**Type**: _integer_

The maximum number of MAC addresses to learn.  The default is currently 16K.
The value, if specified, is forced into a reasonable range, currently 10 to
256K.

### 3.6 other_config : mac-aging-time

**Type**: _integer_

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

### 3.7 datapath_version

**Type**: _string_

### 3.8 datapath_type

**Type**: _string_

Name of datapath provider.

## 4. Core Features

### 4.1 name

**Type**: _string_

Bridge identifier.  Should be alphanumeric and no more than about 8 bytes long.
Must be unique among the names of ports, interfaces, and bridges on a host.

### 4.2 mstp_instances

**Type**: _integer->uuid_ **refTable**: [MSTP_Instance](mstp_instance.html) **refType**: _strong_



MSTP configuration for individual instance.

### 4.3 vlans

**Type**: _uuid_ **refTable**: [VLAN](vlan.html) **refType**: _strong_



VLANs included in the bridge.

### 4.4 ports

**Type**: _uuid_ **refTable**: [Port](port.html) **refType**: _strong_



Ports included in the bridge.

### 4.5 mstp_common_instance

**Type**: _uuid_ **refTable**: [MSTP_Common_Instance](mstp_common_instance.html) **refType**: _strong_



MSTP configuration for CIST(Common Instance Spanning Tree).

## 5. MSTP Configurations

MSTP global configurations for all MSTIs.

### 5.1 other_config

**Type**: _string->string_

### 5.2 other_config : mstp_config_name

**Type**: _string_

Set this value to specify the MSTP configuration name. Default value is system
MAC address.

### 5.3 other_config : mstp_config_revision

**Type**: _string_

Set this value to specify the configuration revision number. Default value is 0.

### 5.4 mstp_enable

**Type**: _boolean_

Set this value to `true`, to enable MSTP. Default value is `false`.

## 6. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 6.1 other_config

**Type**: _string->string_

### 6.2 external_ids

**Type**: _string->string_

