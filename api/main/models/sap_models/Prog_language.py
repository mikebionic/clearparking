from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Prog_language(BaseModel, db.Model):
	__tablename__ = "tbl_dk_prog_language"
	LangId = db.Column("LangId",db.Integer,nullable=False,primary_key=True)
	LangGuid = db.Column("LangGuid",UUID(as_uuid=True),unique=True)
	LangName = db.Column("LangName",db.String(50),nullable=False)
	LangDesc = db.Column("LangDesc",db.String(200))

	def to_json_api(self):
		data = {
			"LangId": self.LangId,
			"LangGuid": self.LangGuid,
			"LangName": self.LangName,
			"LangDesc": self.LangDesc
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data