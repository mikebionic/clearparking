from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Rp_acc_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_rp_acc_type"
	RpAccTypeId = db.Column("RpAccTypeId",db.Integer,nullable=False,primary_key=True)
	RpAccTypeGuid = db.Column("RpAccTypeGuid",UUID(as_uuid=True),unique=True)
	RpAccTypeName_tkTM = db.Column("RpAccTypeName_tkTM",db.String(100),nullable=False)
	RpAccTypeDesc_tkTM = db.Column("RpAccTypeDesc_tkTM",db.String(500))
	RpAccTypeName_ruRU = db.Column("RpAccTypeName_ruRU",db.String(100))
	RpAccTypeDesc_ruRU = db.Column("RpAccTypeDesc_ruRU",db.String(500))
	RpAccTypeName_enUS = db.Column("RpAccTypeName_enUS",db.String(100))
	RpAccTypeDesc_enUS = db.Column("RpAccTypeDesc_enUS",db.String(500))
	Rp_acc = db.relationship("Rp_acc",backref='rp_acc_type',lazy=True)

	def to_json_api(self):
		data = {
			"RpAccTypeId": self.RpAccTypeId,
			"RpAccTypeGuid": self.RpAccTypeGuid,
			"RpAccTypeName_tkTM": self.RpAccTypeName_tkTM,
			"RpAccTypeDesc_tkTM": self.RpAccTypeDesc_tkTM,
			"RpAccTypeName_ruRU": self.RpAccTypeName_ruRU,
			"RpAccTypeDesc_ruRU": self.RpAccTypeDesc_ruRU,
			"RpAccTypeName_enUS": self.RpAccTypeName_enUS,
			"RpAccTypeDesc_enUS": self.RpAccTypeDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data
