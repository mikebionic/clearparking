from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Sale_agr_res_price(BaseModel, db.Model):
	__tablename__ = "tbl_dk_sale_agr_res_price"
	SaleAgrResPriceId = db.Column("SaleAgrResPriceId",db.Integer,nullable=False,primary_key=True)
	SaleAgrResPriceGuid = db.Column("SaleAgrResPriceGuid",UUID(as_uuid=True),unique=True)
	SaleAgrId = db.Column("SaleAgrId",db.Integer,db.ForeignKey("tbl_dk_sale_agreement.SaleAgrId"))
	ResPriceTypeId = db.Column("ResPriceTypeId",db.Integer,db.ForeignKey("tbl_dk_res_price_type.ResPriceTypeId"))
	UnitId = db.Column("UnitId",db.Integer,db.ForeignKey("tbl_dk_unit.UnitId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	SaleAgrResPriceRegNo = db.Column("SaleAgrResPriceRegNo",db.String(100),nullable=False)
	SaleAgrResPriceValue = db.Column("SaleAgrResPriceValue",db.Float,default=0.0)
	SaleAgrPriceStartDate = db.Column("SaleAgrPriceStartDate",db.DateTime)
	SaleAgrPriceEndDate = db.Column("SaleAgrPriceEndDate",db.DateTime)

	def to_json_api(self):
		data = {
			"SaleAgrResPriceId": self.SaleAgrResPriceId,
			"SaleAgrResPriceGuid": self.SaleAgrResPriceGuid,
			"SaleAgrId": self.SaleAgrId,
			"ResPriceTypeId": self.ResPriceTypeId,
			"UnitId": self.UnitId,
			"CurrencyId": self.CurrencyId,
			"ResId": self.ResId,
			"SaleAgrResPriceRegNo": self.SaleAgrResPriceRegNo,
			"SaleAgrResPriceValue": self.SaleAgrResPriceValue,
			"SaleAgrPriceStartDate": self.SaleAgrPriceStartDate,
			"SaleAgrPriceEndDate": self.SaleAgrPriceEndDate
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data