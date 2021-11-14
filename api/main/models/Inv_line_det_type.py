from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Inv_line_det_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_inv_line_det_type"
	InvLineDetTypeId = db.Column("InvLineDetTypeId",db.Integer,nullable=False,primary_key=True)
	InvLineDetTypeGuid = db.Column("InvLineDetTypeGuid",UUID(as_uuid=True),unique=True)
	InvLineDetTypeName_tkTM = db.Column("InvLineDetTypeName_tkTM",db.String(100),nullable=False)
	InvLineDetTypeDesc_tkTM = db.Column("InvLineDetTypeDesc_tkTM",db.String(500))
	InvLineDetTypeName_ruRU = db.Column("InvLineDetTypeName_ruRU",db.String(100))
	InvLineDetTypeDesc_ruRU = db.Column("InvLineDetTypeDesc_ruRU",db.String(500))
	InvLineDetTypeName_enUS = db.Column("InvLineDetTypeName_enUS",db.String(100))
	InvLineDetTypeDesc_enUS = db.Column("InvLineDetTypeDesc_enUS",db.String(500))
	Inv_line_det = db.relationship("Inv_line_det",backref='inv_line_det_type',lazy=True)

	def to_json_api(self):
		data = {
			"InvLineDetTypeId": self.InvLineDetTypeId,
			"InvLineDetTypeGuid": self.InvLineDetTypeGuid,
			"InvLineDetTypeName_tkTM": self.InvLineDetTypeName_tkTM,
			"InvLineDetTypeDesc_tkTM": self.InvLineDetTypeDesc_tkTM,
			"InvLineDetTypeName_ruRU": self.InvLineDetTypeName_ruRU,
			"InvLineDetTypeDesc_ruRU": self.InvLineDetTypeDesc_ruRU,
			"InvLineDetTypeName_enUS": self.InvLineDetTypeName_enUS,
			"InvLineDetTypeDesc_enUS": self.InvLineDetTypeDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data