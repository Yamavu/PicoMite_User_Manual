

### REQUEST request$, buff%() [,timeout]

and wait for an answer. 'request$' is a string and is the request to be sent to the server. 'buff%()' is an integer array which will receive the response as a LONGSTRING. The size of this buffer will limit the amount of data received from the server. 'timeout' is the optional time out in milliseconds and defaults to 5000. If the request times out an error will occur, otherwise the received data will be saved in the LONGSTRING 'buff%()'. If the received data is a JSON string then the JSON$() function can be used to parse it.