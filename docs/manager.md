# Manager

![Manager_table_img](http://www.plantuml.com/plantuml/img/0Vy00Fz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo1DOMvXPsLo2dqAJM5kOMTbSY0yBMGj85DvStHbRGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCASsjfRd1XSc5j86rlRczZQ79lRMKWT79rPGfiPMTbRcGWScbdQ7GAOszkT6bkTMzp86nfRcKWBI0yOZvpT79lRcSyBs8-879bPcLoPMvZPGfaRtHqPMGWR6bkPI0j83nfFdTbOMiyBsa-879bPcLoPMvZPGfbRcHiPMTbRcGAG6LkP7LjR0e0)

Configuration for a database connection to an OpenSwitch database (OVSDB)
client.

This table primarily configures the OpenSwitch database (`ovsdb-server`), not
the OpenSwitch switch (`ovs-vswitchd`).  The switch does read the table to
determine what connections should be treated as in-band.

The OpenSwitch database server can initiate and maintain active connections to
remote clients.  It can also listen for database connections.

## 1. Client Failure Detection and Handling

### 1.1 max_backoff

**Type**: _integer_

Maximum number of milliseconds to wait between connection attempts. Default is
implementation-specific.

### 1.2 inactivity_probe

**Type**: _integer_

Maximum number of milliseconds of idle time on connection to the client before
sending an inactivity probe message.  If OpenSwitch does not communicate with
the client for the specified number of seconds, it will send a probe.  If a
response is not received for the same additional amount of time, OpenSwitch
assumes the connection has been broken and attempts to reconnect.  Default is
implementation-specific. A value of 0 disables inactivity probes.

## 2. Status

### 2.1 status

**Type**: _string->string_

### 2.2 status : locks_waiting

**Type**: _string_

Space-separated list of the names of OVSDB locks that the connection is
currently waiting to acquire.  Omitted if the connection is not waiting for any
locks.

### 2.3 status : locks_lost

**Type**: _string_

Space-separated list of the names of OVSDB locks that the connection has had
stolen by another OVSDB client.  Omitted if no locks have been stolen from this
connection.

### 2.4 status : bound_port

**Type**: _integer_

When [target](manager.html#target) is `ptcp:` or `pssl:`, this is the TCP port on
which the OVSDB server is listening.  (This is is particularly useful when
[target](manager.html#target) specifies a port of 0, allowing the kernel to choose
any available port.)

### 2.5 status : last_error

**Type**: _string_

A human-readable description of the last error on the connection to the manager;
i.e. `strerror(errno)`.  This key will exist only if an error has occurred.

### 2.6 status : sec_since_connect

**Type**: _integer_

The amount of time since this manager last successfully connected to the
database (in seconds). Value is empty if manager has never successfully
connected.

### 2.7 status : state

**Type**: _string_

The state of the connection to the manager:

+ __`VOID`__:  Connection is disabled.
+ __`BACKOFF`__:  Attempting to reconnect at an increasing period.
+ __`CONNECTING`__:  Attempting to connect.
+ __`ACTIVE`__:  Connected, remote host responsive.
+ __`IDLE`__:  Connection is idle.  Waiting for response to keep-alive.

These values may change in the future.  They are provided only for human
consumption.

### 2.8 status : locks_held

**Type**: _string_

Space-separated list of the names of OVSDB locks that the connection holds.
Omitted if the connection does not hold any locks.

### 2.9 status : n_connections

**Type**: _integer_

When [target](manager.html#target) specifies a connection method that listens for
inbound connections (e.g. `ptcp:` or `pssl:`) and more than one connection is
actually active, the value is the number of active connections.  Otherwise, this
key-value pair is omitted.

When multiple connections are active, status columns and key-value pairs (other
than this one) report the status of one arbitrarily chosen connection.

### 2.10 status : sec_since_disconnect

**Type**: _integer_

The amount of time since this manager last disconnected from the database (in
seconds). Value is empty if manager has never disconnected.

### 2.11 is_connected

**Type**: _boolean_

`true` if currently connected to this manager, `false` otherwise.

## 3. Core Features

### 3.1 target

**Type**: _string_

Connection method for managers.

The following connection methods are currently supported:

+ __`ssl:_ip_`[`:_port_`]__:    The specified SSL _port_ on the host at the
given _ip_, which must be expressed as an IP address (not a DNS name).  The
[ssl](system.html#ssl) column in the [System](system.html) table must point to a valid SSL
configuration when this form is used.   If _port_ is not specified, it currently
defaults to 6632.  In the future, the default will change to 6640, which is the
IANA-defined value.   SSL support is an optional feature that is not always
built as part of OpenSwitch.
+ __`tcp:_ip_`[`:_port_`]__:    The specified TCP _port_ on the host at the
given _ip_, which must be expressed as an IP address (not a DNS name), where
_ip_ can be IPv4 or IPv6 address.  If _ip_ is an IPv6 address, wrap it in square
brackets, e.g. `tcp:[::1]:6632`.   If _port_ is not specified, it currently
defaults to 6632.  In the future, the default will change to 6640, which is the
IANA-defined value.
+ __`pssl:`[_port_][`:_ip_`]__:    Listens for SSL connections on the specified
TCP _port_. Specify 0 for _port_ to have the kernel automatically choose an
available port.  If _ip_, which must be expressed as an IP address (not a DNS
name), is specified, then connections are restricted to the specified local IP
address (either IPv4 or IPv6 address).  If _ip_ is an IPv6 address, wrap in
square brackets, e.g. `pssl:6632:[::1]`.  If _ip_ is not specified then it
listens only on IPv4 (but not IPv6) addresses. The [ssl](system.html#ssl) column in
the [System](system.html) table must point to a valid SSL configuration when this
form is used.   If _port_ is not specified, it currently defaults to 6632.  In
the future, the default will change to 6640, which is the IANA-defined value.
SSL support is an optional feature that is not always built as part of
OpenSwitch.
+ __`ptcp:`[_port_][`:_ip_`]__:    Listens for connections on the specified TCP
_port_. Specify 0 for _port_ to have the kernel automatically choose an
available port.  If _ip_, which must be expressed as an IP address (not a DNS
name), is specified, then connections are restricted to the specified local IP
address (either IPv4 or IPv6 address).  If _ip_ is an IPv6 address, wrap it in
square brackets, e.g. `ptcp:6632:[::1]`.  If _ip_ is not specified then it
listens only on IPv4 addresses.   If _port_ is not specified, it currently
defaults to 6632.  In the future, the default will change to 6640, which is the
IANA-defined value.

When multiple managers are configured, the [target](manager.html#target) values must
be unique.  Duplicate [target](manager.html#target) values yield unspecified results.

### 3.2 connection_mode

**Type**: _string_

If it is specified, this setting must be one of the following strings that
describes how OpenSwitch contacts this OVSDB client over the network:

+ __`in-band`__:   In this mode, this connection's traffic travels over a bridge
managed by OpenSwitch.  With this setting, OpenSwitch allows traffic to and from
the client regardless of the contents of the OpenFlow flow table.  (Otherwise,
OpenSwitch would never be able to connect to the client, because it did not have
a flow to enable it.)  This is the most common connection mode because it is not
necessary to maintain two independent networks.
+ __`out-of-band`__:   In this mode, the client's traffic uses a control network
separate from that managed by OpenSwitch, that is, OpenSwitch does not use any
of its own network devices to communicate with the client. The control network
must be configured separately, before or after `pswitchd` is started.

If not specified, the default is implementation-specific.

## 4. Connection Parameters

Additional configuration for a connection between the manager and the OpenSwitch
Database.

### 4.1 other_config

**Type**: _string->string_

### 4.2 other_config : dscp

**Type**: _integer_

The Differentiated Service Code Point (DSCP) is specified using 6 bits in the
Type of Service (TOS) field in the IP header. DSCP provides a mechanism to
classify the network traffic and provide Quality of Service (QoS) on IP
networks.  The DSCP value specified here is used when establishing the
connection between the manager and the OpenSwitch.  If no value is specified, a
default value of 48 is chosen.  Valid DSCP values must be in the range 0 to 63.

## 5. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 5.1 other_config

**Type**: _string->string_

### 5.2 external_ids

**Type**: _string->string_

