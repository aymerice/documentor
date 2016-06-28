# OSPF_Summary_Address

![OSPF_Summary_Address_table_img](http://www.plantuml.com/plantuml/img/0Ui05Fz0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16NrDrRMrXSdbVGMHaScLpSmfZR65pSo1FKr16Nq5oPM4AVGfFKr16NrDrRMrXSdbVGMHaScLpSo0yBNKj84zJK4PVGN9bOGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. Configuration group

### 1.1 prefix column

The prefix address in A.B.C.D/M format.

### 1.2 other_config : advertise key

This determines whether to advertise the summary address or not. If value is
false then the OSPFv2 router does not advertise this summary address. The
default value is true.

### 1.3 other_config : cost key

The cost of the summary address. The default value is 16777214.

### 1.4 other_config : tag key

The tag for the summarized prefix.

