from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Res_translation(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_translations"
	ResTranslationId = db.Column("ResTranslId",db.Integer,nullable=False,primary_key=True)
	ResTranslationGuid = db.Column("ResTranslGuid",UUID(as_uuid=True),unique=True)
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	LangId = db.Column("LangId",db.Integer,db.ForeignKey("tbl_dk_language.LangId"))
	ResName = db.Column("ResName",db.String(255))
	ResDesc = db.Column("ResDesc",db.String(500))
	ResFullDesc = db.Column("ResFullDesc",db.String(1500))

	def to_json_api(self):
		data = {
			"ResTranslId": self.ResTranslationId,
			"ResTranslGuid": self.ResTranslationGuid,
			"ResId": self.ResId,
			"LangId": self.LangId,
			"ResName": self.ResName,
			"ResDesc": self.ResDesc,
			"ResFullDesc": self.ResFullDesc
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data