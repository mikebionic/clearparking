import os

from main.config import Config

def serial_car_presence(park_type = "entrance"):
	os_response = None
	try:
		os_response = os.popen(f"{Config.SERIAL_DEVICE_APP_EXECUTION_COMMAND}").read()
	except Exception as ex:
		print(f"Serial_car_presence exception {ex}")

	return os_response

def serial_open_gates(park_type = "entrance", direction = "up"):
	os_response = None
	try:
		serial_type = "writeup" if direction == "up" else "writedown"
		os_response = os.popen(f"{Config.SERIAL_DEVICE_APP_EXECUTION_COMMAND} -t={serial_type}").read()
	except Exception as ex:
		print(f"serial_open_gates exception {ex}")

	return os_response

def serial_print_invoice(id):
	os_response = None
	try:
		if Config.USE_SERIAL_PRINTER:
			os_response = os.popen(f"{Config.SERIAL_PRINTER_EXECUTION_COMMAND} {id}").read()
	except Exception as ex:
		print(f"serial_print_invoice exception {ex}")

	return os_response