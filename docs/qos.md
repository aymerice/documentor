# QoS

![QoS_table_img](http://www.plantuml.com/plantuml/img/0H01x_v0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKMzJ2cDiONDp85DvStHbRGfz2dHlPsLqQ6Lo87iAOsnXStCWK6zoT0fz2b5lKo0yBNKj851lSdGAKMzJ83mjP2qWKtbpT6Lj2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Used to specify named profiles of scheduling configuration. Ports use a schedule
profile to configure their packet queue servicing behavior.

## 1. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 1.1 external_ids

**Type**: _string->string_

### 1.2 other_config

**Type**: _string->string_

## 2. Hardware Default

### 2.1 hw_default

**Type**: _boolean_

When true, this row signifies the hardware default schedule profile.

Default schedule profile is "Strict Priority" when any of the following occur:

+No row in this table has hw_default true +More than one row in this table has
hw_default true +Any [Queue](queue.html) rows referenced do not have their hw_default
true

## 3. Configuration

### 3.1 queues

**Type**: _integer->uuid_ **refTable**: [Queue](queue.html) **refType**: _strong_



Schedule parameters for individual queues.

Queues are numbered in *priority order*, with zero being the lowest priority.
The maximum number of queues is hardware dependent.

### 3.2 name

**Type**: _string_

There must be a user-defined name of the schedule profile.

