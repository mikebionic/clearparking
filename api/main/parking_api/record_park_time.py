# from main.models import Attendance
# -*- coding: utf-8 -*-
import uuid
from datetime import datetime
import random

from main.models import Attendance
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


def sap_record_park_time(data, park_type = "entrance"):
	att_data, message = {}, ""

	this_att_data = {
		"AttId": random.randint(1,1009990),
		"AttGuid": uuid.uuid4(),
		"RpAccId": data["RpAccId"],
		"DevId": data["DevId"],
		"AttTypeId": get_att_type_id(park_type),
		"AttDate": datetime.now(),
		"AttDesc": f'{data["RpAccUName"]} | {data["RpAccGuid"]}, | {park_type} | {data["DevUniqueId"]}',
	}
	this_attendance = Attendance(**this_att_data)
	db.session.add(this_attendance)
	db.session.commit()
	att_data= this_attendance.to_json_api()
	return att_data, message


def ak_record_park_time(data, park_type = "entrance"):
	att_data, message = {}, ""

	this_att_data = {
		"AttId": random.randint(1,1009990),
		"AttGuid": uuid.uuid4(),
		"RpAccId": data["RpAccId"],
		"AttTypeId": get_att_type_id(park_type),
		"AttDate": datetime.now(),
	}
	this_attendance = Attendance(**this_att_data)
	db.session.add(this_attendance)
	db.session.commit()
	att_data= this_attendance.to_json_api()
	return att_data, message
