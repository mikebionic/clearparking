from flask import request, make_response
from sqlalchemy.orm import joinedload

from main import app
from main.models import (
	Rp_acc,
	Rp_acc_trans_total,
	Invoice,
	Inv_line,
	Attendance,
)

from main.config import Config


@app.route("/clearpark/rp-accs/")
def clearpark_rp_accs():
	data = []
	
	rp_accs = Rp_acc.query.order_by(Rp_acc.CreatedDate.desc()).all()
	for rp_acc in rp_accs:
		rp_data = rp_acc.to_json_api()
		this_trans_total = Rp_acc_trans_total.query.filter_by(RpAccId = rp_acc.RpAccId).first()
		rp_data["Rp_acc_trans_total"] = this_trans_total.to_json_api() if this_trans_total else {}

		data.append(rp_data)

	res = {
		"status": 1 if data else 0,
		"data": data,
		"message": "Rp_accs"
	}
	return make_response(res, 200)


@app.route("/clearpark/attendances/")
def clearpark_attendances():
	rpAccId = request.args.get("rpAccId", None, int)
	
	attendance_query = Attendance.query\
		.order_by(Attendance.AttDate.desc())
	if rpAccId:
		attendance_query = attendance_query.filter_by(RpAccId = rpAccId)
	attendances = attendance_query.all()
	
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



@app.route("/clearpark/invoices/")
def clearpark_invoices():
	RpAccId = request.args.get("RpAccId", None, int)

	if not RpAccId:
		rp_accs_list = Rp_acc.query.all()
	
	if RpAccId:
		this_inv_rp_acc = Rp_acc.query.filter_by(RpAccId = RpAccId).first()

	inv_query = Invoice.query\
		.order_by(Invoice.CreatedDate.desc())
	if RpAccId:
		inv_query = inv_query.filter_by(RpAccId = RpAccId)
	invoices = inv_query.all()
	
	data = []
	for inv in invoices:
		inv_data = inv.to_json_api()
		this_inv_lines_list = Inv_line.query.filter_by(InvId = inv.InvId).all()
		inv_data["Inv_lines"] = [inv_line.to_json_api() for inv_line in this_inv_lines_list]

		try:
			if RpAccId:
				inv_data["Rp_acc"] = this_inv_rp_acc.to_json_api()
			else:
				inv_rp_list = [rp_query for rp_query in rp_accs_list if rp_query.RpAccId == inv.RpAccId ]
				inv_data["Rp_acc"] = inv_rp_list[0]

		except:
			inv_data["Rp_acc"] = {}

		data.append(inv_data)

	res = {
		"status": 1 if data else 0,
		"data": data,
		"message": "invoices"
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