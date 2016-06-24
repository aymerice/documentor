# ACL

![ACL_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuIf8JCvEJ4zLK0hApozH24bCoaajLbAevb80WkISnE9YXU3AufBKN0KR6mMD49sSpFICalIYrDGyJGKxEwvQBeYQC1z7F-mg8F81-KKb-EGTdNsmIuCDrjMr0wdW0fi2uq2T1UCwfEQb0Fq3)

## 1. Access Control List Status group

### 1.1 in_progress_aces column

The in flight version of the Access Control List.  Access Control Entries (ACE)
specified in this ACL are defined in [ACL_Entry](acl_entry.html)

### 1.2 status : state key

Valid values are 'applied', 'in_progress', 'canceled', 'rejected'

### 1.3 status : code key

Numeric error code.  Expected to be 0 when state is 'applied'

### 1.4 status : message key

Detailed reason for error state.  Expected empty when state is 'applied'

### 1.5 status : version key

The version of cfg_aces that corresponds to this status.

### 1.6 status : status_string key

The status of the last version of 'cfg_aces' column, that has been processed by
switchd.  Accepted values are: 'in_progress', 'applied', 'rejected', and
'canceled'.

### 1.7 in_progress_version column

The version of the 'in_progress' Access Control List.  This value is copied from
the cfg_version column when the ACL processing begins. This value is cleared
when the ACL status is updated to 'applied' or 'rejected.'

### 1.8 cur_aces column

The currently configured version of the Access Control List.  Access Control
Entries (ACE) specified in this version of the ACL are defined in
[ACL_Entry](acl_entry.html)

## 2. Access Control List Configuration group

### 2.1 name column

Name of an Access Control List (ACL).

### 2.2 cfg_version column

The version of the 'cfg_aces' column. This value is incremented by the
management interface - CLI/REST/Web UI, etc. every time it changes the
'cfg_aces' value.

### 2.3 list_type column

Type of an Access Control List  Accepted values: 'ipv4'

### 2.4 cfg_aces column

The desired version of the Access Control List.  Access Control Entries (ACE)
specified in this version of the ACL are defined in [ACL_Entry](acl_entry.html)

