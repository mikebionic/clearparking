GOOS=windows GOARCH=amd64 go build -o bin/serial_arduino_gateway_console-amd64.exe
GOOS=windows GOARCH=386 go build -o bin/serial_arduino_gateway_console-386.exe

GOOS=windows GOARCH=amd64 go build -ldflags -H=windowsgui -o bin/serial_arduino_gateway-amd64.exe
GOOS=windows GOARCH=386 go build -ldflags -H=windowsgui -o bin/serial_arduino_gateway-386.exe