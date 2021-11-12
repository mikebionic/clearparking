from flask import request, abort, make_response
from datetime import datetime
from sqlalchemy.orm import joinedload
from flask_login import current_user

from main import app, db
from main.models import Access_log, Finger


# http://192.168.1.252:5000/finger_logger/?device_key=finger_secret_key&finger_id=3
@app.route("/finger_logger/")
def finger_logger():
	device_key = request.args.get("device_key",None,str)
	finger_id = request.args.get("finger_id",0,int)
	access_type = request.args.get("access_type",None,str)

	if not device_key:
		abort(400)
	
	if not finger_id and not access_type:
		abort(400)

	if device_key != app.config["DEVICE_SECRET"]:
		abort(401)

	if finger_id:
		this_finger = Finger.query.filter_by(finger_id = finger_id).first()
		if not this_finger:
			this_finger = Finger(
				finger_id = finger_id,
				name = str(datetime.now())
			)
			db.session.add(this_finger)
			db.session.commit()
		
		new_log = Access_log(
			finger_id = this_finger.finger_id,
			access_type = "Fingerprint",
			date = datetime.now()
		)

	else:
		new_log = Access_log(
			access_type = access_type,
			date = datetime.now()
		)

	db.session.add(new_log)
	db.session.commit()

	return make_response('success'), 201


@app.route("/access_logs/")
def access_logs():
	if not current_user.is_authenticated:
		abort(401)

	logs = Access_log.query\
		.options(joinedload(Access_log.finger))\
		.order_by(Access_log.date.desc())\
		.all()

	data = []
	for log in logs:
		log_data = log.to_json()
		log_data["name"] = log.finger.name if log.finger else ''
		data.append(log_data)

	response = {
		"data": data,
		"total": len(logs),
		"message": "Access logs"
	}

	return make_response(response)


@app.route("/fingerprints_data/")
def fingers_data():
	if not current_user.is_authenticated:
		abort(401)

	fingers = Finger.query.all()

	response = {
		"data": [finger.to_json() for finger in fingers],
		"total": len(fingers),
		"message": "Finger data"
	}

	return make_response(response)


@app.route("/configure_fingerprint/", methods=["POST"])
def configure_fingerprint():
	if not current_user.is_authenticated:
		abort(401)
	if request.method == 'POST':
		data = {}

		data = request.get_json()
		finger_id = data.get("finger_id")
		name = data.get("name")

		this_finger = Finger.query.filter_by(finger_id = finger_id).first()

		if this_finger and name:
			this_finger.name = name

			db.session.add(this_finger)
			db.session.commit()
			data = this_finger.to_json()

		response = {
			"data": data,
			"total": 1 if data else 0,
			"message": "Finger data"
		}

		return make_response(response)




cards = {
	"77:A8:3C:3D": "mike",
}

esp_device_key = "rfid_secret"
esp_device_ip = "192.168.1.145"


@app.route("/esp/door/")
def esp_door():
	device_key = request.args.get("device_key")
	command = request.args.get("command")
	data = request.args.get("data")

	if device_key == esp_device_key:

		if data in cards:
			print(cards[data])

			return "ok"

		return "not found"

	print("==========")

	return "err"


@app.route("/door_action/")
def door_action():
	command = request.args.get("command")
	print(command)
	payload = "http://{}/door/?command={}&secret={}".format(esp_device_ip, command, esp_device_key)
	r = requests.get(payload)
	print(r.text)
	return "ok"