from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db
from main.models import BaseModel
from main.base.dataMethods import apiDataFormat

class Res_total(BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_total"
	ResTotId = db.Column("ResTotId",db.Integer,nullable=False,primary_key=True)
	ResTotGuid = db.Column("ResTotGuid",UUID(as_uuid=True),unique=True)
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	WhId = db.Column("WhId",db.Integer,db.ForeignKey("tbl_dk_warehouse.WhId"))
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	WpId = db.Column("WpId",db.Integer,db.ForeignKey("tbl_dk_work_period.WpId"))
	ResTotBalance = db.Column("ResTotBalance",db.Float,default=0.0)
	ResTotInAmount = db.Column("ResTotInAmount",db.Float,default=0.0)
	ResPendingTotalAmount = db.Column("ResPendingTotalAmount",db.Float,default=0.0)
	ResTotOutAmount = db.Column("ResTotOutAmount",db.Float,default=0.0)
	ResTotLastTrDate = db.Column("ResTotLastTrDate",db.DateTime,default=datetime.now)
	ResTotPurchAvgPrice = db.Column("ResTotPurchAvgPrice",db.Float,default=0.0)

	def to_json_api(self):
		data = {
			"ResTotId": self.ResTotId,
			"ResTotGuid": self.ResTotGuid,
			"ResId": self.ResId,
			"CurrencyId": self.CurrencyId,
			"WhId": self.WhId,
			"CId": self.CId,
			"DivId": self.DivId,
			"WpId": self.WpId,
			"ResTotBalance": self.ResTotBalance,
			"ResTotInAmount": self.ResTotInAmount,
			"ResPendingTotalAmount": self.ResPendingTotalAmount,
			"ResTotOutAmount": self.ResTotOutAmount,
			"ResTotLastTrDate": apiDataFormat(self.ResTotLastTrDate),
			"ResTotPurchAvgPrice": self.ResTotPurchAvgPrice,
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data