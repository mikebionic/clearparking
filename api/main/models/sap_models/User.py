from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from main import db
from . import AddInf, BaseModel
from main.base.dataMethods import apiDataFormat
from main.config import Config


class User(AddInf, BaseModel, db.Model, UserMixin):
	__tablename__ = "tbl_dk_users"
	UId = db.Column("UId",db.Integer,nullable=False,primary_key=True)
	UGuid = db.Column("UGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	ResPriceGroupId = db.Column("ResPriceGroupId",db.Integer,db.ForeignKey("tbl_dk_res_price_group.ResPriceGroupId"))
	RpAccId = db.Column("RpAccId",db.Integer)
	UFullName = db.Column("UFullName",db.String(100))
	UName = db.Column("UName",db.String(60),nullable=False)
	UEmail = db.Column("UEmail",db.String(100),unique=True)
	UPass = db.Column("UPass",db.String(60),nullable=False)
	URegNo = db.Column("URegNo",db.String(100),unique=True)
	UShortName = db.Column("UShortName",db.String(10))
	EmpId = db.Column("EmpId",db.Integer)
	UTypeId = db.Column("UTypeId",db.Integer,db.ForeignKey("tbl_dk_user_type.UTypeId"))
	ULastActivityDate = db.Column("ULastActivityDate",db.DateTime,default=datetime.now())
	ULastActivityDevice = db.Column("ULastActivityDevice",db.String(100))
	Wish = db.relationship("Wish",backref='user',lazy=True)
	Rating = db.relationship("Rating",backref='user',lazy=True)
	Rp_acc = db.relationship("Rp_acc",backref='user',lazy=True)
	Image = db.relationship("Image",backref='user',lazy=True)
	Device = db.relationship("Device",backref='user',lazy=True)
	Order_inv = db.relationship("Order_inv",backref='user',lazy=True)
	
	def is_admin(self):
		return self.UTypeId == 1

	def get_id(self):
		return (self.UId)

	def get_reset_token(self,expires_sec=1800):
		s = Serializer(Config.SECRET_KEY,expires_sec)
		return s.dumps({"UId": self.UId}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(Config.SECRET_KEY)
		try:
			UId = s.loads(token)['UId']
		except Exception:
			return None
		return User.query.get(UId)

	def to_json_api(self):
		data = {
			"UId": self.UId,
			"UGuid": self.UGuid,
			"CId": self.CId,
			"DivId": self.DivId,
			"RpAccId": self.RpAccId,
			"ResPriceGroupId": self.ResPriceGroupId,
			"UFullName": self.UFullName,
			"UName": self.UName,
			"UEmail": self.UEmail,
			# "UPass": self.UPass,
			"UShortName": self.UShortName,
			"URegNo": self.URegNo,
			"ULastActivityDate": apiDataFormat(self.ULastActivityDate),
			"ULastActivityDevice": self.ULastActivityDevice,
			"EmpId": self.EmpId,
			"UTypeId": self.UTypeId
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data

