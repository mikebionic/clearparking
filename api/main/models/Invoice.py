from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db
from main.models import AddInf, BaseModel
from main.base.dataMethods import configureFloat, apiDataFormat


class Invoice(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_invoice"
	InvId = db.Column("InvId",db.Integer,nullable=False,primary_key=True)
	InvGuid = db.Column("InvGuid",UUID(as_uuid=True),unique=True)
	InvTypeId = db.Column("InvTypeId",db.Integer,db.ForeignKey("tbl_dk_inv_type.InvTypeId"))
	InvStatId = db.Column("InvStatId",db.Integer,db.ForeignKey("tbl_dk_inv_status.InvStatId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	WhId = db.Column("WhId",db.Integer,db.ForeignKey("tbl_dk_warehouse.WhId"))
	WpId = db.Column("WpId",db.Integer,db.ForeignKey("tbl_dk_work_period.WpId")) #?
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	PtId = db.Column("PtId",db.Integer,db.ForeignKey("tbl_dk_payment_type.PtId"))
	PmId = db.Column("PmId",db.Integer,db.ForeignKey("tbl_dk_payment_method.PmId"))
	InvLatitude = db.Column("InvLatitude",db.Float,default=0.0)
	InvLongitude = db.Column("InvLongitude",db.Float,default=0.0)
	InvRegNo = db.Column("InvRegNo",db.String(100),nullable=False,unique=True)
	InvDesc = db.Column("InvDesc",db.String(500))
	InvDate = db.Column("InvDate",db.DateTime,default=datetime.now)
	InvTotal = db.Column("InvTotal",db.Float)
	InvExpenseAmount = db.Column("InvExpenseAmount",db.Float,default=0.0)
	InvTaxAmount = db.Column("InvTaxAmount",db.Float,default=0.0)
	InvDiscountAmount = db.Column("InvDiscountAmount",db.Float,default=0.0)
	InvFTotal = db.Column("InvFTotal",db.Float,default=0.0)
	InvFTotalInWrite = db.Column("InvFTotalInWrite",db.String(100),default=0)
	InvModifyCount = db.Column("InvModifyCount",db.Integer,default=0)
	InvPrintCount = db.Column("InvPrintCount",db.Integer,default=0)
	InvCreditDays = db.Column("InvCreditDays",db.Integer,default=0)
	InvCreditDesc = db.Column("InvCreditDesc",db.String(100))
	Inv_line = db.relationship("Inv_line",backref='invoice',lazy=True)
	Rp_acc_transaction = db.relationship("Rp_acc_transaction",backref='invoice',lazy=True)

	def to_json_api(self):
		data = {
			"InvId": self.InvId,
			"InvGuid": self.InvGuid,
			"InvTypeId": self.InvTypeId,
			"InvStatId": self.InvStatId,
			"CurrencyId": self.CurrencyId,
			"RpAccId": self.RpAccId,
			"CId": self.CId,
			"DivId": self.DivId,
			"WhId": self.WhId,
			"WpId": self.WpId,
			"EmpId": self.EmpId,
			"PtId": self.PtId,
			"PmId": self.PmId,
			"InvLatitude": self.InvLatitude,
			"InvLongitude": self.InvLongitude,
			"InvRegNo": self.InvRegNo,
			"InvDesc": self.InvDesc,
			"InvDate": apiDataFormat(self.InvDate),
			"InvTotal": configureFloat(self.InvTotal),
			"InvExpenseAmount": configureFloat(self.InvExpenseAmount),
			"InvTaxAmount": configureFloat(self.InvTaxAmount),
			"InvDiscountAmount": configureFloat(self.InvDiscountAmount),
			"InvFTotal": configureFloat(self.InvFTotal),
			"InvFTotalInWrite": self.InvFTotalInWrite,
			"InvModifyCount": self.InvModifyCount,
			"InvPrintCount": self.InvPrintCount,
			"InvCreditDays": self.InvCreditDays,
			"InvCreditDesc": self.InvCreditDesc,
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data