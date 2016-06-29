# Package_Info

![Package_Info_table_img](http://www.plantuml.com/plantuml/img/0Rm0G_z0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWK65ZQs5dPLz9RcPl2dqAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

Each entry contains metadata related to package which is part of the image

## 1. Ungrouped group

### 1.1 src_type column

Corresponds to the type of source pointed to by src_url. Depending on the
src_url, some of the values it can take are - git, https, http, ftp, svn, cvs
etc.

### 1.2 src_url column

This denotes the download location for the source-code of the package. For
example: ops-openvswitch: https://git.openswitch.net/openswitch/ops-openvswitch
sed: http://ftp.gnu.org/gnu/sed/sed-4.2.2.tar.gz

### 1.3 name column

Name of the package. Example: ops-openvswitch, sed, ops-quagga, openssh etc.

### 1.4 version column

If the src_type is a git repository, this will contain the git hash. Otherwise
it will contain the version string (depending on the package). For example: ops-
openvswitch: ac19ac49778adf6cf011a3ef6e0675025f1945b5 sed: 4.2.2

