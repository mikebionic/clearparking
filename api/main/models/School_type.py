from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class School_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_school_type"
	SchoolTypeId = db.Column("SchoolTypeId",db.Integer,nullable=False,primary_key=True)
	SchoolTypeGuid = db.Column("SchoolTypeGuid",UUID(as_uuid=True),unique=True)
	SchoolTypeName_tkTM = db.Column("SchoolTypeName_tkTM",db.String(50))
	SchoolTypeDesc_tkTM = db.Column("SchoolTypeDesc_tkTM",db.String(500))
	SchoolTypeName_ruRU = db.Column("SchoolTypeName_ruRU",db.String(50))
	SchoolTypeDesc_ruRU = db.Column("SchoolTypeDesc_ruRU",db.String(500))
	SchoolTypeName_enUS = db.Column("SchoolTypeName_enUS",db.String(50))
	SchoolTypeDesc_enUS = db.Column("SchoolTypeDesc_enUS",db.String(500))	

	def to_json_api(self):
		data = {
			"SchoolTypeId": self.SchoolTypeId,
			"SchoolTypeGuid": self.SchoolTypeGuid,
			"SchoolTypeName_tkTM": self.SchoolTypeName_tkTM,
			"SchoolTypeDesc_tkTM": self.SchoolTypeDesc_tkTM,
			"SchoolTypeName_ruRU": self.SchoolTypeName_ruRU,
			"SchoolTypeDesc_ruRU": self.SchoolTypeDesc_ruRU,
			"SchoolTypeName_enUS": self.SchoolTypeName_enUS,
			"SchoolTypeDesc_enUS": self.SchoolTypeDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data