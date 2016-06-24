# UDP_Bcast_Forwarder_Server

![UDP_Bcast_Forwarder_Server_table_img](http://www.plantuml.com/plantuml/img/XOzD2i8m48NtSugXAmLxWnAAIDUbhMx3c0vHZ8rCHbs8TzVGRT6t_TuFhqvAelThW1kv2td6eejHSQ1Zu5JW2_0h5oWbtEzQktMKr3PHdYGZY-rP7YnOLRWQDk7iJ-g5ULgZCV06c8E7hbbspBYDeiiSVaoMfSd5_oov7A3cQSmd)

Each entry represents the match and forward criteria for UDP broadcast packets
received on the port. UDP-Broadcast-Forwarder feature uses these entries to
forward selective UDP broadcast packets received on the routed Port to the
configured server(s).

## 1. UDP Broadcast Forwarder Configuration group

### 1.1 udp_dport column

UDP broadcast packets with this destination udp port are forwarded to the
configured server(s).

### 1.2 dest_vrf column

VRF through which server is reachable.

### 1.3 src_port column

Reference to the routed port on which packets are receive.

### 1.4 ipv4_ucast_server column

List of IPv4 unicast server destinations to which matching UDP broadcast packets
received on the port are duplicated and forwarded.

