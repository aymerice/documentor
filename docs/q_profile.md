# Q_Profile

![Q_Profile_table_img](http://www.plantuml.com/plantuml/img/0I81tVv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKLzGSczcQMnb2cDiONDp85DvStHbRGfz2dHlPsLqQ6Lo87iAOsnXStCWK6zoT0fz2b5VK79lPcbiPI0yBNKj851lSdGAKLzGSczcQMnb83mjP2qWKtbpT6Lj2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Used to specify named profiles of queue configuration. Ports use a queue profile
to configure their packet queue settings.

## 1. Configuration

### 1.1 q_profile_entries

**Type**: _integer->uuid_ **refTable**: [Q_Profile_Entry](q_profile_entry.html) **refType**: _strong_



Configuration parameters for individual queues.

Queues are numbered in *priority order*, with zero being the lowest priority.
The maximum number of queues is hardware dependent.

### 1.2 name

**Type**: _string_

There must be a user-defined name of the schedule profile.

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

When true, this row contains the hardware default queue profile.

The default queue profile will be 8 queues when any of the following conditions
occur:

+No row in this table has hw_default true +More than one row in this table has
hw_default true +Any [Q_Profile_Entry](q_profile_entry.html) rows referenced do not
have their hw_default true

