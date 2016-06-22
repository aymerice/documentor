# Q_Profile

Used to specify named profiles of queue configuration. Ports use a queue profile
to configure their packet queue settings.

## 1. Configuration group

### 1.1 q_profile_entries column

Configuration parameters for individual queues.

Queues are numbered in *priority order*, with zero being the lowest priority.
The maximum number of queues is hardware dependent.

### 1.2 name column

There must be a user-defined name of the schedule profile.

## 2. Hardware Default group

### 2.1 hw_default column

When true, this row contains the hardware default queue profile.

The default queue profile will be 8 queues when any of the following conditions
occur:

+No row in this table has hw_default true +More than one row in this table has
hw_default true +Any [Q_Profile_Entry](q_profile_entry.html) rows referenced do not
have their hw_default true

