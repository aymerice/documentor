# Q_Profile_Entry

![Q_Profile_Entry_table_img](http://www.plantuml.com/plantuml/img/SoWkIImgAStDuKhEIImkLWYC3oZAJylCIOrtpIifgbImiL7G2D79oKpFA4alIatDqrImi-DoICrB0Me1)

Contains configuration parameters for one queue of one profile.

## 1. Configuration group

### 1.1 local_priorities column

This essential parameter specifies one or more local-priority(s) that are
assigned to this queue.  Packets' local-priority meta-data is initially assigned
by the port's QoS Trust Mode  (see [Port](port.html) qos_config).  If missing, the
queue is not used.

### 1.2 description column

Used for documentation of these queue configuration parameters.

## 2. Hardware Default group

### 2.1 hw_default column

When true, this row contains the hardware default queue profile parameters for
this queue.

