# SNMP_Trap

![SNMP_Trap_table_img](http://www.plantuml.com/plantuml/img/0TC0BFz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKqvDK5zKSc5m2dqAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

## 1. configuration

### 1.1 community_name

**Type**: _string_

SNMPv1/SNMPv2c community strings. The default community string is "public".

### 1.2 receiver_address

**Type**: _string_

The IP address of the trap receiver.

### 1.3 version

**Type**: _string_

Trap/inform version. The default version is "v2c".

### 1.4 type

**Type**: _string_

Trap type. The default type is "trap".

### 1.5 receiver_udp_port

**Type**: _integer_

The UDP port of the trap receiver.

