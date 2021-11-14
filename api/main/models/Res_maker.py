from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Res_maker(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_maker"
	ResMakerId = db.Column("ResMakerId",db.Integer,nullable=False,primary_key=True)
	ResMakerGuid = db.Column("ResMakerGuid",UUID(as_uuid=True),unique=True)
	ResMakerName = db.Column("ResMakerName",db.String(100),nullable=False)
	ResMakerDesc = db.Column("ResMakerDesc",db.String(500))
	ResMakerSite = db.Column("ResMakerSite",db.String(150))
	ResMakerMail = db.Column("ResMakerMail",db.String(100))
	ResMakerPhone1 = db.Column("ResMakerPhone1",db.String(100))
	ResMakerPhone2 = db.Column("ResMakerPhone2",db.String(100))
	Resource = db.relationship("Resource",backref='res_maker',lazy=True)

	def to_json_api(self):
		data = {
			"ResMakerId": self.ResMakerId,
			"ResMakerGuid": self.ResMakerGuid,
			"ResMakerName": self.ResMakerName,
			"ResMakerDesc": self.ResMakerDesc,
			"ResMakerSite": self.ResMakerSite,
			"ResMakerMail": self.ResMakerMail,
			"ResMakerPhone1": self.ResMakerPhone1,
			"ResMakerPhone2": self.ResMakerPhone2
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data