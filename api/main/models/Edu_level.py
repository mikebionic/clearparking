from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Edu_level(BaseModel, db.Model):
	__tablename__ = "tbl_dk_edu_level"
	EduLevelId = db.Column("EduLevelId",db.Integer,nullable=False,primary_key=True)
	EduLevelGuid = db.Column("EduLevelGuid",UUID(as_uuid=True),unique=True)
	EduLevelName_tkTM = db.Column("EduLevelName_tkTM",db.String(100))
	EduLevelDesc_tkTM = db.Column("EduLevelDesc_tkTM",db.String(500))
	EduLevelName_ruRU = db.Column("EduLevelName_ruRU",db.String(100))
	EduLevelDesc_ruRU = db.Column("EduLevelDesc_ruRU",db.String(500))
	EduLevelName_enUS = db.Column("EduLevelName_enUS",db.String(100))
	EduLevelDesc_enUS = db.Column("EduLevelDesc_enUS",db.String(500))
	Employee = db.relationship("Employee",backref='edu_level',lazy=True)

	def to_json_api(self):
		data = {
			"EduLevelId": self.EduLevelId,
			"EduLevelGuid": self.EduLevelGuid,
			"EduLevelName_tkTM": self.EduLevelName_tkTM,
			"EduLevelDesc_tkTM": self.EduLevelDesc_tkTM,
			"EduLevelName_ruRU": self.EduLevelName_ruRU,
			"EduLevelDesc_ruRU": self.EduLevelDesc_ruRU,
			"EduLevelName_enUS": self.EduLevelName_enUS,
			"EduLevelDesc_enUS": self.EduLevelDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data