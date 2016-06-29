# QoS

![QoS_table_img](http://www.plantuml.com/plantuml/img/0VO02Vz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKMzJ2cDiONDp85DvStHbRGfz2dHlPsLqQ6Lo87iAOsnXStCWK6zoT0fz2b5lKo0yBNKj851lSdGAKMzJ83mjP2qWKtbpT6Lj2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Used to specify named profiles of scheduling configuration. Ports use a schedule
profile to configure their packet queue servicing behavior.

## 1. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 1.1 external_ids column

### 1.2 other_config column

## 2. Hardware Default group

### 2.1 hw_default column

When true, this row signifies the hardware default schedule profile.

Default schedule profile is "Strict Priority" when any of the following occur:

+No row in this table has hw_default true +More than one row in this table has
hw_default true +Any [Queue](queue.html) rows referenced do not have their hw_default
true

## 3. Configuration group

### 3.1 queues column

Schedule parameters for individual queues.

Queues are numbered in *priority order*, with zero being the lowest priority.
The maximum number of queues is hardware dependent.

### 3.2 name column

There must be a user-defined name of the schedule profile.

