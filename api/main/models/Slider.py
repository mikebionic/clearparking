from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Slider(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_slider"
	SlId = db.Column("SlId",db.Integer,nullable=False,primary_key=True)
	SlGuid = db.Column("SlGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	SlName = db.Column("SlName",db.String(100),nullable=False)
	SlDesc = db.Column("SlDesc",db.String(500),default='')
	Sl_image = db.relationship("Sl_image",backref='slider',lazy=True)

	def to_json_api(self):
		data = {
			"SlId": self.SlId,
			"SlGuid": self.SlGuid,
			"CId": self.CId,
			"DivId": self.DivId,
			"SlName": self.SlName,
			"SlDesc": self.SlDesc
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data