from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Res_color(BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_color"
	RcId = db.Column("RcId",db.Integer,nullable=False,primary_key=True)
	RcGuid = db.Column("RcGuid",UUID(as_uuid=True),unique=True)
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	ColorId = db.Column("ColorId",db.Integer,db.ForeignKey("tbl_dk_color.ColorId"))

	def to_json_api(self):
		data = {
			"RcId": self.RcId,
			"RcGuid": self.RcGuid,
			"ResId": self.ResId,
			"ColorId": self.ColorId
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data