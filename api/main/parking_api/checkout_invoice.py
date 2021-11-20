
from sqlalchemy.orm import joinedload


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

		resource = Resource.query\
			.filter_by(ResGuid = Config.IOT_RESOURCE_GUID, GCRecord = None)\
			.options(
				joinedload(Resource.Res_price)
			)\
			.first()
		

		
		res_prices_list = [res_price.to_json_api() for res_price in resource.Res_price if res_price.ResPriceTypeId == 2 and not res_price.GCRecord]
		resource_price = res_prices_list[0]["ResPriceValue"]
		current_price = calculate_attendance_price(entered_attendace.AttDate, att_data["AttDate"], resource_price)
		print(current_price)

		this_invoice = {
			"InvGuid": uuid.uuid4(),
			"RpAccId": rp_acc_model.RpAccId
		}

	except Exception as ex:
		print(f"++clearparking++ {datetime.now()} | checkout park invoice exception {ex}")

	return

def calculate_attendance_price(entrance_date, exit_date, resource_price):
	print("datetime minute calculation")