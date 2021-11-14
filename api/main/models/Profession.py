from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Profession(BaseModel, db.Model):
	__tablename__ = "tbl_dk_profession"
	ProfessionId = db.Column("ProfessionId",db.Integer,nullable=False,primary_key=True)
	ProfessionGuid = db.Column("ProfessionGuid",UUID(as_uuid=True),unique=True)
	ProfessionName_tkTM = db.Column("ProfessionName_tkTM",db.String(50))
	ProfessionDesc_tkTM = db.Column("ProfessionDesc_tkTM",db.String(500))
	ProfessionName_ruRU = db.Column("ProfessionName_ruRU",db.String(50))
	ProfessionDesc_ruRU = db.Column("ProfessionDesc_ruRU",db.String(500))
	ProfessionName_enUS = db.Column("ProfessionName_enUS",db.String(50))
	ProfessionDesc_enUS = db.Column("ProfessionDesc_enUS",db.String(500))
	Employee = db.relationship("Employee",backref='profession',lazy=True)
	Emp_recr_line = db.relationship("Emp_recr_line",backref='profession',lazy=True)
	Staffing_table = db.relationship("Staffing_table",backref='profession',lazy=True)

	def to_json_api(self):
		data = {
			"ProfessionId": self.ProfessionId,
			"ProfessionGuid": self.ProfessionGuid,
			"ProfessionName_tkTM": self.ProfessionName_tkTM,
			"ProfessionDesc_tkTM": self.ProfessionDesc_tkTM,
			"ProfessionName_ruRU": self.ProfessionName_ruRU,
			"ProfessionDesc_ruRU": self.ProfessionDesc_ruRU,
			"ProfessionName_enUS": self.ProfessionName_enUS,
			"ProfessionDesc_enUS": self.ProfessionDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data