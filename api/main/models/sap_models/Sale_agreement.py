from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Sale_agreement(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_sale_agreement"
	SaleAgrId = db.Column("SaleAgrId",db.Integer,nullable=False,primary_key=True)
	SaleAgrGuid = db.Column("SaleAgrGuid",UUID(as_uuid=True),unique=True)
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	SaleAgrName = db.Column("SaleAgrName",db.String(100),nullable=False)
	SaleAgrDesc = db.Column("SaleAgrDesc",db.String(500))
	SaleAgrMinOrderPrice = db.Column("SaleAgrMinOrderPrice",db.Float,default=0.0)
	SaleAgrDiscPerc = db.Column("SaleAgrDiscPerc",db.Float,default=0.0)
	SaleAgrMaxDiscPerc = db.Column("SaleAgrMaxDiscPerc",db.Float,default=0.0)
	SaleAgrTaxPerc = db.Column("SaleAgrTaxPerc",db.Float,default=0.0)
	SaleAgrTaxAmount = db.Column("SaleAgrTaxAmount",db.Float,default=0.0)
	SaleAgrUseOwnPriceList = db.Column("SaleAgrUseOwnPriceList",db.Boolean,default=False)
	Sale_card = db.relationship("Sale_card",backref='sale_agreement',lazy=True)
	Sale_agr_res_price = db.relationship("Sale_agr_res_price",backref='sale_agreement',lazy=True)

	def to_json_api(self):
		data = {
			"SaleAgrId": self.SaleAgrId,
			"SaleAgrGuid": self.SaleAgrGuid,
			"CurrencyId": self.CurrencyId,
			"SaleAgrName": self.SaleAgrName,
			"SaleAgrDesc": self.SaleAgrDesc,
			"SaleAgrMinOrderPrice": self.SaleAgrMinOrderPrice,
			"SaleAgrDiscPerc": self.SaleAgrDiscPerc,
			"SaleAgrMaxDiscPerc": self.SaleAgrMaxDiscPerc,
			"SaleAgrTaxPerc": self.SaleAgrTaxPerc,
			"SaleAgrTaxAmount": self.SaleAgrTaxAmount,
			"SaleAgrUseOwnPriceList": self.SaleAgrUseOwnPriceList
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data