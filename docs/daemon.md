# Daemon

![Daemon_table_img](http://www.plantuml.com/plantuml/img/0UC07Fz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo14OMLjRsuAVGf4OMLjRsuWF2raBI1JUNDqPMqAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Each entry in this table represents a single system daemon and contains
information about that specific daemon. One use is to identify those daemons
that read and process hardware description files to add new hardware into the
db.

## 1. Configuration group

### 1.1 is_hw_handler column

A boolean to indicate if this daemon is responsible for processing hardware
description information (either on boot, or as hardware subsystems are added or
removed).

### 1.2 name column

The name of the daemon.

## 2. Status group

### 2.1 cur_hw column

Sequence number that a daemon sets to the current value of
[next_hw](system.html#next-hw-column) in the [System](system.html) table after it has
successfully responded to a hardware change.

