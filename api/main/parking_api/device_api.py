from flask import request, make_response
from datetime import datetime

from main import app
from main.models import Device
from main.parking_api.iot_functions import manage_iot_device
from main.parking_api.record_park_time import record_park_time
from main.parking_api.checkout_invoice import checkout_invoice

# add sha key decorator
@app.route("/find-device/", methods=["POST"])
def find_device():
	data = {}
	park_type = request.args.get("type","entrance",str)

	req = request.get_json()
	DevUniqueId = req.get("data")

	this_device = Device.query.filter_by(DevUniqueId = DevUniqueId).first()

	if this_device:
		if this_device.rp_acc:
			this_rp_acc = this_device.rp_acc
			data = this_rp_acc.to_json_api()
			data["Device"] = this_device.to_json_api()

			record_park_time(this_rp_acc, this_device, park_type)
			if park_type == "exit":
				checkout_invoice(this_rp_acc)

			manage_iot_device(park_type)

		else:
			print(f"--clearparking--: {datetime.now()} | Device doesn't have an Rp_acc")
	else:
		print(f"--clearparking--: {datetime.now()} | Device not found {DevUniqueId}")

	response = {
		"data": data,
		"total": 1 if data else 0,
		"message": "Find Device"
	}

	return make_response(response)
