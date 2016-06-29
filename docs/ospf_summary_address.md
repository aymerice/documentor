# OSPF_Summary_Address

![OSPF_Summary_Address_table_img](http://www.plantuml.com/plantuml/img/0GK1-lv0StHXSdHrRMmAT6zdPNHePN8WUmfZR65pSo1FKr16NrDrRMrXSdbVGMHaScLpSmfZR65pSo1FKr16Nq5oPM4AVGfFKr16NrDrRMrXSdbVGMHaScLpSo0yBNKj84zJK4PVGN9bOGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. Configuration

### 1.1 prefix

**Type**: _string_

The prefix address in A.B.C.D/M format.

### 1.2 other_config

**Type**: _string->string_

### 1.3 other_config : advertise

**Type**: _boolean_

This determines whether to advertise the summary address or not. If value is
false then the OSPFv2 router does not advertise this summary address. The
default value is true.

### 1.4 other_config : cost

**Type**: _integer_

The cost of the summary address. The default value is 16777214.

### 1.5 other_config : tag

**Type**: _string_

The tag for the summarized prefix.

