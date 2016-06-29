# Subsystem

![Subsystem_table_img](http://www.plantuml.com/plantuml/img/0QW1L_v0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo1JTM9pUNDqPMqAOsnXStCWJ4L42cDiONDp84PXRWfZR65pSo19RdHbScPXOsKAOsnXStCWL6LjS5zpPMvpRt8AOsnXStCWK6ztPN9VStLmS6nv2dqAKtLYStbpT6Lj82raBJuWHc5k2bDrOdDvStHbRI0yBMGj85DvStHbRGfJTM9pUNDqPMqWBMGjFY19RdHbScPXOsKAKtLYStbpT6Lj82raBJuWJ4L42bDrOdDvStHbRI0jP2q-85HbRN1VSsLkSszo2bDrOdDvStHbRI0jP2q-851lTsLoNtDrS71iUGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. Configuration group

### 1.1 leds column

### 1.2 asset_tag_number column

### 1.3 fans column

### 1.4 power_supplies column

### 1.5 temp_sensors column

## 2. Inventory Info group

### 2.1 other_info column

### 2.2 other_info : diag_version key

### 2.3 other_info : l3_port_requires_internal_vlan key

### 2.4 other_info : number_of_macs key

### 2.5 other_info : vendor key

### 2.6 other_info : max_interface_speed key

### 2.7 other_info : interface_count key

### 2.8 other_info : onie_version key

### 2.9 other_info : max_bond_member_count key

### 2.10 other_info : height key

### 2.11 other_info : platform_name key

### 2.12 other_info : max_bond_count key

### 2.13 other_info : part_number key

### 2.14 other_info : device_version key

### 2.15 other_info : country_code key

### 2.16 other_info : label_revision key

### 2.17 other_info : serial_number key

### 2.18 other_info : manufacture_date key

### 2.19 other_info : max_transmission_unit key

### 2.20 other_info : base_mac_address key

### 2.21 other_info : manufacturer key

### 2.22 name column

### 2.23 hw_desc_dir column

Directory where the hardware description files for this subsystem are located.

### 2.24 type column

## 3. Hardware Configuration group

### 3.1 interfaces column

References to the interfaces which are part of this subsystem.

### 3.2 next_mac_address column

Next available (unused) Ethernet MAC address from the MAC address pool for this
subsystem.

### 3.3 macs_remaining column

The number of available (unused) Ethernet MAC address from the MAC address pool
for this subsystem.

## 4. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 4.1 other_config column

### 4.2 other_config : fan_speed_override key

If the fan_speed_override value is set, `fand` uses that value (unless the
output of `tempd` requests max speed, in which case the fans are set to max to
avoid an over-temperature situation).

### 4.3 external_ids column

