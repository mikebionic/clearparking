from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Nationality(BaseModel, db.Model):
	__tablename__ = "tbl_dk_nationality"
	NatId = db.Column("NatId",db.Integer,nullable=False,primary_key=True)
	NatGuid = db.Column("NatGuid",UUID(as_uuid=True),unique=True)
	NatName_tkTM = db.Column("NatName_tkTM",db.String(50))
	NatDesc_tkTM = db.Column("NatDesc_tkTM",db.String(500))
	NatName_ruRU = db.Column("NatName_ruRU",db.String(50))
	NatDesc_ruRU = db.Column("NatDesc_ruRU",db.String(500))
	NatName_enUS = db.Column("NatName_enUS",db.String(50))
	NatDesc_enUS = db.Column("NatDesc_enUS",db.String(500))
	Employee = db.relationship("Employee",backref='nationality',lazy=True)
	Rp_acc = db.relationship("Rp_acc",backref='nationality',lazy=True)

	def to_json_api(self):
		data = {
			"NatId": self.NatId,
			"NatGuid": self.NatGuid,
			"NatName_tkTM": self.NatName_tkTM,
			"NatDesc_tkTM": self.NatDesc_tkTM,
			"NatName_ruRU": self.NatName_ruRU,
			"NatDesc_ruRU": self.NatDesc_ruRU,
			"NatName_enUS": self.NatName_enUS,
			"NatDesc_enUS": self.NatDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data