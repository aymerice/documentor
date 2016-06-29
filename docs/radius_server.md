# Radius_Server

![Radius_Server_table_img](http://www.plantuml.com/plantuml/img/0V403lz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo1IOMHfTNDVKsLoTcLo2dqAKc5aQNLpNrDbSdPbSY0yBMGj85DvStHbRGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

These radius servers are being used for authenticating when users wants to login
to the box.

## 1. Ungrouped group

### 1.1 retries column

Specifies the number of retries to radius server if there is no response.
Default retry value is 1.

### 1.2 passkey column

Specifies the passkey between radius client and radius server for
authentication. Default passkey is testing123-1.

### 1.3 udp_port column

Specifies the udp port number for authentication. Default udp port number for
authentication is 1812.

### 1.4 priority column

Specifies the order in which radius servers are configured on the switch.

### 1.5 timeout column

Specifies the timeout between authentication requests to radius server. Default
timeout is 5 seconds.

### 1.6 ip_address column

IP address of the radius server configured.

