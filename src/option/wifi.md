## OPTION WIFI ssid$, passwd$,[name$] [,ipaddress$, mask$,gateway$]

*WEBMITE VERSION ONLY*

Configures the firmware to automatically connect to a WiFi network on restart.

`ssid$` is the name of the network and `password$` is the access password. Both are strings and if string constants are used they should be quoted.

Optionally a name for the device can be specified `name$`, otherwise a name is created from the unique device ID.

Optionally, a static IP address, IP mask, and gateway address can be specified as `ipaddress$`, `mask$`, `gateway$`. 

```basic
OPTION WIFI "mysid","mypassword", "myPico", "192.168.1.111", "255.255.255.0", "192.168.1.1"
```