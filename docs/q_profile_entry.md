# Q_Profile_Entry

![Q_Profile_Entry_table_img](http://www.plantuml.com/plantuml/img/0R80JVz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1HNr1oRsPfR6LVHMvqSdaAVGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

Contains configuration parameters for one queue of one profile.

## 1. Configuration group

### 1.1 local_priorities column

This essential parameter specifies one or more local-priority(s) that are
assigned to this queue.  Packets' local-priority meta-data is initially assigned
by the port's QoS Trust Mode  (see [Port](port.html) qos_config).  If missing, the
queue is not used.

### 1.2 description column

Used for documentation of these queue configuration parameters.

## 2. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 2.1 external_ids column

### 2.2 other_config column

## 3. Hardware Default group

### 3.1 hw_default column

When true, this row contains the hardware default queue profile parameters for
this queue.

