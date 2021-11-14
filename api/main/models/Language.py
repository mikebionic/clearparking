from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Language(BaseModel, db.Model):
	__tablename__ = "tbl_dk_language"
	LangId = db.Column("LangId",db.Integer,nullable=False,primary_key=True)
	LangGuid = db.Column("LangGuid",UUID(as_uuid=True),unique=True)
	LangName = db.Column("LangName",db.String(100),nullable=False)
	LangDesc = db.Column("LangDesc",db.String(500))
	Res_translation = db.relationship("Res_translation",backref='language',lazy=True)
	Media = db.relationship("Media",backref='language',lazy=True)

	def to_json_api(self):
		data = {
			"LangId": self.LangId,
			"LangGuid": self.LangGuid,
			"LangName": self.LangName,
			"LangDesc": self.LangDesc
		}
		return data