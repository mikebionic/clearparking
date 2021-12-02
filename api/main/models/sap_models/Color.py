from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Color(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_color"
	ColorId = db.Column("ColorId",db.Integer,nullable=False,primary_key=True)
	ColorGuid = db.Column("ColorGuid",UUID(as_uuid=True),unique=True)
	ColorName = db.Column("ColorName",db.String(100),nullable=False)
	ColorDesc = db.Column("ColorDesc",db.String(500))
	ColorCode = db.Column("ColorCode",db.String(100))
	Res_color = db.relationship("Res_color",backref='color',lazy=True)
	Translation = db.relationship("Translation",backref='color',lazy=True)

	def to_json_api(self):
		data = {
			"ColorId": self.ColorId,
			"ColorGuid": self.ColorGuid,
			"ColorName": self.ColorName,
			"ColorDesc": self.ColorDesc,
			"ColorCode": self.ColorCode
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data