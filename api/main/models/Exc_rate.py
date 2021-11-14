from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel
from main.base.dataMethods import apiDataFormat


class Exc_rate(BaseModel, db.Model):
	__tablename__ = "tbl_dk_exc_rate"
	ExcRateId = db.Column("ExcRateId",db.Integer,nullable=False,primary_key=True)
	ExcRateGuid = db.Column("ExcRateGuid",UUID(as_uuid=True),unique=True)
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	ExcRateDate = db.Column("ExcRateDate",db.DateTime)
	ExcRateInValue = db.Column("ExcRateInValue",db.Float,default=0.0)
	ExcRateOutValue = db.Column("ExcRateOutValue",db.Float,default=0.0)

	def to_json_api(self):
		data = {
			"ExcRateId": self.ExcRateId,
			"ExcRateGuid": self.ExcRateGuid,
			"CurrencyId": self.CurrencyId,
			"ExcRateDate": apiDataFormat(self.ExcRateDate),
			"ExcRateInValue": self.ExcRateInValue,
			"ExcRateOutValue": self.ExcRateOutValue
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data