# Q_Profile

![Q_Profile_table_img](http://www.plantuml.com/plantuml/img/0GW1z_v0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKLzGSczcQMnb2cDiONDp85DvStHbRGfz2dHlPsLqQ6Lo87iAOsnXStCWK6zoT0fz2b5VK79lPcbiPI0yBNKj851lSdGAKLzGSczcQMnb83mjP2qWKtbpT6Lj2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Used to specify named profiles of queue configuration. Ports use a queue profile
to configure their packet queue settings.

## 1. Configuration group

### 1.1 q_profile_entries column

Configuration parameters for individual queues.

Queues are numbered in *priority order*, with zero being the lowest priority.
The maximum number of queues is hardware dependent.

### 1.2 name column

There must be a user-defined name of the schedule profile.

## 2. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 2.1 external_ids column

### 2.2 other_config column

## 3. Hardware Default group

### 3.1 hw_default column

When true, this row contains the hardware default queue profile.

The default queue profile will be 8 queues when any of the following conditions
occur:

+No row in this table has hw_default true +More than one row in this table has
hw_default true +Any [Q_Profile_Entry](q_profile_entry.html) rows referenced do not
have their hw_default true

