# DHCP_Server

![DHCP_Server_table_img](http://www.plantuml.com/plantuml/img/0QS1MFv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo14I4DGKt9sNqrXT6De2cDiONDp84H8Gr1JSdPVKc5kPsKAOsnXStCWLb962cDiONDp84H8Gr1VKsLoTcLo2cDiONDp84H8Gr1JSdPVKtHXT6bZNqXlStGAOsnXStCWH4X3K5DoTbzFS7HfRsuAVGf4I4DGNrDbSdPbSY0jP2q-84H8Gr1JSdPVKtHXT6bZNqXlStGAH4X3K5zJPN9sPN8WBMGjFY14I4DGKt9sNqrXT6De2aH8Gr1VKsLoTcLo82raBJuWH4X3K5DoTbzIOMvdPGf4I4DGNrDbSdPbSY0jP2q-84H8Gr1JSdPVJt1qQMzk2aH8Gr1VKsLoTcLo83mjTIqWLb962cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

DHCP Server configuration.

## 1. Configuration group

### 1.1 matches column

Matching incoming DHCP options.

### 1.2 static_hosts column

Static leases.

### 1.3 ranges column

Dynamic IP address ranges.

### 1.4 dhcp_options column

DHCP options settings.

### 1.5 BOOTP Options Configuration group

#### 1.5.1 bootp column

Key-value pairs that specifies BOOTP options for the DHCP clients.

#### 1.5.2 bootp : match tag key

The filename is keyed by match tag. If no key is specified, default key is
no_matching_tag.

