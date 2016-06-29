# Subsystem

![Subsystem_table_img](http://www.plantuml.com/plantuml/img/0S81FVv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo1JTM9pUNDqPMqAOsnXStCWJ4L42cDiONDp84PXRWfZR65pSo19RdHbScPXOsKAOsnXStCWL6LjS5zpPMvpRt8AOsnXStCWK6ztPN9VStLmS6nv2dqAKtLYStbpT6Lj82raBJuWHc5k2bDrOdDvStHbRI0yBMGj85DvStHbRGfJTM9pUNDqPMqWBMGjFY19RdHbScPXOsKAKtLYStbpT6Lj82raBJuWJ4L42bDrOdDvStHbRI0jP2q-85HbRN1VSsLkSszo2bDrOdDvStHbRI0jP2q-851lTsLoNtDrS71iUGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. Configuration

### 1.1 leds

**Type**: _uuid_ **refTable**: [LED](led.html) **refType**: _strong_



### 1.2 asset_tag_number

**Type**: _string_

### 1.3 fans

**Type**: _uuid_ **refTable**: [Fan](fan.html) **refType**: _strong_



### 1.4 power_supplies

**Type**: _uuid_ **refTable**: [Power_supply](power_supply.html) **refType**: _strong_



### 1.5 temp_sensors

**Type**: _uuid_ **refTable**: [Temp_sensor](temp_sensor.html) **refType**: _strong_



## 2. Inventory Info

### 2.1 other_info

**Type**: _string->string_

### 2.2 other_info : diag_version

**Type**: _string_

### 2.3 other_info : l3_port_requires_internal_vlan

**Type**: _string_

### 2.4 other_info : number_of_macs

**Type**: _string_

### 2.5 other_info : vendor

**Type**: _string_

### 2.6 other_info : max_interface_speed

**Type**: _string_

### 2.7 other_info : interface_count

**Type**: _string_

### 2.8 other_info : onie_version

**Type**: _string_

### 2.9 other_info : max_bond_member_count

**Type**: _string_

### 2.10 other_info : height

**Type**: _string_

### 2.11 other_info : platform_name

**Type**: _string_

### 2.12 other_info : max_bond_count

**Type**: _string_

### 2.13 other_info : part_number

**Type**: _string_

### 2.14 other_info : device_version

**Type**: _string_

### 2.15 other_info : country_code

**Type**: _string_

### 2.16 other_info : label_revision

**Type**: _string_

### 2.17 other_info : serial_number

**Type**: _string_

### 2.18 other_info : manufacture_date

**Type**: _string_

### 2.19 other_info : max_transmission_unit

**Type**: _string_

### 2.20 other_info : base_mac_address

**Type**: _string_

### 2.21 other_info : manufacturer

**Type**: _string_

### 2.22 name

**Type**: _string_

### 2.23 hw_desc_dir

**Type**: _string_

Directory where the hardware description files for this subsystem are located.

### 2.24 type

**Type**: _string_

## 3. Hardware Configuration

### 3.1 interfaces

**Type**: _uuid_ **refTable**: [Interface](interface.html) **refType**: _strong_



References to the interfaces which are part of this subsystem.

### 3.2 next_mac_address

**Type**: _string_

Next available (unused) Ethernet MAC address from the MAC address pool for this
subsystem.

### 3.3 macs_remaining

**Type**: _integer_

The number of available (unused) Ethernet MAC address from the MAC address pool
for this subsystem.

## 4. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 4.1 other_config

**Type**: _string->string_

### 4.2 other_config : fan_speed_override

**Type**: _string_

If the fan_speed_override value is set, `fand` uses that value (unless the
output of `tempd` requests max speed, in which case the fans are set to max to
avoid an over-temperature situation).

### 4.3 external_ids

**Type**: _string->string_

