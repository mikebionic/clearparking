from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Res_trans_inv_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_trans_inv_type"
	ResTrInvTypeId = db.Column("ResTrInvTypeId",db.Integer,nullable=False,primary_key=True)
	ResTrInvTypeGuid = db.Column("ResTrInvTypeGuid",UUID(as_uuid=True),unique=True)
	ResTrInvName_tkTM = db.Column("ResTrInvName_tkTM",db.String(100),nullable=False)
	ResTrInvDesc_tkTM = db.Column("ResTrInvDesc_tkTM",db.String(500))
	ResTrInvName_ruRU = db.Column("ResTrInvName_ruRU",db.String(100))
	ResTrInvDesc_ruRU = db.Column("ResTrInvDesc_ruRU",db.String(500))
	ResTrInvName_enUS = db.Column("ResTrInvName_enUS",db.String(100))
	ResTrInvDesc_enUS = db.Column("ResTrInvDesc_enUS",db.String(500))
	Res_trans_inv = db.relationship("Res_trans_inv",backref='res_trans_inv_type',lazy=True)

	def to_json_api(self):
		data = {
			"ResTrInvTypeId": self.ResTrInvTypeId,
			"ResTrInvTypeGuid": self.ResTrInvTypeGuid,
			"ResTrInvName_tkTM": self.ResTrInvName_tkTM,
			"ResTrInvDesc_tkTM": self.ResTrInvDesc_tkTM,
			"ResTrInvName_ruRU": self.ResTrInvName_ruRU,
			"ResTrInvDesc_ruRU": self.ResTrInvDesc_ruRU,
			"ResTrInvName_enUS": self.ResTrInvName_enUS,
			"ResTrInvDesc_enUS": self.ResTrInvDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data