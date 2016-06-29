# CLI_Alias

![CLI_Alias_table_img](http://www.plantuml.com/plantuml/img/0TC0BFz0StHXSdHrRMmAS65ZQs5dPI0YKczlT21KOM9iPNCY87iAOsnXStCWGqn9Nq5iQM5p2dqAQ6baPI1ZQN9ZR6KAQ6baPI1jPMrYPN9p2dDhQMvmON9XRI1jRsvlOsXoRsrb87HoTMKAR6LdPMva879fPsXq2cDlRdHfRdLlSo1iQMvb82qWF68-StHoRsvdF2zYFY1oPMPbScLkOsKAP6zqT6La86nfRcKWBI0yQJvtPM5hF2zfFY1oPMPbScLkOsKAPMvaR6LdPMva2a1bRcHrRMmA)

Alias configurations for the command line interface.

## 1. Ungrouped

### 1.1 alias_name

**Type**: _string_

Shortcut name configured by the user for a set of commands.

### 1.2 other_config

**Type**: _string->string_

### 1.3 alias_definition

**Type**: _string_

The list of commands to be executed when the shortcut is used. Different
commands can be separated by ";". Runtime arguments can be specified using $1,
$2 etc. Any extra arguments, will be added at the end of last command. Eg:
Execute the command "alias mycmd hostname $1; console length $2; console width
$3" to configure "mycmd" as shortcut. On executing "mycmd Switch1 80 24", it
will be expanded to "hostname Switch1; console length 80; console width 24".
"mycmd" will be stored in alias_name" and "hostname $1; console length $2;
console width $3" will be saved in alias_definition.

## 2. Common Columns

The overall purpose of these columns is described under `Common Columns` at the
beginning of this document.

### 2.1 external_ids

**Type**: _string->string_

