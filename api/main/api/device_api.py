from flask import request, make_response

from main import app
from main.models import Device

# add sha key decorator
@app.route("/find-device/", methods=["POST"])
def find_device():
	data = {}

	req = request.get_json()
	DevUniqueId = req.get("data")

	this_device = Device.query.filter_by(DevUniqueId = DevUniqueId).first()

	if this_device:
		if this_device.rp_acc:
			data = this_device.rp_acc.to_json_api()
			data["Device"] = this_device.to_json_api()

	response = {
		"data": data,
		"total": 1 if data else 0,
		"message": "Find Device"
	}

	return make_response(response)
