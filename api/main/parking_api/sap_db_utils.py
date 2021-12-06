from main.models import Device

def device_find_request(DevUniqueId):
	data, message = {}, ""
	try:
		this_device = Device.query.filter_by(DevUniqueId = DevUniqueId).first()
		if not this_device:
			message = f"Device not found {DevUniqueId}"

		if not this_device.rp_acc:
			message = f"Device doesn't have an Rp_acc {DevUniqueId}"

		this_rp_acc = this_device.rp_acc
		data = this_rp_acc.to_json_api()
		data["DevUniqueId"] = this_device.DevUniqueId
		data["DevId"] = this_device.DevId

	except:
		pass

	return data, message