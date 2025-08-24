WiFi and Internet Functions
WEBMITE VERSION ONLY
This chapter provides an overview of the WiFi and Internet features implemented in the WebMite version for
the Raspberry Pi Pico W and the Raspberry Pi Pico 2 W.
These functions are complex and, as a result, a few points should be noted:
 Implementing the Internet protocols uses a lot of the resources of the processor (particularly RAM) so
the WebMite firmware should only be used where WiFi and Internet connectivity are important and
some performance impact can be tolerated compared to the standard Raspberry Pi Pico.
 This manual describes how the WebMite interfaces with the WiFi and Internet protocols and provides
some simple examples but it does not describe HTML, TCP and the many other protocols and
conventions involved. They can be confusing for the newcomer who will need to consult some of the
many primers available on the web.
 While processing complex Internet protocols the WebMite firmware can get confused and hang or throw
an error and return to the command prompt. To allow for this, programs should use the WATCHDOG
feature to recover from such situations. It is also recommended that from time to time (eg, once a week)
the program should force a reboot using CPU RESTART to ensure that the protocol stacks are reset.

Connecting to a WiFi Network
Before you do anything, you need to enable the WiFi feature on the WebMite and this is done with the
following command entered at the command prompt:
OPTION WIFI ssid, password

Where 'ssid' is the name of the WiFi network and 'password' is the security password used to gain access to the
network. Both are strings and if string constants are used they should be quoted as shown in this example:
OPTION WIFI "MyNetwork", "secret"

When this is entered the WebMite will restart which means that you will lose the USB connection and access to
the console. If you reconnect quickly, you will see the following message:
Connecting to WiFi...
Connected 192.168.1.52

The address given in the last line is the IP address given to the WebMite by the router and will vary depending
on the network. If the WebMite cannot connect you will see this message:
Connecting to WiFi...
failed to connect.

If the connection fails you should check the configuration of your WiFi router:
 The WiFi security must be WPA-PSK with either TKIP or AES encryption (or both).
 The WiFi access must have a password set.
 DHCP must be configured.
This command only needs to be entered once and will be remembered every time your WebMite is restarted.
You can check its setting with the OPTION LIST command. When connected you can also check the IP
address allocated as follows:
> PRINT MM.Info(ip address)
192.168.1.52

With some routers it can take some time or a couple of attempts to connect, so if you are using OPTION
AUTORUN ON, it would be worth inserting something like this at the very start of your program:
DO WHILE MM.INFO(IP ADDRESS) = "0.0.0.0"
IF TIMER > 5000 THEN CPU RESTART
LOOP

This would wait 5 seconds for a connection and restart if still not connected.

Remote Console Access
You can remotely connect to the console of the WebMite via WiFi using Telnet. This is handy if the device is
in a location that is difficult to access. Once connected via Telnet you can do everything that you would
normally do via the USB console including running the editor.

PicoMite User Manual

Page 71

