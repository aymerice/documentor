# NTP_Association

![NTP_Association_table_img](http://www.plantuml.com/plantuml/img/0JG1o_v0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWJbHGNqjbUGfZR65pSo1EL51VGNDpRsDfONHfRsuAVGfqRsTbT6XbSY1x2cDiONDp85PIHWfz2avKK5z1StDlOsbXT6blRY0jP2q-85PIHWfEL51VGNDpRsDfONHfRsuWBdKkFY1EL51VIsLv2cXfP6KWOsboOsnb2cXfP6KWRMLjOcLoSmfpQsbkS65oOMqWRMzkRsDeSczjPI1qSdLb2cnbPsLkP21oQMTeT0fZRsvqQMvrRtCWR6bkPI0j83nYFdDqSczkPpmlOZuWScLcPN9bRcDb2cHlT7HbP21iQMvb82qWF6a-TsLXQpmlQJuWScLcPN9bRcDb2cLkP6nbPsLkP0f0PMvaTMri)

NTP Client Configuration info related to configured NTP servers and their status
info.`https://www.ietf.org/rfc/rfc5907.txt`

## 1. NTP Association Configuration

### 1.1 key_id

**Type**: _uuid_ **refTable**: [NTP_Key](ntp_key.html) **refType**: _weak_



Key id is used if NTP client wants to connect to an authenticated association.
Key id is not used when using an unauthenticated association.

### 1.2 address

**Type**: _string_

FQDN or ip address for the association.

### 1.3 association_attributes

**Type**: _string->string_

### 1.4 association_attributes : ref_clock_id

**Type**: _string_

The refclock driver ID, if available. A refclock driver ID like "127.127.1.0"
for non uni/multi/broadcast associations

### 1.5 association_attributes : ntp_version

**Type**: _integer_

NTP version to use for when communicating with this association. Default is 3.

### 1.6 association_attributes : prefer

**Type**: _boolean_

Preference flag to suggest for this association. Set this to `true` to enable
preference for this association. Default is false.

### 1.7 vrf

**Type**: _uuid_ **refTable**: [VRF](vrf.html) **refType**: _strong_



Specifies which VRF this association should connect with.

## 2. NTP Association Status

Status information about NTP associations. For more info refer to
`http://doc.ntp.org/4.2.6p5/debug.html`

### 2.1 association_status

**Type**: _string->string_

Key-value pairs that report NTP association status.

### 2.2 association_status : network_delay

**Type**: _string_

Provides round trip delay (in milliseconds) between the switch and the remote
peer or server.

### 2.3 association_status : jitter

**Type**: _string_

Provides jitter (in milliseconds) in the time reported for that remote peer or
server.

### 2.4 association_status : remote_peer_address

**Type**: _string_

Provides the remote peer's ip address being synced to. If FQDN is used as
"address" during config, then this would be the ip address.

### 2.5 association_status : peer_type

**Type**: _string_

Provides information about the remote peer type.

### 2.6 association_status : reference_time

**Type**: _string_

Provides the time (in "day, month date year hh:mm" format) when the server clock
of refid was last adjusted. Eg format Wed, Jan 13 2016  7:56:26.126

### 2.7 association_status : associd

**Type**: _string_

Provides the Association ID mapped for this association. This is an Internal ID.

### 2.8 association_status : reachability_register

**Type**: _string_

Provides status about the last consequetive polls for this peer. (1 bit per
poll)

### 2.9 association_status : remote_peer_ref_id

**Type**: _string_

Provides the reference id used by the remote peer. This can be either another
server or stratum 1 devices like .GPS. .USNO. etc. For more info, refer to
`http://nlug.ml1.co.uk/2012/01/ntpq-p-output/831`

### 2.10 association_status : last_polled

**Type**: _string_

Provides information about when the peer was last polled. (in seconds ago OR 'h'
hours ago OR 'd' days ago). Example 6h, 5d, 5 (this refers to seconds).

### 2.11 association_status : polling_interval

**Type**: _string_

Provides the polling frequency (in seconds) used for this peer.

### 2.12 association_status : root_dispersion

**Type**: _string_

Provides maximum error relative time (in seconds) to primary reference clock.

### 2.13 association_status : stratum

**Type**: _integer_

Provides the remote peer or server stratum level. Range between 1-16.

### 2.14 association_status : peer_status_word

**Type**: _string_

Provides information about the peer status. Refer to link for more info
`https://www.eecis.udel.edu/~mills/ntp/html/decode.html#peer`

### 2.15 association_status : time_offset

**Type**: _string_

Provides Root Mean Square time (in milliseconds) between this local host and the
remote peer or server.

