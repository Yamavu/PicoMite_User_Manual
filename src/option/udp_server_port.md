## OPTION UDP SERVER PORT n

*WEBMITE VERSION ONLY*

Sets up a listening socket on the port specified. Any UDP datagrams received on that port will be processed and the contents saved in `MM.MESSAGE$`. The IP address of the sender will be stored in MM.ADDRESS$. 

Note: If the UDP datagram is longer than 255 characters then any extra is discarded.

Use `OPTION UDP SERVER PORT 0` to disable.
