from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel
from main.base.dataMethods import apiDataFormat


class Res_price(BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_price"
	ResPriceId = db.Column("ResPriceId",db.Integer,nullable=False,primary_key=True)
	ResPriceGuid = db.Column("ResPriceGuid",UUID(as_uuid=True),unique=True)
	ResPriceTypeId = db.Column("ResPriceTypeId",db.Integer,db.ForeignKey("tbl_dk_res_price_type.ResPriceTypeId"))
	ResPriceGroupId = db.Column("ResPriceGroupId",db.Integer,db.ForeignKey("tbl_dk_res_price_group.ResPriceGroupId"))
	UnitId = db.Column("UnitId",db.Integer,db.ForeignKey("tbl_dk_unit.UnitId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	ResPriceRegNo = db.Column("ResPriceRegNo",db.String(100),nullable=False)
	ResPriceValue = db.Column("ResPriceValue",db.Float,default=0.0)
	PriceStartDate = db.Column("PriceStartDate",db.DateTime)
	PriceEndDate = db.Column("PriceEndDate",db.DateTime)

	def to_json_api(self):
		data = {
			"ResPriceId": self.ResPriceId,
			"ResPriceGuid": self.ResPriceGuid,
			"ResPriceTypeId": self.ResPriceTypeId,
			"ResPriceGroupId": self.ResPriceGroupId,
			"UnitId": self.UnitId,
			"CurrencyId": self.CurrencyId,
			"ResId": self.ResId,
			"ResPriceRegNo": self.ResPriceRegNo,
			"ResPriceValue": self.ResPriceValue,
			"PriceStartDate": apiDataFormat(self.PriceStartDate),
			"PriceEndDate": apiDataFormat(self.PriceEndDate)
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data