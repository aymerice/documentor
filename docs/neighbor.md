# Neighbor

![Neighbor_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuIf8JCvEJ4zLK0hApozH24bCoaajLbAevb80WkISnE9Y1R_KpFICfFmY1HiR1OqGdHmWhoIzA3KrJrF1pewhbWkYAYp83Ri2Y7H0Vb49TdcuyRgwTc1bg290SxaSKlDIW6u5)

List of all the connected neighbors.

## 1. Neighbor information group

### 1.1 status : dp_hit key

Indicates if there is active traffic to the neighbor. This value is periodically
updated. If the value is set to `false`, it indicates that there was no traffic
to this neighbor recently. Default is `true`

### 1.2 address_family column

Address family of the neighbor.

### 1.3 mac column

MAC address learned for this neighbor.

### 1.4 state column

Current state of the neighbor entry.

### 1.5 vrf column

Reference to the VRF table, to which this neighbor belongs.

### 1.6 ip_address column

The IPv4 address or the IPv6 address of neighbor

### 1.7 port column

Port on which this neighbor was learned.

