from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Res_trans_inv_line(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_trans_inv_line"
	ResTrInvLineId = db.Column("ResTrInvLineId",db.Integer,nullable=False,primary_key=True)
	ResTrInvLineGuid = db.Column("ResTrInvLineGuid",UUID(as_uuid=True),unique=True)
	ResTrInvId = db.Column("ResTrInvId",db.Integer,db.ForeignKey("tbl_dk_res_trans_inv.ResTrInvId"))
	UnitId = db.Column("UnitId",db.Integer,db.ForeignKey("tbl_dk_unit.UnitId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	LastVendorId = db.Column("LastVendorId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	ResTrInvLineDesc = db.Column("ResTrInvLineDesc",db.String(500))
	ResTrInvLineAmount = db.Column("ResTrInvLineAmount",db.Float,default=0.0)
	ResTrInvLinePrice = db.Column("ResTrInvLinePrice",db.Float,default=0.0)
	ResTrInvLineTotal = db.Column("ResTrInvLineTotal",db.Float,default=0.0)
	ResTrInvLineExpenseAmount = db.Column("ResTrInvLineExpenseAmount",db.Float,default=0.0)
	ResTrInvLineTaxAmount = db.Column("ResTrInvLineTaxAmount",db.Float,default=0.0)
	ResTrInvLineFTotal = db.Column("ResTrInvLineFTotal",db.Float,default=0.0)
	ResTrInvLineDate = db.Column("ResTrInvLineDate",db.DateTime)
	Res_transaction = db.relationship("Res_transaction",backref='res_trans_inv_line',lazy=True)

	def to_json_api(self):
		data = {
			"ResTrInvLineId": self.ResTrInvLineId,
			"ResTrInvLineGuid": self.ResTrInvLineGuid,
			"ResTrInvId": self.ResTrInvId,
			"UnitId": self.UnitId,
			"CurrencyId": self.CurrencyId,
			"ResId": self.ResId,
			"LastVendorId": self.LastVendorId,
			"ResTrInvLineDesc": self.ResTrInvLineDesc,
			"ResTrInvLineAmount": self.ResTrInvLineAmount,
			"ResTrInvLinePrice": self.ResTrInvLinePrice,
			"ResTrInvLineTotal": self.ResTrInvLineTotal,
			"ResTrInvLineExpenseAmount": self.ResTrInvLineExpenseAmount,
			"ResTrInvLineTaxAmount": self.ResTrInvLineTaxAmount,
			"ResTrInvLineFTotal": self.ResTrInvLineFTotal,
			"ResTrInvLineDate": self.ResTrInvLineDate
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data