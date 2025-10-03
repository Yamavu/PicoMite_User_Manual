## WEB

*Only on Webmite*

The WEB commands are used to manage the Internet capability of the WebMite.

### WEB CONNECT [ssid$, passwd$, [name$] [,ipaddress$, mask$, gateway$]]

This command, with no optional parameters, will connect to the default network if possible (as previously set with OPTION WIFI) or with the optional parameters will connect to the network specified and also set up the OPTION WIFI for future use.

### WEB MQTT CONNECT addr$, port, user$, passwd$ [, interrupt]

Connect to an MQTT Broker. 'addr$' is the IP address, 'port' is the port number to use, 'user$' is the user name, 'passwd$' is the account's password and 'interrupt' is optional and if specified is the subroutine to call when a message is received. WEB CONNECT does not disconnect from a previously connected network so should only be used where nothing has been previously set up or where a previously configured network is not active or a previously configured network has failed to connect on boot (no parameters)

### WEB MQTT PUBLISH topic$, msg$, [,qos] [,retain]

Publish content to an MQTT broker topic. 'topic$' is the topic name and 'msg$' is the message/ 'qos' is the optional quality of service with values of 0, 1 or 2 (default is 1).

### WEB MQTT SUBSCRIBE topic$ [,qos]

Subscribe to an MQTT broker topic. 'topic$' is the topic name and 'qos' is the optional quality of service with values of 0, 1 or 2 (default is 1).

### WEB MQTT UNSUBSCRIBE topic$

Unsubscribe from an MQTT broker topic. 'topic$' is the topic name.

### WEB MQTT CLOSE

Close a persistent MQTT Connection.

### WEB NTP [timeoffset [,

Get the date/time from an NTP server and set the internal WebMite date/time

### WEB OPEN TCP CLIENT address$, port

Opens a TCP client connection to a WEB server. 'address$' is a string and is the address of the server to connect to. It can be either a URL (eg, "api.openweathermap.org") or an IP address (eg, "192.168.1.111"). 'port' is the number of the port to use. Used with WEB TCP CLIENT REQUEST to interrogate the server. Note that one CLIENT connection is allowed.

### WEB OPEN TCP STREAM address$, port

Opens a TCP client connection to a WEB server like WEB OPEN TCP CLIENT but connects the WEB TCP CLIENT STREAM receiver logic rather than the logic for WEB TCP CLIENT REQUEST. 'address$' is a string and is the address of the server to connect to. It can be either a URL (eg, "api.openweathermap.org") or an IP address (eg, "192.168.1.111"). 'port' is the number of the port to use. Note that one CLIENT connection is allowed.

### WEB SCAN [array%()]

Scans for all available wifi connections. If ‘array%()’ is specified the output will be stored in a Longstring, otherwise output will be to the console. The command can be used whether ot not an network connection is already active.

### WEB TCP CLIENT

Send a request to the remote server opened with WEB OPEN TCP CLIENT

### WEB TCP CLIENT STREAM command$, buffer%(), readpointer%, writepointer%

Connects to a server previously opened with WEB OPEN TCP STREAM. 'command$' is a string and is the request to be sent to the server. 'buffer%()' is an integer array which will receive the ongoing responses and acts as a circular buffer of bytes received. The firmware maintains the parameter ‘writepointer%’ as the data from the server arrives. ‘readpointer%’ should be maintained by the Basic program as it removes data from the circular buffer. If ‘writepointer%’ catches up with ‘readpointer%’ then ‘readpointer%’ will be incremented to stay one byte ahead and incoming data will be lost. This command is designed to be compatible with the PLAY STREAM command to allow the implementation of streaming internet audio.

### WEB CLOSE TCP CLIENT

Closes the connection to the remote server opened with WEB OPEN TCP CLIENT. This must be done before another open is attempted.

### WEB TCP INTERRUPT

Start the TCP server running. 'InterruptSub' is the subroutine to call when a

### WEB TCP READ cb%, buff%()

Read the data from a potential TCP connection' cb%'. ' buff%()' is an array to receive any data from that connection as a longstring. The size of this buffer will limit the amount of data received from the remote client. If there is nothing received on that connection this will return an empty string (ie, LLEN(buff%())=0). If there is data that has been received then the BASIC program must respond with one of the WEB TRANSMIT commands in order to respond and close the connection.

### WEB TCP SEND cb%, data%()

These two commands allow more flexibility in using the TCP server. Unlike WEB TRANSMIT PAGE or WEB TRANSMIT FILE, WEB TCP SEND does

### WEB TCP CLOSE cb%

not create any sort of header, nor does it close the TCP connection after transmission. It just sends exactly what is in the LONGSTRING data%() and it is up to the Basic programmer to close the connection when appropriate.

### WEB TRANSMIT CODE cb%, nnn%

Send a numerical response to the open TCP connection 'cb%' and then closes the connection. Typical use would be TRANSMIT CODE cb%, 404 to indicate page not found.

### WEB TRANSMIT FILE cb%, filename$, content-type$

Constructs an HTTP 1.1 header with the ’content-type$’ as specified, sends it and then sends the contents of the file to the open TCP connection cb% and on completion, closes the connection. ’content-type$’ is a MIME type expressed as a string. Eg, "image/jpeg"

### WEB TRANSMIT PAGE cb%, filename$ [,buffersize]

Constructs an HTTP 1.1 header, sends it and then sends the contents of the file to the open TCP connection cb% and on completion closes the connection. MMBasic will substitute current values for any MMBasic variables or expressions defined in the file inside curly brackets eg, {myvar%}. Variables can be simple, array elements or expressions. An opening curly bracket can be included in the output by using {{. By default the command allocates a buffer the size of the file + 4096 bytes to build the page to transmit. However, if the page is complex and includes many MMBasic variables that yield text bigger than the variable name it is possible that the buffer will not be big enough. In this case the user can specify the extra space required (defaults to 4096 if not specified)

### WEB UDP INTERRUPT intname

Sets up a BASIC interrupt routine that will be triggered whenever a UDP datagram is received. The contents will be saved in MM.MESSAGE$. The IP address of the sender will be stored in MM.ADDRESS$.

### WEB UDP SEND addr$, port, data$

Used to send a datagram to a remote receiver. In this case the IP address must be specified and can be either a numeric address (eg, "192.168.1.147") or a normal text address (eg, "google.com"). The port number of the receiver must also be specified and the message itself. The SEND command can be used as a response to an incoming message or stand-alone.