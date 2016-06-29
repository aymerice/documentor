# Radius_Server

![Radius_Server_table_img](http://www.plantuml.com/plantuml/img/0Gi1zFv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo1IOMHfTNDVKsLoTcLo2dqAKc5aQNLpNrDbSdPbSY0yBMGj85DvStHbRGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

These radius servers are being used for authenticating when users wants to login
to the box.

## 1. Ungrouped

### 1.1 retries

**Type**: _integer_

Specifies the number of retries to radius server if there is no response.
Default retry value is 1.

### 1.2 passkey

**Type**: _string_

Specifies the passkey between radius client and radius server for
authentication. Default passkey is testing123-1.

### 1.3 udp_port

**Type**: _integer_

Specifies the udp port number for authentication. Default udp port number for
authentication is 1812.

### 1.4 priority

**Type**: _integer_

Specifies the order in which radius servers are configured on the switch.

### 1.5 timeout

**Type**: _integer_

Specifies the timeout between authentication requests to radius server. Default
timeout is 5 seconds.

### 1.6 ip_address

**Type**: _string_

IP address of the radius server configured.

