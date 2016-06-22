# QoS_COS_Map_Entry

Contains COS map entries used by QoS Trust Mode. It associates each priority to
local_priority (required), and (optionally), color and description.

## 1. Configuration group

### 1.1 description column

Used for customer documentation.

### 1.2 color column

It may be used later in the pipeline in packet-drop decision points. The default
is 'green'.

### 1.3 code_point column

The identifier for an entry in the COS map that is the 802.1Q priority code
point for this entry.

### 1.4 local_priority column

This is a switch internal meta-data value that will be associated with the
packet. This value will be used later to select the egress queue for the packet.

## 2. Hardware Default group

The key-value pairs document the hardware defaults for configuration columns in
this row.

### 2.1 hw_defaults : default_local_priority key

When missing, the default is the 802.1Q (Annex I) Traffic Type assignment for
this row's Priority Code Point:

+code_point 0 (Traffic Type BE) local_priority=1 +code_point 1 (Traffic Type BK)
local_priority=0 +code_point 2 (Traffic Type EE) local_priority=2 +code_point 3
(Traffic Type CA) local_priority=3 +code_point 4 (Traffic Type VI)
local_priority=4 +code_point 5 (Traffic Type VO) local_priority=5 +code_point 6
(Traffic Type IC) local_priority=6 +code_point 7 (Traffic Type NC)
local_priority=7

### 2.2 hw_defaults : default_color key

When missing, the default is 'green'.

