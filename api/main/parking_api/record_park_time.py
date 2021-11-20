# from main.models import Attendance
# -*- coding: utf-8 -*-
import uuid
from datetime import datetime
import random

from main.models.Attendance import Attendance
from main import db


def get_att_type_id(type_name):
	current_att_type_id = 1

	att_types = [
		{
			"id": 1,
			"name": "entrance"
		},
		{
			"id": 2,
			"name": "exit"
		}
	]
	for att_type in att_types:
		if att_type["name"] == type_name:
			current_att_type_id = att_type["id"]

	return current_att_type_id


def record_park_time(rp_acc_model, device_model, park_type = "entrance"):
	data, message = {}, ""
	# this could return info about last insertion to use to calculate invoice
	print("Here should be an insertion to attendance table")

	this_att_data = {
		"AttId": random.randint(1,1009990),
		"AttGuid": uuid.uuid4(),
		"RpAccId": rp_acc_model.RpAccId,
		"DevId": device_model.DevId,
		"AttTypeId": get_att_type_id(park_type),
		"AttDate": datetime.now(),
		"AttDesc": f"{rp_acc_model.RpAccUName} | {rp_acc_model.RpAccGuid}, | {park_type} | {str(device_model.to_json_api())}",
	}
	this_attendance = Attendance(**this_att_data)
	db.session.add(this_attendance)
	db.session.commit()
	data = this_attendance.to_json_api()
	return data, message