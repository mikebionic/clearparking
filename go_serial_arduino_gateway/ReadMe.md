# SmartParking

## Build
```
go build
```

## Run
```
./laser -t=type -p=port -b=baud
```

* Flags
  * -t = *type. Default: read. 
    * writeup. "To turn arduino led up".
    * writedown. "To turn arduino led off"
  * -p = *port. Default: /dev/ttyUSB0. Show where Arduino connected.
  * -b = *baudRate. Default:115200. Write Baud Rate of Serial Connection with Arduino.
  