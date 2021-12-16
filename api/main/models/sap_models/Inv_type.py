from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Inv_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_inv_type"
	InvTypeId = db.Column("InvTypeId",db.Integer,nullable=False,primary_key=True)
	InvTypeGuid = db.Column("InvTypeGuid",UUID(as_uuid=True),unique=True)
	InvTypeName_tkTM = db.Column("InvTypeName_tkTM",db.String(100),nullable=False)
	InvTypeDesc_tkTM = db.Column("InvTypeDesc_tkTM",db.String(500))
	InvTypeName_ruRU = db.Column("InvTypeName_ruRU",db.String(100))
	InvTypeDesc_ruRU = db.Column("InvTypeDesc_ruRU",db.String(500))
	InvTypeName_enUS = db.Column("InvTypeName_enUS",db.String(100))
	InvTypeDesc_enUS = db.Column("InvTypeDesc_enUS",db.String(500))
	Invoice = db.relationship("Invoice",backref='inv_type',lazy=True)

	def to_json_api(self):
		data = {
			"InvTypeId": self.InvTypeId,
			"InvTypeGuid": self.InvTypeGuid,
			"InvTypeName_tkTM": self.InvTypeName_tkTM,
			"InvTypeDesc_tkTM": self.InvTypeDesc_tkTM,
			"InvTypeName_ruRU": self.InvTypeName_ruRU,
			"InvTypeDesc_ruRU": self.InvTypeDesc_ruRU,
			"InvTypeName_enUS": self.InvTypeName_enUS,
			"InvTypeDesc_enUS": self.InvTypeDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data