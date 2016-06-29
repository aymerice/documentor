# SSL

![SSL_table_img](http://www.plantuml.com/plantuml/img/0Tq08lz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo1JKqmAVGfJKqmWF2raBI1JUNDqPMqAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

SSL configuration for an System.

## 1. Ungrouped group

### 1.1 certificate column

Name of a PEM file containing a certificate, signed by the certificate authority
(CA) used by the controller and manager, that certifies the switch's private
key, identifying a trustworthy switch.

### 1.2 bootstrap_ca_cert column

If set to `true`, then OpenSwitch will attempt to obtain the CA certificate from
the controller on its first SSL connection and save it to the named PEM file. If
it is successful, it will immediately drop the connection and reconnect, and
from then on all SSL connections must be authenticated by a certificate signed
by the CA certificate thus obtained.  _This option exposes the SSL connection to
a man-in-the-middle attack obtaining the initial CA certificate._  It may still
be useful for bootstrapping.

### 1.3 private_key column

Name of a PEM file containing the private key used as the switch's identity for
SSL connections to the controller.

### 1.4 ca_cert column

Name of a PEM file containing the CA certificate used to verify that the switch
is connected to a trustworthy controller.

## 2. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 2.1 external_ids column

