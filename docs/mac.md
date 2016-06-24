# MAC

![MAC_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuIf8JCvEJ4zLK0hApozH24bCoaajLbAevb80WkISnE9Y1Lz7PmKR6mMD49sSpFICalIYrDGyJGKxEwvQBYw82gUYp1IW4LWLGLG4v1ULO9Vd0Xclgsi7LWBdG4paud98pKi1kH80)

Configuration for consolidated MAC table which can potentially be learnt from
ASIC, from the hw-vtep controller or statically configured.

## 1. status group

This column specifies the status of this entry in the table.

### 1.1 status : no_memory key

Memory exhaustion

### 1.2 status : ok key

Properly configured

### 1.3 status : invalid key

Invalid parameters

### 1.4 status : error key

Unspecified error.

