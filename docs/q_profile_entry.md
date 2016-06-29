# Q_Profile_Entry

![Q_Profile_Entry_table_img](http://www.plantuml.com/plantuml/img/0Sm0C_z0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1HNr1oRsPfR6LVHMvqSdaAVGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Contains configuration parameters for one queue of one profile.

## 1. Configuration

### 1.1 local_priorities

**Type**: _integer_

This essential parameter specifies one or more local-priority(s) that are
assigned to this queue.  Packets' local-priority meta-data is initially assigned
by the port's QoS Trust Mode  (see [Port](port.html) qos_config).  If missing, the
queue is not used.

### 1.2 description

**Type**: _string_

Used for documentation of these queue configuration parameters.

## 2. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 2.1 external_ids

**Type**: _string->string_

### 2.2 other_config

**Type**: _string->string_

## 3. Hardware Default

### 3.1 hw_default

**Type**: _boolean_

When true, this row contains the hardware default queue profile parameters for
this queue.

