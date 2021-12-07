from main import db

class Res_price(db.Model):
	__tablename__ = "tbl_mg_mat_price"
	ResPriceId = db.Column("price_id",db.Integer,nullable=False,primary_key=True)
	ResPriceTypeId = db.Column("price_type_id",db.Integer)
	ResId = db.Column("material_id",db.Integer)
	CurrencyId = db.Column("currency_id",db.Integer)
	ResPriceValue= db.Column("price_value",db.Integer,nullable=False)
	
	def to_json_api(self):
		data = {
			"ResPriceId": self.ResPriceId,
			"ResPriceTypeId": self.ResPriceTypeId,
			"ResId": self.ResId,
			"CurrencyId": self.CurrencyId,
			"ResPriceValue": self.ResPriceValue,
		}

		return data
