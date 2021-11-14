from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Res_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_type"
	ResTypeId = db.Column("ResTypeId",db.Integer,nullable=False,primary_key=True)
	ResTypeGuid = db.Column("ResTypeGuid",UUID(as_uuid=True),unique=True)
	ResTypeName_tkTM = db.Column("ResTypeName_tkTM",db.String(100))
	ResTypeDesc_tkTM = db.Column("ResTypeDesc_tkTM",db.String(500))
	ResTypeName_ruRU = db.Column("ResTypeName_ruRU",db.String(100))
	ResTypeDesc_ruRU = db.Column("ResTypeDesc_ruRU",db.String(500))
	ResTypeName_enUS = db.Column("ResTypeName_enUS",db.String(100))
	ResTypeDesc_enUS = db.Column("ResTypeDesc_enUS",db.String(500))
	Resource = db.relationship("Resource",backref='res_type',lazy=True)

	def to_json_api(self):
		data = {
			"ResTypeId": self.ResTypeId,
			"ResTypeGuid": self.ResTypeGuid,
			"ResTypeName_tkTM": self.ResTypeName_tkTM,
			"ResTypeDesc_tkTM": self.ResTypeDesc_tkTM,
			"ResTypeName_ruRU": self.ResTypeName_ruRU,
			"ResTypeDesc_ruRU": self.ResTypeDesc_ruRU,
			"ResTypeName_enUS": self.ResTypeName_enUS,
			"ResTypeDesc_enUS": self.ResTypeDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data