# Syslog_Remote

![Syslog_Remote_table_img](http://www.plantuml.com/plantuml/img/0Gi1zFv0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo1JUNDiRsTVKcLjRtHb2dqAKtbpR6zdNr9bRMzqPI0yBMGj85DvStHbRGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Each entry contains the configuration of the remote syslog server to forward
syslog messages.

## 1. Configuration

### 1.1 remote_host

**Type**: _string_

FQDN or host name or IPv4 address or IPv6 address of the syslog server.

### 1.2 port_number

**Type**: _integer_

Port number on which syslog server is listening. Default is `514` for UDP
protocol and `1470` for TCP protocol.

### 1.3 severity

**Type**: _string_

Filter syslog messages with severity.  Only messages with severity higher than
or equal to the specified value will be sent to the remote server. Default is
`debug`.

### 1.4 transport

**Type**: _string_

Transport layer protocol used to forward messages to the server. Default is
`udp`

