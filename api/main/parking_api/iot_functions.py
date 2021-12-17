import requests
from datetime import datetime

from main.config import Config
from main.parking_api.serial_device_functions import serial_car_presence, serial_open_gates


def check_car_presence(park_type = "entrance"):
	state = False
	try:
		if Config.USE_SERIAL_DEVICE:
			res = serial_car_presence()
			res = int(res.replace('\n', '').strip())
			print("++++++ serial response = ", res)
			state = False if res == 0 else True

		else:
			r = requests.get(f"{Config.IOT_DEVICE_URL}/check-car-presence/?device_key={Config.IOT_DEVICE_KEY}&type={park_type}")
			state = False if int(r.text()) == 0 else True
			ttt = r.text()
			print(ttt, " +++++ ", state)

	except Exception as ex:
		print(f"--clearparking--: {datetime.now()} | check_car_presence exception: {ex}")

	return state


def open_gates(park_type = "entrance", direction = "up"):
	try:
		if Config.USE_SERIAL_DEVICE:
			res = serial_open_gates()
			return True

		else:
			r = requests.get(f"{Config.IOT_DEVICE_URL}/control/?device_key={Config.IOT_DEVICE_KEY}&type={park_type}&direction={direction}")
			ttt = r.text()
			print(ttt, " \/////////")

	except Exception as ex:
		print(f"--clearparking--: {datetime.now()} | open_gates exception: {ex}")
		return False

	return True


def manage_iot_device(park_type = "entrance"):
	if Config.SIMULATE_REQUEST:
		return

	if check_car_presence(park_type):
		if open_gates(park_type):
			print(f"++clearparking++: {datetime.now()} | Opening Gates of {park_type}")
		else:
			print(f"++clearparking++: {datetime.now()} | Unable to open gates of {park_type}")

	# if open_gates(park_type):
	# 	print(f"++clearparking++: {datetime.now()} | ANYWAYS Opening Gates of {park_type}")

	else:
		print(f"--clearparking--: {datetime.now()} | Car is not on the road..")

	return