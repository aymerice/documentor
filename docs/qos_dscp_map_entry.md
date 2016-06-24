# QoS_DSCP_Map_Entry

![QoS_DSCP_Map_Entry_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuIf8JCvEJ4zLK0hApozH24bCoaajLbAevb80WkISnE9YXU3AufBKN0KR6mMD49sSpFICalIYrDGyJGKxEwvQBYw8ei3yu7YNOEU0UD_4WdZNl9AYIkmQkA2cwUhQOT73nUMGcfS2SXO0)

Contains DSCP map entries used by QoS Trust Mode. It associates each code point
to local_priority (required), and (optionally), priority code point, color and
description.

## 1. Configuration group

### 1.1 description column

Used for customer documentation.

### 1.2 color column

It may be used later in the pipeline in packet-drop decision points. The default
is 'green'.

### 1.3 code_point column

The identifier for an entry in the DSCP map that represents the Differentiated
Services Code Point (DSCP) value for this entry.

### 1.4 priority_code_point column

The 802.1Q priority that will be assigned to the packet. If the packet is
transmitted with a VLAN tag, this value will be in the Priority Code Point
field. If this value is not specified, the default behavior is that the priority
of the packet will not be changed.

### 1.5 local_priority column

This is a switch internal meta-data value that will be associated with the
packet. This value will be used later to select the egress queue for the packet.

## 2. Hardware Default group

The key-value pairs document the hardware defaults for configuration columns in
this row.

### 2.1 hw_defaults : default_local_priority key

When missing, the default local_priority is obtained from the
[hw_defaults](qos_dscp_map_entry.html#hw-defaults-column) of the
[QoS_COS_Map_Entry](qos_cos_map_entry.html) row indexed by the top 3-bits of this
row's code_point (i.e. class selector bits cs0 through cs7).

### 2.2 hw_defaults : default_priority_code_point key

When missing, the default is not to remark packets' 802.1Q priority.

### 2.3 hw_defaults : default_color key

When missing, the default is 'green'.

