# bufmon

Configuration and status of the counters per Capacity Monitoring feature

## 1. Status group

### 1.1 status column

Specifies the status of the counter.

### 1.2 counter_value column

Last collected value of the counter.

## 2. Counter identification group

### 2.1 name column

Name of the counter as it will be shown in the management systems and will be
referenced by all the interested agents. No spaces should be used in the name.

### 2.2 hw_unit_id column

Identifies the ASIC that counter belongs to.

### 2.3 counter_vendor_specific_info column

Contains any information that might help ASIC specific driver to identify the
counter. Both keys and values are driver and ASIC specific.

## 3. Configuration group

### 3.1 enabled column

Specifies whether counter is enabled.

### 3.2 trigger_threshold column

Specifies counter specific threshold that would trigger collection.
