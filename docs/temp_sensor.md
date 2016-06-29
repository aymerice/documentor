# Temp_sensor

![Temp_sensor_table_img](http://www.plantuml.com/plantuml/img/0Ta09lz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1JTM9pUNDqPMqAOsnXStCWL6LjS5zpPMvpRt8AVGfKPMrmNtDbRdDlSY0yBNKj85DrOdDvStHbRGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. Status group

### 1.1 status column

Results of evaluation of the current temperature against the sensor's threshold
values.

### 1.2 fan_state column

Recommended minimum fan setting based on current temperature. The fand process
should choose the worst-case sensor fan_state when determining the fan setting
for the subsystem.

## 2. Ungrouped group

### 2.1 name column

Logical name of the temperature sensor, including the subsystem name and numeric
identifier of the temperature sensor.

### 2.2 location column

Descriptive text for the physical location of the temperature sensor relative to
the subsystem.

### 2.3 hw_config column

## 3. Readings group

### 3.1 min column

Historic minimum (since last restart of tempd process), in milidegrees Celcius.

### 3.2 max column

Historic maximum (since last restart of tempd process), in milidegrees Celcius.

### 3.3 temperature column

Current temperature reading, in milidegrees Celcius.

## 4. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 4.1 other_config column

### 4.2 external_ids column

