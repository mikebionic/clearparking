from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Rp_acc_transaction(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_rp_acc_transaction"
	RpAccTransId = db.Column("RpAccTransId",db.Integer,nullable=False,primary_key=True)
	RpAccTransGuid = db.Column("RpAccTransGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	WpId = db.Column("WpId",db.Integer,db.ForeignKey("tbl_dk_work_period.WpId"))
	TransTypeId = db.Column("TransTypeId",db.Integer,db.ForeignKey("tbl_dk_transaction_type.TransTypeId"))
	InvId = db.Column("InvId",db.Integer,db.ForeignKey("tbl_dk_invoice.InvId"))
	ResTransInvId = db.Column("ResTransInvId",db.Integer,db.ForeignKey("tbl_dk_res_trans_inv.ResTrInvId"))
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	RpAccTransName = db.Column("RpAccTransName",db.String(100),nullable=False)
	RpAccTransCode = db.Column("RpAccTransCode",db.String(100))
	RpAccTransDate = db.Column("RpAccTransDate",db.DateTime)
	RpAccTransDebit = db.Column("RpAccTransDebit",db.Float,default=0.0)
	RpAccTransCredit = db.Column("RpAccTransCredit",db.Float,default=0.0)
	RpAccTransTotal = db.Column("RpAccTransTotal",db.Float,default=0.0)

	def to_json_api(self):
		data = {
			"RpAccTransId": self.RpAccTransId,
			"RpAccTransGuid": self.RpAccTransGuid,
			"CId": self.CId,
			"DivId": self.DivId,
			"WpId": self.WpId,
			"TransTypeId": self.TransTypeId,
			"InvId": self.InvId,
			"ResTransInvId": self.ResTransInvId,
			"RpAccId": self.RpAccId,
			"CurrencyId": self.CurrencyId,
			"RpAccTransName": self.RpAccTransName,
			"RpAccTransCode": self.RpAccTransCode,
			"RpAccTransDate": self.RpAccTransDate,
			"RpAccTransDebit": self.RpAccTransDebit,
			"RpAccTransCredit": self.RpAccTransCredit,
			"RpAccTransTotal": self.RpAccTransTotal
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data