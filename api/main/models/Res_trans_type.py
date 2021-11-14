from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Res_trans_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_trans_type"
	ResTrTypeId = db.Column("ResTrTypeId",db.Integer,nullable=False,primary_key=True)
	ResTrTypeGuid = db.Column("ResTrTypeGuid",UUID(as_uuid=True),unique=True)
	ResTrTypeName_tkTM = db.Column("ResTrTypeName_tkTM",db.String(100),nullable=False)
	ResTrTypeDesc_tkTM = db.Column("ResTrTypeDesc_tkTM",db.String(500))
	ResTrTypeName_ruRU = db.Column("ResTrTypeName_ruRU",db.String(100))
	ResTrTypeDesc_ruRU = db.Column("ResTrTypeDesc_ruRU",db.String(500))
	ResTrTypeName_enUS = db.Column("ResTrTypeName_enUS",db.String(100))
	ResTrTypeDesc_enUS = db.Column("ResTrTypeDesc_enUS",db.String(500))
	Res_transaction = db.relationship("Res_transaction",backref='res_trans_type',lazy=True)

	def to_json_api(self):
		data = {
			"ResTrTypeId": self.ResTrTypeId,
			"ResTrTypeGuid": self.ResTrTypeGuid,
			"ResTrTypeName_tkTM": self.ResTrTypeName_tkTM,
			"ResTrTypeDesc_tkTM": self.ResTrTypeDesc_tkTM,
			"ResTrTypeName_ruRU": self.ResTrTypeName_ruRU,
			"ResTrTypeDesc_ruRU": self.ResTrTypeDesc_ruRU,
			"ResTrTypeName_enUS": self.ResTrTypeName_enUS,
			"ResTrTypeDesc_enUS": self.ResTrTypeDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data