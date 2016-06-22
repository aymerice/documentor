# Temp_sensor

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

