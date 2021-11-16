from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel
from main.base.dataMethods import apiDataFormat


class Device(AddInf, BaseModel, db.Model, UserMixin):
	__tablename__ = "tbl_dk_device"
	DevId = db.Column("DevId",db.Integer,nullable=False,primary_key=True)
	DevGuid = db.Column("DevGuid",UUID(as_uuid=True),unique=True)
	DevUniqueId = db.Column("DevUniqueId",db.String(100),nullable=False)
	UId = db.Column("UId",db.Integer,db.ForeignKey("tbl_dk_users.UId"))
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	DevName = db.Column("DevName",db.String(200))
	DevDesc = db.Column("DevDesc",db.String(500))
	AllowedDate = db.Column("AllowedDate",db.DateTime)
	DisallowedDate = db.Column("DisallowedDate",db.DateTime)
	IsAllowed = db.Column("IsAllowed",db.Boolean,default=False)
	DevVerifyDate = db.Column("DevVerifyDate",db.DateTime)
	DevVerifyKey = db.Column("DevVerifyKey")

	def get_id(self):
		return (self.DevId)

	def to_json_api(self):
		data = {
			"DevId": self.DevId,
			"DevGuid": self.DevGuid,
			"DevUniqueId": self.DevUniqueId,
			"UId": self.UId,
			"RpAccId": self.RpAccId,
			"DevName": self.DevName,
			"DevDesc": self.DevDesc,
			"AllowedDate": apiDataFormat(self.AllowedDate),
			"DisallowedDate": apiDataFormat(self.DisallowedDate),
			"IsAllowed": self.IsAllowed,
			"DevVerifyDate": apiDataFormat(self.DevVerifyDate),
			"DevVerifyKey": self.DevVerifyKey
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data