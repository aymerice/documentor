# Manager

![Manager_table_img](http://www.plantuml.com/plantuml/img/0UK06lz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWKtbpT6Lj2dqAT6zdPNHePN8WUmfZR65pSo1DOMvXPsLo2dqAJM5kOMTbSY0yBMGj85DvStHbRGfeQMHb86DfScDiPGfeQMHb86rbRM9bSdCAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

Configuration for a database connection to an OpenSwitch database (OVSDB)
client.

This table primarily configures the OpenSwitch database (`ovsdb-server`), not
the OpenSwitch switch (`ovs-vswitchd`).  The switch does read the table to
determine what connections should be treated as in-band.

The OpenSwitch database server can initiate and maintain active connections to
remote clients.  It can also listen for database connections.

## 1. Client Failure Detection and Handling group

### 1.1 max_backoff column

Maximum number of milliseconds to wait between connection attempts. Default is
implementation-specific.

### 1.2 inactivity_probe column

Maximum number of milliseconds of idle time on connection to the client before
sending an inactivity probe message.  If OpenSwitch does not communicate with
the client for the specified number of seconds, it will send a probe.  If a
response is not received for the same additional amount of time, OpenSwitch
assumes the connection has been broken and attempts to reconnect.  Default is
implementation-specific. A value of 0 disables inactivity probes.

## 2. Status group

### 2.1 status column

### 2.2 status : locks_waiting key

Space-separated list of the names of OVSDB locks that the connection is
currently waiting to acquire.  Omitted if the connection is not waiting for any
locks.

### 2.3 status : locks_lost key

Space-separated list of the names of OVSDB locks that the connection has had
stolen by another OVSDB client.  Omitted if no locks have been stolen from this
connection.

### 2.4 status : bound_port key

When [target](manager.html#target-column) is `ptcp:` or `pssl:`, this is the TCP port on
which the OVSDB server is listening.  (This is is particularly useful when
[target](manager.html#target-column) specifies a port of 0, allowing the kernel to choose
any available port.)

### 2.5 status : last_error key

A human-readable description of the last error on the connection to the manager;
i.e. `strerror(errno)`.  This key will exist only if an error has occurred.

### 2.6 status : sec_since_connect key

The amount of time since this manager last successfully connected to the
database (in seconds). Value is empty if manager has never successfully
connected.

### 2.7 status : state key

The state of the connection to the manager:

+ __`VOID`__:  Connection is disabled.
+ __`BACKOFF`__:  Attempting to reconnect at an increasing period.
+ __`CONNECTING`__:  Attempting to connect.
+ __`ACTIVE`__:  Connected, remote host responsive.
+ __`IDLE`__:  Connection is idle.  Waiting for response to keep-alive.

These values may change in the future.  They are provided only for human
consumption.

### 2.8 status : locks_held key

Space-separated list of the names of OVSDB locks that the connection holds.
Omitted if the connection does not hold any locks.

### 2.9 status : n_connections key

When [target](manager.html#target-column) specifies a connection method that listens for
inbound connections (e.g. `ptcp:` or `pssl:`) and more than one connection is
actually active, the value is the number of active connections.  Otherwise, this
key-value pair is omitted.

When multiple connections are active, status columns and key-value pairs (other
than this one) report the status of one arbitrarily chosen connection.

### 2.10 status : sec_since_disconnect key

The amount of time since this manager last disconnected from the database (in
seconds). Value is empty if manager has never disconnected.

### 2.11 is_connected column

`true` if currently connected to this manager, `false` otherwise.

## 3. Core Features group

### 3.1 target column

Connection method for managers.

The following connection methods are currently supported:

+ __`ssl:_ip_`[`:_port_`]__:    The specified SSL _port_ on the host at the
given _ip_, which must be expressed as an IP address (not a DNS name).  The
[ssl](system.html#ssl-column) column in the [System](system.html) table must point to a valid SSL
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
listens only on IPv4 (but not IPv6) addresses. The [ssl](system.html#ssl-column) column in
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

When multiple managers are configured, the [target](manager.html#target-column) values must
be unique.  Duplicate [target](manager.html#target-column) values yield unspecified results.

### 3.2 connection_mode column

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

## 4. Connection Parameters group

Additional configuration for a connection between the manager and the OpenSwitch
Database.

### 4.1 other_config column

### 4.2 other_config : dscp key

The Differentiated Service Code Point (DSCP) is specified using 6 bits in the
Type of Service (TOS) field in the IP header. DSCP provides a mechanism to
classify the network traffic and provide Quality of Service (QoS) on IP
networks.  The DSCP value specified here is used when establishing the
connection between the manager and the OpenSwitch.  If no value is specified, a
default value of 48 is chosen.  Valid DSCP values must be in the range 0 to 63.

## 5. Common Columns group

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 5.1 other_config column

### 5.2 external_ids column

