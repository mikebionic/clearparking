from main import db

class Exc_rate_akhasap(db.Model):
	__tablename__ = "tbl_mg_exchange_rate"
	ExcRateId = db.Column("exch_id",db.Integer,nullable=False,primary_key=True)
	ExcRateValue = db.Column("exch_value",db.Float)
	CurrencyId = db.Column("currency_id",db.Integer)
	ExcRateType = db.Column("exch_op_type",db.Integer)
	ExcRateDate = db.Column("exch_date",db.DateTime)

	def to_json_api(self):
		data = {
			"ExcRateId": self.ExcRateId,
			"ExcRateValue": self.ExcRateValue,
			"CurrencyId": self.CurrencyId,
			"ExcRateType": self.ExcRateType,
			"ExcRateDate": self.ExcRateDate,
		}

		return data