# Power_supply

![Power_supply_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuKhEIImkLWWkJIgkB2v9pLMmiL7G2D79oKpFA4alIatDqrImiuCg2iWlJosABoujACYfnAuEOOokhXsAUYw7rBmKe7q0)

Information for a power supply unit (PSU).

## 1. Statistics group

### 1.1 statistics column

Various statistics about the PSU.

### 1.2 statistics : failures key

Number of failures the PSU has experienced since the most recent insertion of
the PSU and boot of the system.  The number of failures for a PSU will be
cleared if the PSU is removed from the system or if the system is rebooted.  For
non removable PSUs, the number of failures will not clear until the system
reboots.  Failures are any events where power delivery from the PSU did not
occur when expected.  This includes unsupported PSU types since their power
delivery is not considered valid even though the PSU itself may not have an
internal failure. Some examples of failures are over current, invalid input
power, and unsupported PSU type.

### 1.3 statistics : warnings key

Number of warnings the PSU has experienced since the most recent insertion of
the PSU and boot of the system.  The number of warnings for a PSU will be
cleared if the PSU is removed from the system or if the system is rebooted.  For
non removable PSUs, the number of warnings will not clear until the system
reboots.  Warnings are any events that do not impair the power delivery from the
PSU but require notification that service may be needed.  Some examples of
warnings are fan failures and over temperature.

## 2. Status group

If the PSU does not have a means to obtain information through software to
populate a field in a Status column, then that field will remain blank.

### 2.1 characteristics column

Electrical characteristics.

### 2.2 characteristics : maximum_power key

Total maximum power capacity that can be supplied by the PSU in Watts.

### 2.3 characteristics : instantaneous_power key

Total instantaneous power supplied by the PSU in Watts.

### 2.4 identity column

PSU identification.

### 2.5 identity : serial_number key

PSU serial number to uniquely identify the PSU.

### 2.6 identity : product_name key

PSU product name identification.  This field is used to determine if the PSU is
supported.

