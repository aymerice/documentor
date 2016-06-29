# Temp_sensor

![Temp_sensor_table_img](http://www.plantuml.com/plantuml/img/0VC03Fz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1JTM9pUNDqPMqAOsnXStCWL6LjS5zpPMvpRt8AVGfKPMrmNtDbRdDlSY0yBNKj85DrOdDvStHbRGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. Status

### 1.1 status

**Type**: _string_

Results of evaluation of the current temperature against the sensor's threshold
values.

### 1.2 fan_state

**Type**: _string_

Recommended minimum fan setting based on current temperature. The fand process
should choose the worst-case sensor fan_state when determining the fan setting
for the subsystem.

## 2. Ungrouped

### 2.1 name

**Type**: _string_

Logical name of the temperature sensor, including the subsystem name and numeric
identifier of the temperature sensor.

### 2.2 location

**Type**: _string_

Descriptive text for the physical location of the temperature sensor relative to
the subsystem.

### 2.3 hw_config

**Type**: _string->string_

## 3. Readings

### 3.1 min

**Type**: _integer_

Historic minimum (since last restart of tempd process), in milidegrees Celcius.

### 3.2 max

**Type**: _integer_

Historic maximum (since last restart of tempd process), in milidegrees Celcius.

### 3.3 temperature

**Type**: _integer_

Current temperature reading, in milidegrees Celcius.

## 4. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 4.1 other_config

**Type**: _string->string_

### 4.2 external_ids

**Type**: _string->string_

