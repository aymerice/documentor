# DHCP_Server

![DHCP_Server_table_img](http://www.plantuml.com/plantuml/img/0S41Flv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo14I4DGKt9sNqrXT6De2cDiONDp84H8Gr1JSdPVKc5kPsKAOsnXStCWLb962cDiONDp84H8Gr1VKsLoTcLo2cDiONDp84H8Gr1JSdPVKtHXT6bZNqXlStGAOsnXStCWH4X3K5DoTbzFS7HfRsuAVGf4I4DGNrDbSdPbSY0jP2q-84H8Gr1JSdPVKtHXT6bZNqXlStGAH4X3K5zJPN9sPN8WBMGjFY14I4DGKt9sNqrXT6De2aH8Gr1VKsLoTcLo82raBJuWH4X3K5DoTbzIOMvdPGf4I4DGNrDbSdPbSY0jP2q-84H8Gr1JSdPVJt1qQMzk2aH8Gr1VKsLoTcLo83mjTIqWLb962cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

DHCP Server configuration.

## 1. Configuration

### 1.1 matches

**Type**: _uuid_ **refTable**: [DHCPSrv_Match](dhcpsrv_match.html) **refType**: _strong_



Matching incoming DHCP options.

### 1.2 static_hosts

**Type**: _uuid_ **refTable**: [DHCPSrv_Static_Host](dhcpsrv_static_host.html) **refType**: _strong_



Static leases.

### 1.3 ranges

**Type**: _uuid_ **refTable**: [DHCPSrv_Range](dhcpsrv_range.html) **refType**: _strong_



Dynamic IP address ranges.

### 1.4 dhcp_options

**Type**: _uuid_ **refTable**: [DHCPSrv_Option](dhcpsrv_option.html) **refType**: _strong_



DHCP options settings.

### 1.5 BOOTP Options Configuration

#### 1.5.1 bootp

**Type**: _string->string_

Key-value pairs that specifies BOOTP options for the DHCP clients.

#### 1.5.2 bootp : match tag

**Type**: _string_

The filename is keyed by match tag. If no key is specified, default key is
no_matching_tag.

## 2. Ungrouped

### 2.1 other_config

**Type**: _string->string_

