from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from main import db
from main.models import AddInf, BaseModel
from main.base.dataMethods import apiDataFormat
from main.config import Config


class Rp_acc(AddInf, BaseModel, db.Model, UserMixin):
	__tablename__ = "tbl_dk_rp_acc"
	RpAccId = db.Column("RpAccId",db.Integer,nullable=False,primary_key=True)
	RpAccGuid = db.Column("RpAccGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	UId = db.Column("UId",db.Integer,db.ForeignKey("tbl_dk_users.UId"))
	# EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	# GenderId = db.Column("GenderId",db.Integer,db.ForeignKey("tbl_dk_gender.GenderId"))
	# NatId = db.Column("NatId",db.Integer,db.ForeignKey("tbl_dk_nationality.NatId"))
	# RpAccStatusId = db.Column("RpAccStatusId",db.Integer,db.ForeignKey("tbl_dk_rp_acc_status.RpAccStatusId"))
	# ReprId = db.Column("ReprId",db.Integer,db.ForeignKey("tbl_dk_representative.ReprId"))
	ResPriceGroupId = db.Column("ResPriceGroupId",db.Integer,db.ForeignKey("tbl_dk_res_price_group.ResPriceGroupId"))
	# RpAccTypeId = db.Column("RpAccTypeId",db.Integer,db.ForeignKey("tbl_dk_rp_acc_type.RpAccTypeId"))
	WpId = db.Column("WpId",db.Integer,db.ForeignKey("tbl_dk_work_period.WpId"))
	RpAccRegNo = db.Column("RpAccRegNo",db.String(100),nullable=False)
	RpAccUName = db.Column("RpAccUName",db.String(60))
	RpAccUPass = db.Column("RpAccUPass",db.String(60))
	RpAccName = db.Column("RpAccName",db.String(255))
	IsMain = db.Column("IsMain",db.Integer)
	RpAccVisibleIndex = db.Column("RpAccVisibleIndex",db.Integer)
	RpAccViewCnt = db.Column("RpAccViewCnt",db.Integer)
	DbGuid = db.Column("DbGuid",UUID(as_uuid=True))
	DeviceQty = db.Column("DeviceQty",db.Integer)
	UnusedDeviceQty = db.Column("UnusedDeviceQty",db.Integer)
	RpAccAddress = db.Column("RpAccAddress",db.String(500))
	RpAccMobilePhoneNumber = db.Column("RpAccMobilePhoneNumber",db.String(100))
	RpAccHomePhoneNumber = db.Column("RpAccHomePhoneNumber",db.String(100))
	RpAccWorkPhoneNumber = db.Column("RpAccWorkPhoneNumber",db.String(100))
	RpAccWorkFaxNumber = db.Column("RpAccWorkFaxNumber",db.String(100))
	RpAccWebAddress = db.Column("RpAccWebAddress",db.String(255))
	RpAccWebKey = db.Column("RpAccWebKey")
	RpAccZipCode = db.Column("RpAccZipCode",db.String(100))
	RpAccEMail = db.Column("RpAccEMail",db.String(100))
	RpAccFirstName = db.Column("RpAccFirstName",db.String(100))
	RpAccLastName = db.Column("RpAccLastName",db.String(100))
	RpAccPatronomic = db.Column("RpAccPatronomic",db.String(100))
	RpAccBirthDate = db.Column("RpAccBirthDate",db.DateTime)
	RpAccResidency = db.Column("RpAccResidency",db.String(100))
	RpAccPassportNo = db.Column("RpAccPassportNo",db.String(100))
	RpAccPassportIssuePlace = db.Column("RpAccPassportIssuePlace",db.String(100))
	RpAccLangSkills = db.Column("RpAccLangSkills",db.String(100))
	RpAccSaleBalanceLimit = db.Column("RpAccSaleBalanceLimit",db.Float,default=0)
	RpAccPurchBalanceLimit = db.Column("RpAccPurchBalanceLimit",db.Float,default=0)
	RpAccLastActivityDate = db.Column("RpAccLastActivityDate",db.DateTime,default=datetime.now())
	RpAccLastActivityDevice = db.Column("RpAccLastActivityDevice",db.String(100))
	RpAccLatitude = db.Column("RpAccLatitude",db.Float,default=0.0)
	RpAccLongitude = db.Column("RpAccLongitude",db.Float,default=0.0)
	Representative = db.relationship("Representative",backref='rp_acc',foreign_keys='Representative.RpAccId',lazy=True)
	Accounting_info = db.relationship("Accounting_info",backref='rp_acc',lazy=True)
	Contact = db.relationship("Contact",backref='rp_acc',lazy=True)
	Image = db.relationship("Image",backref='rp_acc',lazy=True)
	Location = db.relationship("Location",backref='rp_acc',lazy=True)
	Resource = db.relationship("Resource",backref='last_vendor',lazy=True)
	Inv_line = db.relationship("Inv_line",backref='last_vendor',lazy=True)
	Order_inv_line = db.relationship("Order_inv_line",backref='last_vendor',lazy=True)
	Res_trans_inv_line = db.relationship("Res_trans_inv_line",backref='last_vendor',lazy=True)
	Rp_acc_price_list = db.relationship("Rp_acc_price_list",backref='rp_acc',lazy=True)
	Rp_acc_resource = db.relationship("Rp_acc_resource",backref='rp_acc',lazy=True)
	Rp_acc_trans_total = db.relationship("Rp_acc_trans_total",backref='rp_acc',lazy=True)
	Rp_acc_transaction = db.relationship("Rp_acc_transaction",backref='rp_acc',lazy=True)
	Invoice = db.relationship("Invoice",backref='rp_acc',lazy=True)
	Device = db.relationship("Device",backref='rp_acc',lazy=True)

	def get_reset_token(self, expires_sec=1800):
		s = Serializer(Config.SECRET_KEY,expires_sec)
		return s.dumps({"RpAccId": self.RpAccId}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(Config.SECRET_KEY)
		try:
			RpAccId = s.loads(token)['RpAccId']
		except Exception:
			return None
		return	Rp_acc.query.get(RpAccId)

	def get_id(self):
		return (self.RpAccId)

	def to_json_api(self):
		data = {
			"RpAccId": self.RpAccId,
			"RpAccGuid": self.RpAccGuid,
			"CId": self.CId,
			"DivId": self.DivId,
			"EmpId": self.EmpId,
			"GenderId": self.GenderId,
			"NatId": self.NatId,
			"RpAccStatusId": self.RpAccStatusId,
			"ReprId": self.ReprId,
			"ResPriceGroupId": self.ResPriceGroupId,
			"RpAccTypeId": self.RpAccTypeId,
			"WpId": self.WpId,			
			"RpAccRegNo": self.RpAccRegNo,
			"RpAccUName": self.RpAccUName,
			# "RpAccUPass": self.RpAccUPass,
			"RpAccName": self.RpAccName,
			"IsMain": self.IsMain,
			"RpAccVisibleIndex": self.RpAccVisibleIndex,
			"RpAccViewCnt": self.RpAccViewCnt,
			"RpAccAddress": self.RpAccAddress,
			"DbGuid": self.DbGuid,
			"DeviceQty": self.DeviceQty,
			"UnusedDeviceQty": self.UnusedDeviceQty,
			"RpAccMobilePhoneNumber": self.RpAccMobilePhoneNumber,
			"RpAccHomePhoneNumber": self.RpAccHomePhoneNumber,
			"RpAccWorkPhoneNumber": self.RpAccWorkPhoneNumber,
			"RpAccWorkFaxNumber": self.RpAccWorkFaxNumber,
			"RpAccWebAddress": self.RpAccWebAddress,
			# "RpAccWebKey": self.RpAccWebKey,
			"RpAccZipCode": self.RpAccZipCode,
			"RpAccEMail": self.RpAccEMail,
			"RpAccFirstName": self.RpAccFirstName,
			"RpAccLastName": self.RpAccLastName,
			"RpAccPatronomic": self.RpAccPatronomic,
			"RpAccBirthDate": apiDataFormat(self.RpAccBirthDate),
			"RpAccResidency": self.RpAccResidency,
			"RpAccPassportNo": self.RpAccPassportNo,
			"RpAccPassportIssuePlace": self.RpAccPassportIssuePlace,
			"RpAccLangSkills": self.RpAccLangSkills,
			"RpAccSaleBalanceLimit": self.RpAccSaleBalanceLimit,
			"RpAccPurchBalanceLimit": self.RpAccPurchBalanceLimit,
			"RpAccLastActivityDate": apiDataFormat(self.RpAccLastActivityDate),
			"RpAccLastActivityDevice": self.RpAccLastActivityDevice,
			"RpAccLatitude": self.RpAccLatitude,
			"RpAccLongitude": self.RpAccLongitude
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data
