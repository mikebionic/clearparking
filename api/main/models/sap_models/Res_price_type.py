from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Res_price_type(AddInf,BaseModel,db.Model):
	__tablename__ = "tbl_dk_res_price_type"
	ResPriceTypeId = db.Column("ResPriceTypeId",db.Integer,nullable=False,primary_key=True)
	RespriceTypeGuid = db.Column("RespriceTypeGuid",UUID(as_uuid=True),unique=True)
	ResPriceTypeName_tkTM = db.Column("ResPriceTypeName_tkTM",db.String(100),nullable=False)
	ResPriceTypeDesc_tkTM = db.Column("ResPriceTypeDesc_tkTM",db.String(500))
	ResPriceTypeName_ruRU = db.Column("ResPriceTypeName_ruRU",db.String(100))
	ResPriceTypeDesc_ruRU = db.Column("ResPriceTypeDesc_ruRU",db.String(500))
	ResPriceTypeName_enUS = db.Column("ResPriceTypeName_enUS",db.String(100))
	ResPriceTypeDesc_enUS = db.Column("ResPriceTypeDesc_enUS",db.String(500))
	Res_price = db.relationship("Res_price",backref='res_price_type',lazy=True)
	# multiple relationship
	Res_price_group = db.relationship("Res_price_group",foreign_keys='Res_price_group.FromResPriceTypeId',backref='res_price_type',lazy=True)
	Res_price_group = db.relationship("Res_price_group",foreign_keys='Res_price_group.ToResPriceTypeId',backref='res_price_type',lazy=True)
	Sale_agr_res_price = db.relationship("Sale_agr_res_price",backref='res_price_type',lazy=True)

	def to_json_api(self):
		data = {
			"ResPriceTypeId": self.ResPriceTypeId,
			"ResPriceTypeGuid": self.ResPriceTypeGuid,
			"ResPriceTypeName_tkTM": self.ResPriceTypeName_tkTM,
			"ResPriceTypeDesc_tkTM": self.ResPriceTypeDesc_tkTM,
			"ResPriceTypeName_ruRU": self.ResPriceTypeName_ruRU,
			"ResPriceTypeDesc_ruRU": self.ResPriceTypeDesc_ruRU,
			"ResPriceTypeName_enUS": self.ResPriceTypeName_enUS,
			"ResPriceTypeDesc_enUS": self.ResPriceTypeDesc_enUS
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data