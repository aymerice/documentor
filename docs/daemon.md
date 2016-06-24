# Daemon

![Daemon_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuIf8JCvEJ4zLK0hApozH24bCoaajLbAevb80WkISnE9YXU3AufBKN0KR6mMD49sSpFICalIYrDGyJGKxEwvQBeWQbyJKtFmyx6gW-dLrxQ3Ak1nIyrA0TWC0)

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

