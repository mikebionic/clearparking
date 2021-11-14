from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db
from main.models import AddInf, BaseModel


class Inv_line(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_inv_line"
	InvLineId = db.Column("InvLineId",db.Integer,nullable=False,primary_key=True)
	InvLineGuid = db.Column("InvLineGuid",UUID(as_uuid=True),unique=True)
	InvId = db.Column("InvId",db.Integer,db.ForeignKey("tbl_dk_invoice.InvId"))
	UnitId = db.Column("UnitId",db.Integer,db.ForeignKey("tbl_dk_unit.UnitId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	LastVendorId = db.Column("LastVendorId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	InvLineRegNo = db.Column("InvLineRegNo",db.String(100),nullable=False,unique=True)
	InvLineDesc = db.Column("InvLineDesc",db.String(500))
	InvLineAmount = db.Column("InvLineAmount",db.Float)
	InvLinePrice = db.Column("InvLinePrice",db.Float,default=0.0)
	InvLineTotal = db.Column("InvLineTotal",db.Float,default=0.0)
	InvLineExpenseAmount = db.Column("InvLineExpenseAmount",db.Float,default=0.0)
	InvLineTaxAmount = db.Column("InvLineTaxAmount",db.Float,default=0.0)
	InvLineDiscAmount = db.Column("InvLineDiscAmount",db.Float,default=0.0)
	InvLineFTotal = db.Column("InvLineFTotal",db.Float,default=0.0)
	InvLineDate = db.Column("InvLineDate",db.DateTime,default=datetime.now)
	ExcRateValue = db.Column("ExcRateValue",db.Float,default=0.0)
	Inv_line_det = db.relationship("Inv_line_det",backref='inv_line',lazy=True)
	Res_transaction = db.relationship("Res_transaction",backref='inv_line',lazy=True)
	# Rp_acc_transaction = db.relationship("Rp_acc_transaction",backref='inv_line',lazy=True)

	def to_json_api(self):
		data = {
			"InvLineId": self.InvLineId,
			"InvLineGuid": self.InvLineGuid,
			"InvId": self.InvId,
			"UnitId": self.UnitId,
			"CurrencyId": self.CurrencyId,
			"ResId": self.ResId,
			"LastVendorId": self.LastVendorId,
			"InvLineDesc": self.InvLineDesc,
			"InvLineAmount": self.InvLineAmount,
			"InvLinePrice": self.InvLinePrice,
			"InvLineTotal": self.InvLineTotal,
			"InvLineExpenseAmount": self.InvLineExpenseAmount,
			"InvLineTaxAmount": self.InvLineTaxAmount,
			"InvLineDiscAmount": self.InvLineDiscAmount,
			"InvLineFTotal": self.InvLineFTotal,
			"InvLineDate": self.InvLineDate,
			"ExcRateValue": self.ExcRateValue
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data