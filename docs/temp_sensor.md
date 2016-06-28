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

## 2. Readings group

### 2.1 min column

Historic minimum (since last restart of tempd process), in milidegrees Celcius.

### 2.2 max column

Historic maximum (since last restart of tempd process), in milidegrees Celcius.

### 2.3 temperature column

Current temperature reading, in milidegrees Celcius.

