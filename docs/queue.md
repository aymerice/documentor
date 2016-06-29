# Queue

![Queue_table_img](http://www.plantuml.com/plantuml/img/0QW0L_z0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1HTMLrPGfz2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Contains scheduling parameters for one queue of one profile.

## 1. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 1.1 external_ids column

### 1.2 other_config column

## 2. Hardware Default group

### 2.1 hw_default column

When true, this row contains the hardware default schedule profile parameters
for this queue.

## 3. Configuration group

### 3.1 algorithm column

This parameter selects the scheduling behavior of the queue:

`strict` - Strict Priority will service all packets in the queue before any
packets in lower numbered queues as long as there are no packets in any higher
number queue.

`dwrr` - Deficit Weight Round Robin will apportion available bandwidth amongst
all non-empty dwrr queues in relation to their queue weights.

If this parameter is missing, it is assumed to be 'strict'.

### 3.2 weight column

The weight value for this queue. The maximum weight is hardware dependent.

