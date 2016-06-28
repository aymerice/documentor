# Syslog_Remote

![Syslog_Remote_table_img](http://www.plantuml.com/plantuml/img/0V403lz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo1JUNDiRsTVKcLjRtHb2dqAKtbpR6zdNr9bRMzqPI0yBMGj85DvStHbRGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

Each entry contains the configuration of the remote syslog server to forward
syslog messages.

## 1. Configuration group

### 1.1 remote_host column

FQDN or host name or IPv4 address or IPv6 address of the syslog server.

### 1.2 port_number column

Port number on which syslog server is listening. Default is `514` for UDP
protocol and `1470` for TCP protocol.

### 1.3 severity column

Filter syslog messages with severity.  Only messages with severity higher than
or equal to the specified value will be sent to the remote server. Default is
`debug`.

### 1.4 transport column

Transport layer protocol used to forward messages to the server. Default is
`udp`

