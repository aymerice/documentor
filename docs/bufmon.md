# bufmon

![bufmon_table_img](http://www.plantuml.com/plantuml/img/0T00B_z0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWOdLcRMzk2dqAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

Configuration and status of the counters per Capacity Monitoring feature

## 1. Status

### 1.1 status

**Type**: _string_

Specifies the status of the counter.

### 1.2 counter_value

**Type**: _integer_

Last collected value of the counter.

## 2. Counter identification

### 2.1 name

**Type**: _string_

Name of the counter as it will be shown in the management systems and will be
referenced by all the interested agents. No spaces should be used in the name.

### 2.2 hw_unit_id

**Type**: _integer_

Identifies the ASIC that counter belongs to.

### 2.3 counter_vendor_specific_info

**Type**: _string->string_

Contains any information that might help ASIC specific driver to identify the
counter. Both keys and values are driver and ASIC specific.

## 3. Configuration

### 3.1 enabled

**Type**: _boolean_

Specifies whether counter is enabled.

### 3.2 trigger_threshold

**Type**: _integer_

Specifies counter specific threshold that would trigger collection.

