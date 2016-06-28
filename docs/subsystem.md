# Subsystem

![Subsystem_table_img](http://www.plantuml.com/plantuml/img/0QW1L_v0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo1JTM9pUNDqPMqAOsnXStCWJ4L42cDiONDp84PXRWfZR65pSo19RdHbScPXOsKAOsnXStCWL6LjS5zpPMvpRt8AOsnXStCWK6ztPN9VStLmS6nv2dqAKtLYStbpT6Lj82raBJuWHc5k2bDrOdDvStHbRI0yBMGj85DvStHbRGfJTM9pUNDqPMqWBMGjFY19RdHbScPXOsKAKtLYStbpT6Lj82raBJuWJ4L42bDrOdDvStHbRI0jP2q-85HbRN1VSsLkSszo2bDrOdDvStHbRI0jP2q-851lTsLoNtDrS71iUGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. Inventory Info group

### 1.1 other_info : diag_version key

### 1.2 other_info : l3_port_requires_internal_vlan key

### 1.3 other_info : number_of_macs key

### 1.4 other_info : vendor key

### 1.5 other_info : max_interface_speed key

### 1.6 other_info : interface_count key

### 1.7 other_info : onie_version key

### 1.8 other_info : max_bond_member_count key

### 1.9 other_info : height key

### 1.10 other_info : platform_name key

### 1.11 other_info : max_bond_count key

### 1.12 other_info : part_number key

### 1.13 other_info : device_version key

### 1.14 other_info : country_code key

### 1.15 other_info : label_revision key

### 1.16 other_info : serial_number key

### 1.17 other_info : manufacture_date key

### 1.18 other_info : max_transmission_unit key

### 1.19 other_info : base_mac_address key

### 1.20 other_info : manufacturer key

### 1.21 hw_desc_dir column

Directory where the hardware description files for this subsystem are located.

## 2. Hardware Configuration group

### 2.1 interfaces column

References to the interfaces which are part of this subsystem.

### 2.2 next_mac_address column

Next available (unused) Ethernet MAC address from the MAC address pool for this
subsystem.

### 2.3 macs_remaining column

The number of available (unused) Ethernet MAC address from the MAC address pool
for this subsystem.

## 3. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 3.1 other_config : fan_speed_override key

If the fan_speed_override value is set, `fand` uses that value (unless the
output of `tempd` requests max speed, in which case the fans are set to max to
avoid an over-temperature situation).

