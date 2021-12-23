import uuid
from datetime import datetime
from main.parking_api.akhasap_lines_convert import akhasap_line_convert
from main import db

from main.models import (
	Invoice,
	Inv_line,
	Resource,
	Attendance,
	Res_price,
	Rp_acc_trans_total,
	User,
)
from main.parking_api.serial_device_functions import serial_print_invoice

from main.config import Config
if Config.DB_STRUCTURE == "saphasap":
	from main.api.common.fetch_and_generate_RegNo import fetch_and_generate_RegNo

if Config.DB_STRUCTURE == "akhasap":
	from main.models import InvoiceFich


def checkout_invoice(data, att_data):
	try:
		entered_attendace = Attendance.query\
			.filter_by(
					RpAccId = att_data["RpAccId"], AttTypeId = 1
				)\
			.order_by(Attendance.AttDate.desc())\
			.first()

		if not entered_attendace:
			print("Entered date not known")
			raise Exception

		main_user = User.query.first()
		resource = Resource.query\
			.filter_by(ResGuid = Config.IOT_RESOURCE_GUID)\
			.first()

		res_prices = Res_price.query.filter_by(ResId = resource.ResId).all()

		res_prices_list = [res_price.to_json_api() for res_price in res_prices if res_price.ResPriceTypeId == 2]
		resource_price = res_prices_list[0]["ResPriceValue"]
		amount, total_price = calculate_attendance_price(entered_attendace.AttDate, att_data["AttDate"], resource_price)

		if not amount or not total_price:
			print(f"Calculate attendance price exception amount: {amount} and price: {total_price}")
			raise Exception

		if Config.DB_STRUCTURE == "saphasap":
			InvRegNo, _ = fetch_and_generate_RegNo(
				main_user.UId,
				main_user.UShortName,
				'sale_invoice_code',
			)
		else:
			InvRegNo = str(datetime.now().timestamp())

		this_invoice_data = {
			"InvGuid": uuid.uuid4(),
			"RpAccId": data["RpAccId"],
			"InvRegNo": InvRegNo,
			"InvTotal": total_price,
			"InvFTotal": total_price,
			"InvTypeId": 8,
		}
		this_invoice = Invoice(**this_invoice_data)
		db.session.add(this_invoice)
		db.session.commit()

		if Config.DB_STRUCTURE == "akhasap":
			this_invoice_fich = InvoiceFich(**this_invoice_data)
			db.session.add(this_invoice_fich)
			db.session.commit()
			this_invoice_fich.InvId = this_invoice.InvId
			this_invoice.FichId = this_invoice_fich.FichId
			db.session.commit()


		if Config.DB_STRUCTURE == "saphasap":
			InvLineRegNo, _ = fetch_and_generate_RegNo(
				main_user.UId,
				main_user.UShortName,
				'invoice_line_code',
			)
		else:
			InvLineRegNo = str(datetime.now().timestamp())

		this_inv_line_data = {
			"InvLineGuid": uuid.uuid4(),
			"ResId": resource.ResId,
			"InvId": this_invoice.InvId,
			"InvLineRegNo": InvLineRegNo,
			"InvLinePrice": resource_price,
			"InvLineTotal": total_price,
			"InvLineFTotal": total_price,
			"InvLineAmount": amount,
		}
		if Config.DB_STRUCTURE == "akhasap":
			this_inv_line_data["FichId"] = this_invoice_fich.FichId

		this_inv_line = Inv_line(**this_inv_line_data)
		db.session.add(this_inv_line)

		# trans_totals = Rp_acc_trans_total.query.filter_by(RpAccId = data["RpAccId"]).all()
		# if not trans_totals:
		# 	new_rp_acc_tr_total = Rp_acc_trans_total(
		# 		RpAccId = data["RpAccId"],
		# 		RpAccTrTotDebit = total_price
		# 	)
		# 	db.session.add(new_rp_acc_tr_total)

		# else:
		# 	trans_totals[0].RpAccTrTotDebit += float(total_price)

		db.session.commit()
		akhasap_line_convert(this_invoice, this_inv_line, data["RpAccId"])

		serial_print_invoice(this_invoice.InvId)

	except Exception as ex:
		print(f"++clearparking++ {datetime.now()} | checkout park invoice exception {ex}")
		return False

	return True

def calculate_attendance_price(entrance_date, exit_date, resource_price):
	amount, price = None, None
	diff = exit_date - entrance_date
	diff_in_minutes = int(diff.total_seconds() / 60)
	amount = diff_in_minutes
	price = resource_price * diff_in_minutes
	return amount, price
