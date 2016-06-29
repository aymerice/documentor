# sFlow

![sFlow_table_img](http://www.plantuml.com/plantuml/img/0Uu04Vz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2cDiONDp87D6R6zt2dqASqPiRtSWF2raBI1JUNDqPMqAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

A set of sFlow(R) configurations.  sFlow is a protocol for remote monitoring of
switches.

## 1. Ungrouped

### 1.1 sampling_per_speed

**Type**: _string->integer_

The sampling rate can be configured per interface-speed (in Mbps) which means
the rate will be applied only for interfaces that match the speed. For example,
`sflow sampling 1024 1G` means a sampling rate of 1024 is applied to all the
1Gig interfaces on the system. If interface-speed is not specified, the global
rate is applied on the interface.

### 1.2 sampling_per_speed : 40G

**Type**: _integer_

Sampling rate for the 40 Gigabit interfaces.

### 1.3 sampling_per_speed : 100G

**Type**: _integer_

Sampling rate for the 100 Gigabit interfaces.

### 1.4 sampling_per_speed : 10G

**Type**: _integer_

Sampling rate for the 10 Gigabit interfaces.

### 1.5 sampling_per_speed : 1G

**Type**: _integer_

Sampling rate for the 1 Gigabit interfaces.

### 1.6 statistics

**Type**: _string->string_

Key value pairs that has sampling statistics.

### 1.7 statistics : num_sampled_pkts

**Type**: _string_

Total number of sampled packets sent to the collector.

### 1.8 name

**Type**: _string_

sFlow identifier for the configuration. Should be alphanumeric.

### 1.9 max_datagram

**Type**: _integer_

Maximum number of bytes that will be send in the sflow datagram. If not
specified, the default is 1400 bytes.

### 1.10 agent

**Type**: _string_

Name of the network device whose IP address should be reported as the ``agent
address'' to collectors.  If not specified, the agent IP is derived from the
first interface in alphabetical order.

### 1.11 sampling

**Type**: _integer_

Specifies the rate at which packets should be sampled and sent to the collector.
If not specified, rate defaults to 4096, which means one out of 4096 packets, on
average, will be sent to the collector.

### 1.12 header

**Type**: _integer_

Number of bytes of a sampled packet to send to the collector. If not specified,
the default is 128 bytes.

### 1.13 agent_addr_family

**Type**: _string_

Address type of agent address reported. If agent interface has both IPv4 and
IPv6 address configured, then this column selects which address will be used.
Defaults to IPv4.

### 1.14 polling

**Type**: _integer_

Specifies the interval at which counter statistics are send to the collector. If
not specified, interval defaults to 30 seconds

### 1.15 external_ids

**Type**: _string->string_

### 1.16 targets

**Type**: _string_

sFlow collectors in the form `_ip_:_port_`. Port defaults to 6343 if not
specified. Can have multiple collectors. Atleast one target has to be configured
for sflow to be enabled. Collectors can only be reached over vrf_default.

