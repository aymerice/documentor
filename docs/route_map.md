# Route_Map

![Route_Map_table_img](http://www.plantuml.com/plantuml/img/0TC0BFz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKczrT6LVJM5m2dqAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. Global Route Map Configuration

### 1.1 route_map_entries

**Type**: _integer->uuid_ **refTable**: [Route_Map_Entry](route_map_entry.html) **refType**: _strong_



Route map entries keyed by preference value.

### 1.2 name

**Type**: _string_

Reference to the VRF table, to which this route belongs.

## 2. Status

### 2.1 status

**Type**: _string->string_

## 3. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 3.1 external_ids

**Type**: _string->string_

### 3.2 other_config

**Type**: _string->string_

