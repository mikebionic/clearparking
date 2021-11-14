from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db
from main.models import AddInf, BaseModel
from main.base.dataMethods import configureFloat, apiDataFormat


class Order_inv(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_order_inv"
	OInvId = db.Column("OInvId",db.Integer,nullable=False,primary_key=True)
	OInvGuid = db.Column("OInvGuid",UUID(as_uuid=True),unique=True)
	OInvTypeId = db.Column("OInvTypeId",db.Integer,db.ForeignKey("tbl_dk_order_inv_type.OInvTypeId"))
	InvStatId = db.Column("InvStatId",db.Integer,db.ForeignKey("tbl_dk_inv_status.InvStatId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	UId = db.Column("UId",db.Integer,db.ForeignKey("tbl_dk_users.UId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	WhId = db.Column("WhId",db.Integer,db.ForeignKey("tbl_dk_warehouse.WhId"))
	WpId = db.Column("WpId",db.Integer,db.ForeignKey("tbl_dk_work_period.WpId"))
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	PtId = db.Column("PtId",db.Integer,db.ForeignKey("tbl_dk_payment_type.PtId"))
	PmId = db.Column("PmId",db.Integer,db.ForeignKey("tbl_dk_payment_method.PmId"))
	PaymStatusId = db.Column("PaymStatusId",db.Integer,db.ForeignKey("tbl_dk_payment_status.PaymStatusId"))
	PaymCode = db.Column("PaymCode",db.String(500))
	PaymDesc = db.Column("PaymDesc",db.String(500))
	OInvLatitude = db.Column("OInvLatitude",db.Float,default=0.0)
	OInvLongitude = db.Column("OInvLongitude",db.Float,default=0.0)
	OInvRegNo = db.Column("OInvRegNo",db.String(100),nullable=False,unique=True)
	OInvDesc = db.Column("OInvDesc",db.String(500))
	OInvDate = db.Column("OInvDate",db.DateTime,default=datetime.now)
	OInvTotal = db.Column("OInvTotal",db.Float,default=0.0)
	OInvExpenseAmount = db.Column("OInvExpenseAmount",db.Float,default=0.0)
	OInvTaxAmount = db.Column("OInvTaxAmount",db.Float,default=0.0)
	OInvDiscountAmount = db.Column("OInvDiscountAmount",db.Float,default=0.0)
	OInvPaymAmount = db.Column("OInvPaymAmount",db.Float,default=0.0)
	OInvFTotal = db.Column("OInvFTotal",db.Float,default=0.0)
	OInvFTotalInWrite = db.Column("OInvFTotalInWrite",db.String(100))
	OInvModifyCount = db.Column("OInvModifyCount",db.Integer,default=0)
	OInvPrintCount = db.Column("OInvPrintCount",db.Integer,default=0)
	OInvCreditDays = db.Column("OInvCreditDays",db.Integer,default=0)
	OInvCreditDesc = db.Column("OInvCreditDesc",db.String(100))
	Order_inv_line = db.relationship("Order_inv_line",backref='order_inv',lazy='joined')

	def to_json_api(self):
		data = {
			"OInvId": self.OInvId,
			"OInvGuid": self.OInvGuid,
			"OInvTypeId": self.OInvTypeId,
			"InvStatId": self.InvStatId,
			"CurrencyId": self.CurrencyId,
			"RpAccId": self.RpAccId,
			"CId": self.CId,
			"UId": self.UId,
			"DivId": self.DivId,
			"WhId": self.WhId,
			"WpId": self.WpId,
			"EmpId": self.EmpId,
			"PtId": self.PtId,
			"PmId": self.PmId,
			"PaymStatusId": self.PaymStatusId,
			"PaymCode": self.PaymCode,
			"PaymDesc": self.PaymDesc,
			"OInvLatitude": self.OInvLatitude,
			"OInvLongitude": self.OInvLongitude,
			"OInvRegNo": self.OInvRegNo,
			"OInvDesc": self.OInvDesc,
			"OInvDate": apiDataFormat(self.OInvDate),
			"OInvTotal": configureFloat(self.OInvTotal),
			"OInvExpenseAmount": configureFloat(self.OInvExpenseAmount),
			"OInvTaxAmount": configureFloat(self.OInvTaxAmount),
			"OInvDiscountAmount": configureFloat(self.OInvDiscountAmount),
			"OInvPaymAmount": configureFloat(self.OInvPaymAmount),
			"OInvFTotal": configureFloat(self.OInvFTotal),
			"OInvFTotalInWrite": self.OInvFTotalInWrite,
			"OInvModifyCount": self.OInvModifyCount,
			"OInvPrintCount": self.OInvPrintCount,
			"OInvCreditDays": self.OInvCreditDays,
			"OInvCreditDesc": self.OInvCreditDesc,
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data