To enable this feature, enter the following at the command prompt: OPTION TELNET CONSOLE ON
This only needs to be entered once and will be remembered every time your WebMite is restarted. It will also
cause the WebMite to restart so you will need to reconnect to the USB console.
Tera Term ( http://tera-term.en.lo4d.com ) supports Telnet and is recommended for this task as it has a good
VT100 emulation and supports the XModem file transfer protocol.

File Transfer
Files can be transferred to and from the WebMite via XModem or TFTP. XModem is supported by Tera Term
and will operate over Telnet the same as it does over a direct serial connection. However TFTP is much faster
and more reliable than XModem so it is the recommended method of transferring files to and from the
WebMite.
A TFTP server on the WebMite is automatically enabled when you are connected to a WiFi network so nothing
is needed there. You do need a TFTP client for your PC and many different implementations are available for
Windows, Mac OS and Linux. Note that many tutorials on TFTP discuss setting up a TFTP server - this is not
needed, you only need a client.
For Windows a TFTP client is included in the operating system but it needs to be enabled via the Control Panel.
To do this select:
Control Panel -> Programs and Features -> Turn Windows features on or off

Then scroll down the list and tick TFTP Client.
To send a file from your PC to the WebMite run the following in a Command or Power Shell window on your
Windows PC (‘IP-Addr’ is the IP address of the WebMite):
TFTP -i IP-Addr PUT filename

And to copy a file from the WebMite to your PC:
TFTP -i IP-Addr GET filename

To list the functions of the TFTP client use the following:
TFTP -h

An alternative and simple graphical Windows TFTP client is: http://www.3iii.dk/linux/dd-wrt/tftp2.exe

Getting the Time
A common first step in a program is to get the time/date and set the clock in the WebMite. This action also
confirms that the WebMite can reach the internet.
Getting the time is done with the WEB NTP command as follows:
WEB NTP [timeoffset [, NTPserver$]]

Where 'timeoffset' is the time zone that you are in and "NTPserver$" is the name or IP address of the time
server to use. This last parameter is optional and if left out the firmware will use a public timeserver pool. If
the 'timeoffset' parameter is also omitted the WebMite's clock will be set to UTC.
This is a typical example for a device in the Los Angeles time zone:
> WEB NTP -10
ntp address 27.124.125.251
got ntp response: 08/03/2023 05:34:57

If the WebMite does not have access to the Internet, you will get an error. This can be trapped using the ON
ERROR SKIP command and a suitable action taken (ie, reboot or display a message for the operator).
For example:
ON ERROR SKIP 3
WEB NTP -10
IF MM.ERRNO THEN WEB NTP -10
IF MM.ERRNO THEN PRINT "Failure to connect to the Internet" : CPU RESTART

The reason why we try the WEB NTP command twice is in case the first attempt failed due to some timing
error (this can happen) – however, it should be successful on the second attempt.

Implementing a Web Server
A popular requirement is to setup a web server which will display data collected by the WebMite in a user
friendly web page.
The first step is to configure the server function using this command at the command prompt:
OPTION TCP SERVER PORT nn

Page 72

PicoMite User Manual

Where 'nn' is the port number to use (normally 80 for a web page). Typically the command will be:
OPTION TCP SERVER PORT 80

As with the other OPTION commands listed above this only needs to be entered once and will be remembered
every time the WebMite is restarted. It will also cause the WebMite to restart and if you reconnect quickly, you
will see the following (with a different IP address):
Starting server at 192.168.1.52 on port 80

The above step configured the WebMite firmware to support a TCP server. In your program you need to start
the server running with the following command:
WEB TCP INTERRUPT InterruptSub

Where 'InterruptSub' is the name of your subroutine that will be called whenever a request is received by the
TCP server. This subroutine can use the command WEB TCP READ to read the incoming request from the
remote client and the command WEB TRANSMIT PAGE can be used to send the requested web page.
For example, below is the full program to implement a simple web page (don't forget to use the OPTION TCP
SERVER command first):
1 DIM buff%(4096/8)
2 WEB TCP INTERRUPT WebInterrupt
3 DO
4
'<do some processing here>'
5 LOOP
6
7 SUB WebInterrupt
8
LOCAL a%, p%, t%, s$
9
FOR a% = 1 To MM.INFO(MAX CONNECTIONS)
10
WEB TCP READ a%, buff%()
11
p% = LINSTR(buff%(),"GET")
12
t% = LINSTR(buff%(),"HTTP")
13
If (p% <> 0) And (t% > p%) Then
14
WEB TRANSMIT PAGE a%,"index.html"
15
ENDIF
16
NEXT a%
17 END SUB

The following describes this program in detail:
Line 1
First a 4K byte buffer is created for the incoming request from the client. This example uses the
long string commands in MMBasic for handling the data and this is the buffer for this (see the next
chapter titled Long Strings for a description of long strings). The size of this buffer will limit the
amount of data received from the client.
Line 2
This starts the server running and specifies the interrupt subroutine for handling incoming requests
as WebInterrupt.
Line 4
This is your main program loop and would be normally collecting data, switching outputs, etc.
Line 7
This is the subroutine that is called every time a request is made by the remote client browser.
Line 9
Loop through all the incoming connections (there could be a number of simultaneous connections).
Line 10 Read the incoming message into the long string buffer.
Lines 11 & 12 Get the locations of key words in the message.
Line 13 Check that the keywords are present and in the correct order.
Line 14 Send the page. This is a file called index.html which is located in the default directory on the
internal flash filesystem or SD card. It is formatted in html which means that it can contain tags
such as <h1>This is a heading</h1>. See A Typical WEB Page below for more.

Inserting Data in the Web Page
Usually you need to insert data generated by the BASIC program in the web page that is transmitted. This is
easily done by inserting the name of the BASIC variable surrounded by curly brackets (ie, { and }) into the text
of the web page.
For example, if your program had a variable called CurrentTemp which had the value of 24 and represented
the current temperature, the following web page: The temperature is {CurrentTemp} would display in
the client's browser as: The temperature is 24.

PicoMite User Manual

Page 73

The identifier between the curly brackets can be a float, integer or string, an array element and even an
expression (ie, A + B). You can also use functions, so if you wanted to format a floating point number with the
correct number of decimal places, etc you could use the formatting function Str$(). Note that an error in the
expression will cause a corresponding error when the WEB TRANSMIT PAGE command is executed.
If you need to use an opening curly bracket in your web page you can use two as a pair (ie, {{) and that will be
changed to a single opening bracket. A closing curly bracket without an opening partner will be untouched.

Sending Multiple Pages
When a remote client requests data without specifying a page it will send the request as GET / HTTP with the
forward slash representing the default page for the server (which is normally index.html). The example above
did not bother checking for this, it just sent the same page for all requests.
However, if your page contains clickable links such as <a href="page2.html">Next page</a> and the
user clicked on this link the remote client will then send another request containing GET /page2.html HTTP.
This can be easily accommodated by examining the requested data between the GET and HTML keywords. For
example, replace line 15 in the above example with the following (s$ is the file requested):
s$ = LGetStr$(buff%(), p% + 4, t% - p% - 5)
IF s$ = "/" THEN
WEB TRANSMIT PAGE a%,"index.html"
ELSE IF s$ = "/page2.html" THEN
WEB TRANSMIT PAGE a%,"page2.html"
ENDIF

this can be extended to as many pages as you need.

Sending an Image
You can insert an image in your web page using the following html code <img src="pix.jpg"/>. When
the remote browser reads this it will send the following request GET /pix.jpg HTTP. You can then send the
requested image using the code shown in bold:
s$ = LGetStr$(buff%(), p% + 4, t% - p% - 5)
IF s$ = "/" THEN
WEB TRANSMIT PAGE a%,"index.html"
ELSE IF s$ = "/page2.html" THEN
WEB TRANSMIT PAGE a%,"page2.html"
ELSE IF s$ = "/pix.jpg" THEN
WEB TRANSMIT FILE a%,"pix.jpg","image/jpeg"
ENDIF

Note that pix.jpg must be a jpeg image residing in the default directory of the internal flash filesystem or SD
card. The WebMite is not a fast server so small and simple images are preferred.
The "image/jpeg" parameter is known as a MIME type and there are many different types, other common
image types are image/bmp, image/png, and image/gif.

Page Not Found (404) Response
If a remote client requests a page or a file which is not supported by your program you can use the WEB
TRANSMIT CODE command to send a 404 error as follows:
s$ = LGetStr$(buff%(), p% + 4, t% - p% - 5)
IF s$ = "/" THEN
WEB TRANSMIT PAGE a%,"index.html"
ELSE IF s$ = "/page2.html" THEN
WEB TRANSMIT PAGE a%,"page2.html"
ELSE IF s$ = "/pix.jpg" THEN
WEB TRANSMIT FILE a%,"pix.jpg","image/jpeg"
ELSE
WEB TRANSMIT CODE a%, 404
ENDIF

Live Graphical Data in a WEB Page
Serving numbers and text in a Web page is useful but often you would like to also include graphical elements
such as pi charts, line graphs, historical trends, etc derived from the data collected by the program This can be
done in a roundabout manner by configuring the WebMite with a virtual display panel, then drawing on that

Page 74

PicoMite User Manual

display using the standard drawing commands (pixel, line, circle, etc) and saving that as a BMP image. This
file can then be included in the web page as an image. In more detail, this process is as follows:
First a virtual display needs to be configured. There are two that you can use, VIRTUAL_C is a 320x240 pixel
image with 16 colours and VIRTUAL_M is a 640x480 pixel monochrome image. For example:
OPTION LCDPANEL VIRTUAL_C

As with the other OPTION commands this must be entered at the command prompt, will cause a restart and
only needs to be entered once.
Then, in your program you can draw images and text on this “display” using the commands described in the
chapter Graphics Commands and Functions. For example:
CIRCLE 100, 100, 50, 1, 1, RGB(red), RGB(blue)
LINE 10, 10, 200, 200, 1, RGB(yellow)

When you are finished, save this image:
SAVE COMPRESSED IMAGE "graph.bmp"

Within the web page that you are serving you can insert this image using the following html code:
<img src="graph.bmp"/>

Finally, in your BASIC program, you must arrange for this file to be sent when the web page is loaded by the
remote browser as described above (see Sending an Image). For example, insert this in the ELSE IF chain
described above:
ELSE IF s$ = "/graph.bmp " THEN
WEB TRANSMIT FILE a%, "graph.bmp", "image/bmp"

Your BASIC program will need to update this file as new data is recorded but, as this only needs to be done
when the remote browser requests the image, it should not cause any excessive wear on the flash memory.

A Complete General Purpose Server
The above pages have described the individual components that make up a web server. Below is an example of
a complete and integrated general purpose server that can handle most requests made by a browser. It works by
examining the extension of the file requested then uses the appropriate WEB TRANSMIT command to send the
requested data. It can be used as a drop in module for any project that needs the WebMite to be a web server.
WEB TCP INTERRUPT WebInterrupt
DO
'<do some processing here>'
LOOP
' sub to handle all web server requests
SUB WebInterrupt
LOCAL a%, p1%, p2%, file$, buff%(4096/8)
FOR a% = 1 To MM.INFO(MAX CONNECTIONS)
WEB TCP READ a%, buff%()
P1% = LINSTR(buff%(),"GET")
P2% = LINSTR(buff%(),"HTTP")
If (p1% <> 0) And (p2% <> 0) And (p2% > p1%) Then
file$ = LCASE$(LGetStr$(buff%(), p1% + 4, p2% - p1% - 5))
IF file$ = "/" THEN file$ = "/index.html"
ON ERROR SKIP
OPEN file$ FOR INPUT AS #1
' check that the file exists
IF MM.ERRNO THEN WEB TRANSMIT CODE a%, 404 : CONTINUE FOR
CLOSE #1
SELECT CASE RIGHT$(file$, 4)
CASE "html", ".htm", ".txt"
WEB TRANSMIT PAGE a%, file$
CASE ".bmp", ".png", ".gif"
WEB TRANSMIT FILE a%, file$, "image/" + RIGHT$(file$, 3)
CASE ".jpg", "jpeg"
WEB TRANSMIT FILE a%, file$, "image/jpeg"
CASE ".ico"
WEB TRANSMIT FILE a%, file$, "image/vnd.microsoft.icon"
END SELECT
ENDIF
NEXT a%
END SUB

PicoMite User Manual

Page 75

Note that all files must be stored in the root of the flash filesystem or SD card and their names must use
lowercase only (the flash filesystem is case sensitive).

A Typical WEB Page
The WEB page to be transmitted via the WEB TRANSMIT PAGE command must be constructed according to
the html standard. It can be as simple as a single line of text with no formatting, ie:
The temperature is {CurrentTemp}

Or you can include some simple formatting:
<title>WebMite</title>
<h2>Temperature Monitor</h2>
The temperature is {CurrentTemp}

Or you can send a complex page. Typically these have head and body sections and delineate text into
paragraphs and use the break tag for spacing. This is the skeleton of such a page:
<html>
<head>
<title>WebMite</title>
</head>
<body>
<h1>This is a heading</h1>
<br>
<p>The temperature is {CurrentTemp}</p>
</body>
</html>

There are many resources on the Internet offering tutorials in html for beginners. A typical example is
http://www.simplehtmlguide.com/. There are also numerous WISWIG HTML editors available. For example:
https://onlinehtmleditor.dev/

Input Fields and Control
Using HTML input fields you can place buttons, check boxes, radio buttons, etc on your WEB page which
allow the user to send requests to the WebMite. This way the user can remotely turn things on/off, set control
parameters and much more - all from the web page served by the WebMite.
To do this you need to insert an HTML form in the web page containing one or more input fields. There are
many types of input fields to choose from (see https://www.w3schools.com/tags/att_input_type.asp ) but in our
simple example we will use two radio buttons to turn off and on a fictitious device.
The following code needs to be inserted in the default web page (ie, index.html):
<form method='get'>
<input name='RB' type='radio' value='OFF' {offb$} onClick='this.form.submit()'> Off
<input name='RB' type='radio' value='ON' {onb$} onClick='this.form.submit()'> On
</form>

This will create two radio buttons which will look like this in a browser:

Note that the above HTML code contains two BASIC variables (offb$ and onb$) which will be substituted by
the WEB TRANSMIT PAGE command. These variables control how the button is displayed. If they are set to
an empty string the button will display as unchecked or, if it is set to the string "checked='checked'", the
button will display as checked. These variables should be initialised when the program starts running.
When the user clicks on the first button the browser will send a request containing: GET /?RB=OFF HTML
and when the second is clicked the request will be: GET /?RB=ON HTML
In the ELSE IF chain in the TCP interrupt subroutine we can act on these requests:
ELSE IF s$ = "/?RB=OFF"
' <insert code here to turn off the device>
offb$ = "checked='checked'" : onb$ = ""
WEB TRANSMIT PAGE a%, "index.html"
ELSE IF s$ = "/?RB=ON"
' <insert code here to turn on the device>
offb$ = "" : onb$ = "checked='checked'"
WEB TRANSMIT PAGE a%, "index.html"

Essentially all that this code does is turn off or on the device as requested, sets the variables onb$ and offb$ to
reflect the new state of the buttons and then resends the whole web page back to the browser.

Page 76

PicoMite User Manual

This example has glossed over the many details involved and you can get extremely complicated if you wished
with multiple inputs involving buttons, text input, drop down lists, password fields, requests for file uploads
and much more. However, to do this, you will have to get deeper into HTML coding. For an example of this
see the Garden Watering Controller project at: https://geoffg.net/retic.html

Implementing a TCP Client
The WebMite can also act as a TCP client to request data from a remote server. This is managed with three
commands. The first is:
WEB OPEN TCP CLIENT Domain$, PortNumber

This opens a TCP connection to Domain$ (for example "openweathermap.org") using the specified
PortNumber (normally 80 for a web page).
With the connection open you can send one or more requests using this command:
WEB TCP CLIENT REQUEST query$, inbuf [, timeout]

The request to be sent is 'query$' and the response will be saved in 'inbuf' which is normally a long string
variable such as buff%(4096/8). The size of this buffer (in bytes) will limit the amount of data received
from the server and should be increased if more data is expected.
'timeout' is optional and is the timeout in milliseconds.
If you are accessing a website 'query$' can be something as simple as "GET / HTTP" which will retrieve the
default page for that website. Your program will then be responsible for picking out the data that you want
from within the response.
Finally, you close the connection with:
WEB CLOSE TCP CLIENT

The following example is a complete program (using these commands) to get the current temperature for the
city of Paris from openweathermap.com. For this to work you need a (free) account with Open Weather Map
( https://openweathermap.org ) which will include an API key, this is a 32 digit hex number that allows you to
make the query. This number should be substituted for the dummy key in the first line.
CONST Key = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
CONST Query = "GET /data/2.5/weather?q=Paris,fra&APPID="+Key+Chr$(13)+Chr$(10)
DIM buff%(4096/8)
WEB OPEN TCP CLIENT "api.openweathermap.org", 80
WEB TCP CLIENT REQUEST Query, buff%()
WEB CLOSE TCP CLIENT
temp = VAL(JSON$(buff%(), "main.temp"))
PRINT "Current temperature in Paris is:" temp - 273

The JSON() function is used to extract the value that we want from the JSON (JavaScript Object Notation)
formatted response.
When this program is run you should see something like:
Connected
Current temperature in Paris is: 13.54

Using UDP
User Datagram Protocol (UDP) is a fast and lightweight protocol used to send messages between devices. It
can be unreliable because it doesn't guarantee that data packets will be delivered or arrive in order, however it is
often used for time sensitive applications that prioritize speed over reliability.
Setting up a UDP server is similar to setting up a TCP server. Firstly UDP is enabled with the following option
entered at the command prompt (this will also cause a restart):
OPTION UDP SERVER PORT port_nbr

In your program you need to start the server running with the following command:
WEB UDP INTERRUPT InterruptSub

Where 'InterruptSub' is the name of your subroutine that will be called whenever a message is received by the
UDP server. When this happens the IP address of the sending device will be held in the read only variable
MM.ADDRESS$ and the received message in MM.MESSAGE$.
You can send a UDP message using:
WEB UDP send ip_address$, port_nbr, message$

The following demonstration uses two WebMites configured with OPTION WIFI on the same network.
Before starting both WebMites must be configured with OPTION UDP SERVER PORT 77.
PicoMite User Manual

Page 77

On the first WebMites make a note of its IP address and enter the following program:
WEB UDP interrupt myint
Do
'<do some processing here>'
Loop
' interrupt subroutine
Sub myint
Print "Received " + mm.message$ + " from " + mm.address
pause 100
WEB UDP send mm.address$, 77, " WebMite #1 message"
End Sub

Then run the program, which will initially sit in a loop doing nothing.
On the second WebMite enter the following program substituting the IP address with the one from the first
WebMite. Then run the program:
WEB UDP interrupt myint
WEB UDP send "192.168.1.127", 77, "Starting UDP echo"
Do
'<do some processing here>'
Loop
' interrupt subroutine
Sub myint
Print "Received " + mm.message$ + " from " + mm.address$
pause 100
WEB UDP send mm.address$, 77, "WebMite #2 message"
End Sub

The result will be a very fast ping pong of UDP messages between the two WebMites.

Sending EMails
When you have a remote device like the WebMite it is useful for it to be able to send emails to raise the alarm
over faults, report on its status and so on. The WebMite can do this using the SMTP protocol to connect to a
server which will then relay the email to its destination.
The following example uses the free SMTP relay service offered by SMTP2GO which allows for 1000 emails
per month (plenty for the WebMite). Note that they do not accept registration requests from people with a
generic free email address (eg, xxx@gmail.com).
To get started you need to create a free login at SMTP2GO ( https://www.smtp2go.com/ ), register a Verified
Sender and create an associated username and password. Both then need to be converted to Base64 encoded
strings (the following website will do this for you: https://www.base64encode.org ).
The Base64 encoded username should be used to replace the nnnnnnnnnn string in the first line of the
following program while the Base64 encoded password should be used to replace the xxxxxxxxxxxx in the
second line. The other four lines at the start of the program should also be replaced with your data:
CONST userBase64$ = "nnnnnnnnnnnn"
CONST paswdBase64$ = "xxxxxxxxxxxx"
CONST mailfrom$ =
"from@server.com"
CONST mailto$ =
"to@server.com"
CONST subject$ =
"Test EMail"
CONST message$ =
"Test of SMTP2GO"
CONST cr = Chr$(13)+Chr$(10)
DIM buff%(4096/8), body$
body$ = "From: " + mailfrom$ + cr + "To: " + mailto$ + cr
body$ = body$ + "Subject: " + subject$ + cr + cr
body$ = body$ + message$ + cr + "." + cr
WEB OPEN TCP CLIENT "mail.smtp2go.com", 2525
WEB TCP CLIENT REQUEST "EHLO" + cr, buff%()
WEB TCP CLIENT REQUEST "AUTH LOGIN" + cr, buff%()
WEB TCP CLIENT REQUEST userBase64$ + cr, buff%()
WEB TCP CLIENT REQUEST paswdBase64$ + cr, buff%()
WEB TCP CLIENT REQUEST "MAIL FROM: " + mailfrom$ + cr, buff%()
Page 78

PicoMite User Manual

WEB TCP CLIENT REQUEST "RCPT TO: " + mailto$ + cr, buff%()
WEB TCP CLIENT REQUEST "DATA" + cr, buff%()
PAUSE 300
WEB TCP CLIENT REQUEST body$, buff%()
PAUSE 300
WEB CLOSE TCP CLIENT
IF LINSTR(buff%(), "250 OK") = 0 THEN
PRINT "Email send failed"
Else
Print "Email sent OK"
EndIf

Note that the mailfrom$ email address used in the above program MUST be the same as that used when you
registered the Verified Sender with SMTP2GO. If they are not the same SMTP2GO will reject the email (this
is an anti spam precaution).
These days using an SMTP relay service is complicated by variations in the SMTP protocol used by each
vendor and the various protections in place to reduce the amount of spam. This example is specific to the
SMTP protocol as used by SMTP2GO however other services can also be used but the program must be
modified to accommodate their own version of the SMTP protocol.

Base 64 Encoding
Base64 is system for converting binary data to a text string that only uses ASCII characters (ie, there are no
control characters). It’s designed to make it easy to send binary data over the internet using protocols which do
not accept binary data and many protocols require its use.
The MATH BASE64 encode/decode function will do the encoding and decoding for you (see the detailed
function list for the full syntax). A typical use is in the above program for sending emails. Rather than use an
external service to convert the username and password to Base64 you can do this in the program using this
function.
For example:
DIM n, userBase64$, paswdBase64$
CONST user$ = "MyUserName"
' user name in plain text
CONST paswd$ = "MyPassword"
' password in plain text
...
' encode the user name and password
n = MATH(BASE64 ENCODE, user$, userBase64$)
n = MATH(BASE64 ENCODE, paswd$, paswdBase64$)
...

MQTT Client
MQTT is a protocol that allows clients like the WebMite to post or retrieve messages on a server (also called a
MQTT broker). This is rather like a bulletin board or web based forum where people post messages which
others can later read at their leisure – the main difference is that MQTT is designed for machine to machine
communications.
A typical example could be a battery powered WebMite which is monitoring the water level in a dam. Twice a
day it would power up, make the measurement, post the result on a MQTT broker and power down again. A
client program (perhaps on a PC) could later read these messages, display the results and graph them.
There are many free brokers available, use Google to search for "free MQTT broker".
The WebMite uses five commands to post or retrieve messages:
WEB MQTT CONNECT Connect to an MQTT broker.
WEB MQTT PUBLISH Publish content to an MQTT topic (ie, post a message).
WEB MQTT SUBSCRIBE
Subscribe to an MQTT topic (ie, retrieve messages).
WEB MQTT UNSUBSCRIBE
Unsubscribe from an MQTT topic.
WEB MQTT CLOSE
Close the MQTT connection.

Ping
The WebMite will respond to a ping message so you can check if it is alive and accessible. If it is connected to
the public Internet a free service like https://uptimerobot.com/ can be used to alert you if it has stopped running.

PicoMite User Manual

Page 79

Streaming audio
The WEB OPEN TCP STREAM and WEB TCP CLIENT STREAM commands can together with the PLAY
STREAM command very simply implement a basic internet radio capability. This is demonstrated in the code
below which receives the UK program ClassicFM. NB: a VS1053 audio codec is required for this program.
Option escape
Option default none
' create the request for the radio site (ClassicFM)
Dim a$="ice-the.musicradio.com"
Dim q$="GET "
Inc q$,"/ClassicFMMP3"
Inc q$," HTTP/1.1\r\n"
Inc q$,"Host: "
Inc q$,a$
Inc q$,"\r\nConnection: close\r\n\r\n"
'create a circular buffer for reading the internet stream and
'read and write pointers
Dim buff%(4095),w%,r%
' Configure the VS1053 and tell it to play from the circular buffer
Play stream buff%(), r%, w%
' Open the internet radio site
WEB open tcp stream a$,80
' Send the request to start the stream using the circular buffer specified
WEB TCP CLIENT STREAM q$, buff%(), r%, w%
'sit back and listen
Do : Pause 500: Loop

Page 80