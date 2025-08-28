## I2C OPEN speed, timeout

Enables the first I2C module in master mode. ‘speed’ is the clock speed (inKHz) to use and must be one of 100, 400 or 1000.‘timeout’ is a value in milliseconds after which the master send and receivecommands will be interrupted if they have not completed. The minimum valueis 100. A value of zero will disable the timeout (though this is notrecommended).