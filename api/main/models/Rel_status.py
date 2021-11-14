from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Rel_status(BaseModel, db.Model):
	__tablename__ = "tbl_dk_rel_status"
	RelStatId = db.Column("RelStatId",db.Integer,nullable=False,primary_key=True)
	RelStatGuid = db.Column("RelStatGuid",UUID(as_uuid=True),unique=True)
	RelStatName_tkTM = db.Column("RelStatName_tkTM",db.String(50))
	RelStatDesc_tkTM = db.Column("RelStatDesc_tkTM",db.String(500))
	RelStatName_ruRU = db.Column("RelStatName_ruRU",db.String(50))
	RelStatDesc_ruRU = db.Column("RelStatDesc_ruRU",db.String(500))
	RelStatName_enUS = db.Column("RelStatName_enUS",db.String(50))
	RelStatDesc_enUS = db.Column("RelStatDesc_enUS",db.String(500))
	Relatives = db.relationship("Relatives",backref='rel_status',lazy=True)

	def to_json_api(self):
		data = {
			"RelStatId": self.RelStatId,
			"RelStatGuid": self.RelStatGuid,
			"RelStatName_tkTM": self.RelStatName_tkTM,
			"RelStatDesc_tkTM": self.RelStatDesc_tkTM,
			"RelStatName_ruRU": self.RelStatName_ruRU,
			"RelStatDesc_ruRU": self.RelStatDesc_ruRU,
			"RelStatName_enUS": self.RelStatName_enUS,
			"RelStatDesc_enUS": self.RelStatDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data