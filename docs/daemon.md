# Daemon

![Daemon_table_img](http://www.plantuml.com/plantuml/img/0Vq00lz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo14OMLjRsuAVGf4OMLjRsuWF2raBI1JUNDqPMqAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

Each entry in this table represents a single system daemon and contains
information about that specific daemon. One use is to identify those daemons
that read and process hardware description files to add new hardware into the
db.

## 1. Configuration

### 1.1 is_hw_handler

**Type**: _boolean_

A boolean to indicate if this daemon is responsible for processing hardware
description information (either on boot, or as hardware subsystems are added or
removed).

### 1.2 name

**Type**: _string_

The name of the daemon.

## 2. Status

### 2.1 cur_hw

**Type**: _integer_

Sequence number that a daemon sets to the current value of
[next_hw](system.html#next-hw) in the [System](system.html) table after it has
successfully responded to a hardware change.

