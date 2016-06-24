# MSTP_Common_Instance_Port

![MSTP_Common_Instance_Port_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuKhEIImkLl0D3Wc8TyxFpStFY_VC0qhc9QV61-GNbIZOs2XeXEZaPAPdbAGNfQRcQIhOsU7HX4yzRlDmMw-hQmVMXrK9M1QdNYw7rBmKe1S1)

This represents information regarding a specific Port within the Bridge's Bridge
Protocol entity, for the CIST.

## 1. Status group

These are status parameters for the common instance. These values will be
calculated from the time of protocol initialization.

### 1.1 port_role column

The role of this port in the active MSTP topology.

### 1.2 fwd_transition_count column

The number of times this port has transitioned to the forwarding state.

### 1.3 protocol_migration_enable column

Set this value to `true` to switch the STP working mode or to `false` to
explicitly disable it. Default is `true`.

### 1.4 port_path_cost column

The operational value of the path cost.

### 1.5 port_hello_time column

The port's hello time value, for the CIST.

### 1.6 designated_bridge column

The designated bridge identifier component of the port's MSTI port priority
vector.

### 1.7 designated_path_cost column

The path cost for this port.

### 1.8 designated_root column

The designated root ID for the port.

### 1.9 port_state column

The state of the port in the active topology. Default value is Blocking.

### 1.10 designated_port column

The designated port identifier component of the port's MSTI port priority
vector.

### 1.11 link_type column

Specifies the link type. Default value is point_to_point.

### 1.12 cist_path_cost column

The CIST path cost from the transmitting bridge to the CIST regional root.

### 1.13 cist_regional_root_id column

The regional root Id for the CIST.

### 1.14 oper_edge_port column

The operational port type as edge port or not for the CIST.

## 2. Configurations group

### 2.1 loop_guard_disable column

Set this value to `true` if loop guard is enabled (to block sending and
receiving BPDUs on the port). Default value is `false`.

### 2.2 bpdu_guard_disable column

Set this value to `true` if BPDU Guard enabled (to shut down the port if that
port receives a BPDU). Default is `false`.

### 2.3 port column

Specifies port for the CIST instance.

### 2.4 bpdu_filter_disable column

Set this value to `true` if BPDU filter is enabled(to suppress sending and
receiving BPDUs on the port). Default value is `false`.

### 2.5 restricted_port_role_disable column

Set this value to `true` if restiricted role enabled (not to be selected as Root
Port for the CIST or any MSTI). Default is `false`.

### 2.6 admin_edge_port_disable column

Set this value to `true`, if this admin edge port should not participate in root
election. Default is `false`.

### 2.7 root_guard_disable column

Set this value to `true` if root guard is enabled(to participate in STP as long
as the device does not try to become the root). Default value is `false`.

### 2.8 bpdus_rx_enable column

Set this value to `false` to stop transmission of BPDUs. Default is `true`.

### 2.9 admin_path_cost column

The path cost for the port to reach spanning-tree root.

### 2.10 port_priority column

Set this value to specify the port-priority. configurable in increments of 16.
Default value is 128.

### 2.11 restricted_port_tcn_disable column

Set this value to `true` if restiricted port tcn is enabled(not to propagate
topology changes to other ports). Default is `false`.

### 2.12 bpdus_tx_enable column

Set this value to `false` not to transmit the BPDUs Default is `true`.

## 3. Statistics group

### 3.1 mstp_statistics : mstp_BPDUs_Rx key

The received BPDU count.

### 3.2 mstp_statistics : mstp_BPDUs_Tx key

The transmitted BPDU count.

