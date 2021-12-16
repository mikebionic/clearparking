from flask import session

from main import login_manager
from . import User, Rp_acc, Device


@login_manager.user_loader
def load_user(id):
	if (not "model_type" in session):
		return None

	if (session["model_type"] == "user"):
		return User.query.get(int(id))

	elif (session["model_type"] == "rp_acc"):
		return Rp_acc.query.get(int(id))

	elif (session["model_type"] == "device"):
		return Device.query.get(int(id))

	return None