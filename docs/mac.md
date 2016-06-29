# MAC

![MAC_table_img](http://www.plantuml.com/plantuml/img/0VO02Vz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJK532dqAT6zdPNHePN8WUmfZR65pSo12ScbaPsKAOsnXStCWK6zoT0fz2ar1Go0kP2u-849oQMHdPGfDGKCWBcGkFY1GRt9q2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Configuration for consolidated MAC table which can potentially be learnt from
ASIC, from the hw-vtep controller or statically configured.

## 1. status group

This column specifies the status of this entry in the table.

### 1.1 status column

### 1.2 status : no_memory key

Memory exhaustion

### 1.3 status : ok key

Properly configured

### 1.4 status : invalid key

Invalid parameters

### 1.5 status : error key

Unspecified error.

## 2. Ungrouped group

### 2.1 bridge column

Specifies the bridge [Bridge](bridge.html) on which this MAC address is associated.

### 2.2 from column

This specifies whether this MAC address has been added by the hw-vtep controller
or dynamically learnt from the ASIC.

### 2.3 vlan column

VLAN associated with MAC address.

### 2.4 mac_addr column

MAC address.

### 2.5 tunnel_key column

If this MAC address is learnt from the tunnel port, then the tunnel_key will be
populated/configured. Otherwise, for static entries not having tunnel as port,
this column should not be populated.

### 2.6 expiry_time column

POSIX Time at which this MAC entry expires.

### 2.7 port column

Specifies the port [Port](port.html) on which this MAC address is associated.

