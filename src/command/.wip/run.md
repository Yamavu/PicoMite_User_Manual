

### RUN or

Run a program. If ‘file$’ is not supplied then run the program currently held in program

### RUN [file$] [, cmdline$]

memory. If ‘file$’ is supplied then run the named file from the Flash or SD Card filesystem. If ‘file$’ does not contain a '.BAS' extension then one will be automatically added. If ‘cmdline$’ is supplied then pass its value to the MM.CMDLINE$ constant of the program when it runs. If ‘cmdline’$ is not supplied then an empty string value is passed to MM.CMDLINE$.. Notes: