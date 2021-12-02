
from sqlalchemy.orm import joinedload
import uuid
from datetime import datetime
from main.models import Rp_acc_trans_total
from main.api.common.fetch_and_generate_RegNo import fetch_and_generate_RegNo
from main.models import User
from main import db


from main.models import Invoice, Inv_line, Resource, Attendance
from main.config import Config


def checkout_invoice(rp_acc_model, att_data):
	try:
		entered_attendace = Attendance.query\
			.filter_by(
					RpAccId = att_data["RpAccId"],
					DevId = att_data["DevId"],
					AttTypeId = 1
				)\
			.order_by(Attendance.AttDate.desc())\
			.first()

		if not entered_attendace:
			print("Entered date not known")
			raise Exception

		main_user = User.query.filter_by(UTypeId = 1, GCRecord = None).first()
		resource = Resource.query\
			.filter_by(ResGuid = Config.IOT_RESOURCE_GUID, GCRecord = None)\
			.options(
				joinedload(Resource.Res_price)
			)\
			.first()

		res_prices_list = [res_price.to_json_api() for res_price in resource.Res_price if res_price.ResPriceTypeId == 2 and not res_price.GCRecord]
		resource_price = res_prices_list[0]["ResPriceValue"]
		amount, total_price = calculate_attendance_price(entered_attendace.AttDate, att_data["AttDate"], resource_price)

		if not amount or not total_price:
			print(f"Calculate attendance price exception amount: {amount} and price: {total_price}")
			raise Exception

		InvRegNo, _ = fetch_and_generate_RegNo(
			main_user.UId,
			main_user.UShortName,
			'sale_invoice_code',
		)
		this_invoice_data = {
			"InvGuid": uuid.uuid4(),
			"RpAccId": rp_acc_model.RpAccId,
			"InvRegNo": InvRegNo,
			"InvTotal": total_price,
			"InvFTotal": total_price,
		}
		this_invoice = Invoice(**this_invoice_data)
		db.session.add(this_invoice)
		db.session.commit()
		
		InvLineRegNo, _ = fetch_and_generate_RegNo(
			main_user.UId,
			main_user.UShortName,
			'invoice_line_code',
		)
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
		this_inv_line = Inv_line(**this_inv_line_data)
		db.session.add(this_inv_line)
		
		if not rp_acc_model.Rp_acc_trans_total:
			new_rp_acc_tr_total = Rp_acc_trans_total(
				RpAccId = rp_acc_model.RpAccId,
				RpAccTrTotDebit = total_price
			)
			db.session.add(new_rp_acc_tr_total)
		
		else:
			rp_acc_model.Rp_acc_trans_total[0].RpAccTrTotDebit += total_price
		db.session.commit()
		print(rp_acc_model.RpAccId)

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