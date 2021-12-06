from flask import request, make_response
from sqlalchemy.orm import joinedload

from main import app
from main.models import (
	Rp_acc,
	# Device,
	Rp_acc_trans_total,
	Invoice,
	Inv_line,
	Attendance,
)

@app.route("/clearpark/rp-accs/")
def clearpark_rp_accs():
	rp_accs = Rp_acc.query\
		.options(
			# joinedload(Rp_acc.Device),
			joinedload(Rp_acc.Rp_acc_trans_total)			
		)\
		.order_by(Rp_acc.CreatedDate.desc())\
		.all()
	
	data = []
	for rp_acc in rp_accs:
		rp_data = rp_acc.to_json_api()
		rp_data["Rp_acc_trans_total"] = [total.to_json_api() for total in rp_acc.Rp_acc_trans_total]
		# rp_data["Device"] = [device.to_json_api() for device in rp_acc.Device]
		data.append(rp_data)

	res = {
		"status": 1 if data else 0,
		"data": data,
		"message": "Rp_accs"
	}
	return make_response(res, 200)


@app.route("/clearpark/attendances/")
def clearpark_attendances():
	attendances = Attendance.query\
		.order_by(Attendance.AttDate.desc())\
		.all()
	
	data = []
	for attendance in attendances:
		att_data = attendance.to_json_api()
		data.append(att_data)

	res = {
		"status": 1 if data else 0,
		"data": data,
		"message": "Attendances"
	}
	return make_response(res, 200)


# @app.route("/clearpark/devices/")
# def clearpark_devices():
# 	devices = Device.query\
# 		.options(
# 			joinedload(Device.rp_acc),	
# 		)\
# 		.order_by(Device.CreatedDate.desc())\
# 		.all()
	
# 	data = []
# 	for device in devices:
# 		dev_data = device.to_json_api()
# 		dev_data["Rp_acc"] = device.rp_acc.to_json_api()
# 		data.append(dev_data)

# 	res = {
# 		"status": 1 if data else 0,
# 		"data": data,
# 		"message": "Devices"
# 	}
# 	return make_response(res, 200)