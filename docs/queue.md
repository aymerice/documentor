# Queue

![Queue_table_img](http://www.plantuml.com/plantuml/img/0S80FVz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1HTMLrPGfz2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Contains scheduling parameters for one queue of one profile.

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

When true, this row contains the hardware default schedule profile parameters
for this queue.

## 3. Configuration

### 3.1 algorithm

**Type**: _string_

This parameter selects the scheduling behavior of the queue:

`strict` - Strict Priority will service all packets in the queue before any
packets in lower numbered queues as long as there are no packets in any higher
number queue.

`dwrr` - Deficit Weight Round Robin will apportion available bandwidth amongst
all non-empty dwrr queues in relation to their queue weights.

If this parameter is missing, it is assumed to be 'strict'.

### 3.2 weight

**Type**: _integer_

The weight value for this queue. The maximum weight is hardware dependent.

