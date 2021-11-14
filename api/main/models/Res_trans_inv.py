from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db
from main.models import AddInf, BaseModel


class Res_trans_inv(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_trans_inv"
	ResTrInvId = db.Column("ResTrInvId",db.Integer,nullable=False,primary_key=True)
	ResTrInvGuid = db.Column("ResTrInvGuid",UUID(as_uuid=True),unique=True)
	ResTrInvTypeId = db.Column("ResTrInvTypeId",db.Integer,db.ForeignKey("tbl_dk_res_trans_inv_type.ResTrInvTypeId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	WhIdIn = db.Column("WhIdIn",db.Integer,db.ForeignKey("tbl_dk_warehouse.WhId"))
	WhIdOut = db.Column("WhIdOut",db.Integer,db.ForeignKey("tbl_dk_warehouse.WhId"))
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	ResTrInvRegNo = db.Column("ResTrInvRegNo",db.String(100),nullable=False)
	ResTrInvDesc = db.Column("ResTrInvDesc",db.String(500))
	ResTrInvDate = db.Column("ResTrInvDate",db.DateTime,default=datetime.now)
	ResTrInvTotal = db.Column("ResTrInvTotal",db.Float,default=0.0)
	ResTrInvExpAmount = db.Column("ResTrInvExpAmount",db.Float,default=0.0)
	ResTrInvTaxAmount = db.Column("ResTrInvTaxAmount",db.Float,default=0.0)
	ResTrInvFTotal = db.Column("ResTrInvFTotal",db.Float,default=0.0)
	ResTrInvFTotalInWrite = db.Column("ResTrInvFTotalInWrite",db.String(100))
	ResTrInvModifyCount = db.Column("ResTrInvModifyCount",db.Integer,default=0)
	ResTrInvPrintCount = db.Column("ResTrInvPrintCount",db.Integer,default=0)
	Res_trans_inv_line = db.relationship("Res_trans_inv_line",backref='res_trans_inv',lazy=True)
	Rp_acc_transaction = db.relationship("Rp_acc_transaction",backref='res_trans_inv',lazy=True)

	def to_json_api(self):
		data = {
			"ResTrInvId": self.ResTrInvId,
			"ResTrInvGuid": self.ResTrInvGuid,
			"ResTrInvTypeId": self.ResTrInvTypeId,
			"CurrencyId": self.CurrencyId,
			"CId": self.CId,
			"DivId": self.DivId,
			"WhIdIn": self.WhIdIn,
			"WhIdOut": self.WhIdOut,
			"EmpId": self.EmpId,
			"ResTrInvRegNo": self.ResTrInvRegNo,
			"ResTrInvDesc": self.ResTrInvDesc,
			"ResTrInvDate": self.ResTrInvDate,
			"ResTrInvTotal": self.ResTrInvTotal,
			"ResTrInvExpAmount": self.ResTrInvExpAmount,
			"ResTrInvTaxAmount": self.ResTrInvTaxAmount,
			"ResTrInvFTotal": self.ResTrInvFTotal,
			"ResTrInvFTotalInWrite": self.ResTrInvFTotalInWrite,
			"ResTrInvModifyCount": self.ResTrInvModifyCount,
			"ResTrInvPrintCount": self.ResTrInvPrintCount
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data