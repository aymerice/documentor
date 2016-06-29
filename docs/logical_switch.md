# Logical_Switch

![Logical_Switch_table_img](http://www.plantuml.com/plantuml/img/0VC03Fz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJ6zdQMDXR5zJTsbqOsWAVGfqRsTbT6XbSY1x2cDiONDp849oQMHdPGfz2anlPsbZOMnVKtTfT6De82vaBZuWGd9fP6Tb2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Configuration for identifying overlay networks associated with bridges.

## 1. Ungrouped group

### 1.1 tunnel_key column

Tunnel key used in the overlay. For VXLAN, this is the VNI.

### 1.2 bridge column

Reference to a [Bridge](bridge.html) participating in the overlay.

### 1.3 from column

The entity managing the overlay.

### 1.4 name column

Name of the overlay network.

### 1.5 description column

Description of the overlay network.

