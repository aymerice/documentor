# ACL

![ACL_table_img](http://www.plantuml.com/plantuml/img/0Ia1rlv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo1MJ45E2cDiONDp851lSdGAOsnXStCWGKDC2dqAGKDC83mkTIuWLan1JWf1GqmWF2raBI1JUNDqPMqAGKDC83mkTIuWK6zoT0feQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

## 1. Access Control List Status

### 1.1 in_progress_aces

**Type**: _integer->uuid_ **refTable**: [ACL_Entry](acl_entry.html) **refType**: _strong_



The in flight version of the Access Control List.  Access Control Entries (ACE)
specified in this ACL are defined in [ACL_Entry](acl_entry.html)

### 1.2 status

**Type**: _string->string_

### 1.3 status : state

**Type**: _string_

Valid values are 'applied', 'in_progress', 'canceled', 'rejected'

### 1.4 status : code

**Type**: _integer_

Numeric error code.  Expected to be 0 when state is 'applied'

### 1.5 status : message

**Type**: _string_

Detailed reason for error state.  Expected empty when state is 'applied'

### 1.6 status : version

**Type**: _integer_

The version of cfg_aces that corresponds to this status.

### 1.7 status : status_string

**Type**: _string_

The status of the last version of 'cfg_aces' column, that has been processed by
switchd.  Accepted values are: 'in_progress', 'applied', 'rejected', and
'canceled'.

### 1.8 in_progress_version

**Type**: _integer_

The version of the 'in_progress' Access Control List.  This value is copied from
the cfg_version column when the ACL processing begins. This value is cleared
when the ACL status is updated to 'applied' or 'rejected.'

### 1.9 cur_aces

**Type**: _integer->uuid_ **refTable**: [ACL_Entry](acl_entry.html) **refType**: _strong_



The currently configured version of the Access Control List.  Access Control
Entries (ACE) specified in this version of the ACL are defined in
[ACL_Entry](acl_entry.html)

## 2. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 2.1 other_config

**Type**: _string->string_

### 2.2 external_ids

**Type**: _string->string_

## 3. Access Control List Configuration

### 3.1 name

**Type**: _string_

Name of an Access Control List (ACL).

### 3.2 cfg_version

**Type**: _integer_

The version of the 'cfg_aces' column. This value is incremented by the
management interface - CLI/REST/Web UI, etc. every time it changes the
'cfg_aces' value.

### 3.3 list_type

**Type**: _string_

Type of an Access Control List  Accepted values: 'ipv4'

### 3.4 cfg_aces

**Type**: _integer->uuid_ **refTable**: [ACL_Entry](acl_entry.html) **refType**: _strong_



The desired version of the Access Control List.  Access Control Entries (ACE)
specified in this version of the ACL are defined in [ACL_Entry](acl_entry.html)

