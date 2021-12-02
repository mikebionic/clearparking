from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class User_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_user_type"
	UTypeId = db.Column("UTypeId",db.Integer,nullable=False,primary_key=True)
	UTypeGuid = db.Column("UTypeGuid",UUID(as_uuid=True),unique=True)
	UTypeName_tkTM = db.Column("UTypeName_tkTM",db.String(50))
	UTypeDesc_tkTM = db.Column("UTypeDesc_tkTM",db.String(500))
	UTypeName_ruRU = db.Column("UTypeName_ruRU",db.String(50))
	UTypeDesc_ruRU = db.Column("UTypeDesc_ruRU",db.String(500))
	UTypeName_enUS = db.Column("UTypeName_enUS",db.String(50))
	UTypeDesc_enUS = db.Column("UTypeDesc_enUS",db.String(500))
	User = db.relationship("User",backref='user_type',lazy=True)

	def to_json_api(self):
		data = {
			"UTypeId": self.UTypeId,
			"UTypeGuid": self.UTypeGuid,
			"UTypeName_tkTM": self.UTypeName_tkTM,
			"UTypeDesc_tkTM": self.UTypeDesc_tkTM,
			"UTypeName_ruRU": self.UTypeName_ruRU,
			"UTypeDesc_ruRU": self.UTypeDesc_ruRU,
			"UTypeName_enUS": self.UTypeName_enUS,
			"UTypeDesc_enUS": self.UTypeDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data