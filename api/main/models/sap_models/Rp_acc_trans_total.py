from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db
from . import BaseModel
from main.base.dataMethods import apiDataFormat


class Rp_acc_trans_total(BaseModel, db.Model):
	__tablename__ = "tbl_dk_rp_acc_trans_total"
	RpAccTrTotId = db.Column("RpAccTrTotId",db.Integer,nullable=False,primary_key=True)
	RpAccTrTotGuid = db.Column("RpAccTrTotGuid",UUID(as_uuid=True),unique=True)
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	RpAccTrTotBalance = db.Column("RpAccTrTotBalance",db.Float,default=0.0)
	RpAccTrTotDebit = db.Column("RpAccTrTotDebit",db.Float,default=0.0)
	RpAccTrTotCredit = db.Column("RpAccTrTotCredit",db.Float,default=0.0)
	RpAccTrTotLastTrDate = db.Column("RpAccTrTotLastTrDate",db.DateTime,default=datetime.now)

	def to_json_api(self):
		data = {
			"RpAccTrTotId": self.RpAccTrTotId,
			"RpAccTrTotGuid": self.RpAccTrTotGuid,
			"RpAccId": self.RpAccId,
			"CurrencyId": self.CurrencyId,
			"RpAccTrTotBalance": self.RpAccTrTotBalance,
			"RpAccTrTotDebit": self.RpAccTrTotDebit,
			"RpAccTrTotCredit": self.RpAccTrTotCredit,
			"RpAccTrTotLastTrDate": apiDataFormat(self.RpAccTrTotLastTrDate)
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data