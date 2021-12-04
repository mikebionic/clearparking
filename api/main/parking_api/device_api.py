from flask import request, make_response
from datetime import datetime
from api.main.parking_api.sap_db_utils import smth

from main import app
from main.config import Config
from main.parking_api.iot_functions import manage_iot_device
from main.parking_api.record_park_time import record_park_time
from main.parking_api.checkout_invoice import checkout_invoice
from main.parking_api.iot_sha_required import iot_sha_required


@app.route("/find-device/", methods=["POST"])
@iot_sha_required
def find_device():
	data = {}
	park_type = request.args.get("type","entrance",str)

	try:
		req = request.get_json()
		DevUniqueId = req.get("data")

		data, message = smth()
		if not data:
			print(f"--clearparking--: {datetime.now()} | {message}")

		att_data, _ = record_park_time(this_rp_acc, this_device, park_type)
		if not att_data:
			print("Attendance not recorded...")
			raise Exception

		if park_type == "exit":
			if checkout_invoice(this_rp_acc, att_data):
				manage_iot_device(park_type)
		else:
			manage_iot_device(park_type)

	except Exception as ex:
		print(f"--clearparking--: {datetime.now()} | find-device exception {ex}")

	response = {
		"data": data,
		"total": 1 if data else 0,
		"message": "Find Device"
	}

	return make_response(response)


@app.route("/set-ip/")
def set_ip():
	device_key = request.args.get('device_key')

	try:
		if not device_key:
			raise Exception

		if not device_key == Config.IOT_DEVICE_KEY:
			raise Exception

		app.config.update(IOT_DEVICE_URL = f"http://{request.remote_addr}")

	except Exception as ex:
		print(f"Setting ip failed {ex}")
		return make_response("err", 400)

	return make_response("ok", 200)
