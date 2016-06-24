# QoS

![QoS_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuIf8JCvEJ4zLK0hApozH24bCoaajLbAevb80WkISnE9YXS3yO0KR6mMD49sSpFICalIYrDGyJGKxEoGbmPN59Qcvs5NLSa7K1EGNbM1N0PRHrRK3sSG5DGh6TKZDIm4w4m00)

Used to specify named profiles of scheduling configuration. Ports use a schedule
profile to configure their packet queue servicing behavior.

## 1. Hardware Default group

### 1.1 hw_default column

When true, this row signifies the hardware default schedule profile.

Default schedule profile is "Strict Priority" when any of the following occur:

+No row in this table has hw_default true +More than one row in this table has
hw_default true +Any [Queue](queue.html) rows referenced do not have their hw_default
true

## 2. Configuration group

### 2.1 queues column

Schedule parameters for individual queues.

Queues are numbered in *priority order*, with zero being the lowest priority.
The maximum number of queues is hardware dependent.

### 2.2 name column

There must be a user-defined name of the schedule profile.

