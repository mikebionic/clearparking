from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Config_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_config_type"
	CfTypeId = db.Column("CfTypeId",db.Integer,primary_key=True)
	CfTypeGuid = db.Column("CfTypeGuid",UUID(as_uuid=True),unique=True)
	CfTypeName_tkTM = db.Column("CfTypeName_tkTM",db.String(100))
	CfTypeDesc_tkTM = db.Column("CfTypeDesc_tkTM",db.String(500))
	CfTypeName_ruRU = db.Column("CfTypeName_ruRU",db.String(100))
	CfTypeDesc_ruRU = db.Column("CfTypeDesc_ruRU",db.String(500))
	CfTypeName_enUS = db.Column("CfTypeName_enUS",db.String(100))
	CfTypeDesc_enUS = db.Column("CfTypeDesc_enUS",db.String(500))
	Config = db.relationship("Config",backref='config_type',lazy=True)

	def to_json_api(self):
		data = {
			"CfTypeId": self.CfTypeId,
			"CfTypeGuid": self.CfTypeGuid,
			"CfTypeName_tkTM": self.CfTypeName_tkTM,
			"CfTypeDesc_tkTM": self.CfTypeDesc_tkTM,
			"CfTypeName_ruRU": self.CfTypeName_ruRU,
			"CfTypeDesc_ruRU": self.CfTypeDesc_ruRU,
			"CfTypeName_enUS": self.CfTypeName_enUS,
			"CfTypeDesc_enUS": self.CfTypeDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data