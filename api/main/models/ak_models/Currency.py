from main import db

class Currency_akhasap(db.Model):
	__tablename__ = "tbl_mg_currency"
	CurrencyId = db.Column("currency_id",db.Integer,nullable=False,primary_key=True)
	CurrencyCode = db.Column("currency_name",db.String)
	
	def to_json_api(self):
		data = {
			"CurrencyId": self.CurrencyId,
			"CurrencyCode": self.CurrencyCode,
		}

		return data