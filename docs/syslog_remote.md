# Syslog_Remote

![Syslog_Remote_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuIf8JCvEJ4zLK0hApozH24bCoaajLbAevb80WkISnE9YXU3AufBKN0KR6mMD49sSpFICalIYrDGyJGKxEwvQBYwuefpyzFYWrDpyabJiQhcW1kdgsg4gv-9oICrB0Ja6)

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

