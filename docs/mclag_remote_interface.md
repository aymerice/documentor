# MCLAG_Remote_Interface

![MCLAG_Remote_Interface_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuIf8JCvEJ4zLK0hApozH24bCoaajLbAevb80WkISnE9Y1Lzd7qVt-A3KtFoIr7ZFl9BKehJ4v5G56ni5ZH2TdCpqZ9BqejJKF4q5EpkkMYukYAQ0_A8Ix4gum5AwkdOu3ERYSaZDIm4v3G00)

Each entry contains the information about a physical interface on the peer
switch which is configured for MCLAG. This information is determined by
exchanging packets over the ISL link between the MLAG switches.

## 1. partner information group

### 1.1 lacp_partner_system_id column

Peer interface's LACP partner system ID.

### 1.2 name column

Name of the peer interface.

### 1.3 lacp_partner_port_id column

Peer interface's LACP partner port ID.

### 1.4 lacp_partner_key column

Peer interface's LACP partner key.

## 2. partner link status group

### 2.1 duplex column

The duplex mode of the physical network link.

### 2.2 link_state column

The observed state of the physical network link.  This is ordinarily the link's
carrier status.

### 2.3 link_speed column

The negotiated speed of the physical network link in bits per second. Valid
values are positive integers greater than 0.

### 2.4 admin_state column

The administrative state of the physical network link.

### 2.5 lacp_partner_state column

LACP partner state.

