from main.models import Rp_acc

def device_find_request(DevUniqueId):
	data, message = {}, ""
	try:
		this_rp_acc = Rp_acc.query.filter_by(RpAccRegNo = DevUniqueId).first()
		if not this_rp_acc:
			message = f"Device not found {DevUniqueId}"

		data = this_rp_acc.to_json_api()
		print(data)
		data["DevUniqueId"] = this_rp_acc.RpAccRegNo
		data["DevId"] = this_rp_acc.RpAccId

	except Exception as ex:
		print(ex)

	return data, message