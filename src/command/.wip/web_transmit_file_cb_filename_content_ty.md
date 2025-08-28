## WEB TRANSMIT FILE cb%, filename$, content-type$

Constructs an HTTP 1.1 header with the ’content-type$’ as specified, sends itand then sends the contents of the file to the open TCP connection cb% and oncompletion, closes the connection.’content-type$’ is a MIME type expressed as a string. Eg, "image/jpeg"