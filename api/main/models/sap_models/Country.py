from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Country(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_country"
	CountryId = db.Column("CountryId",db.Integer,nullable=False,primary_key=True)
	CountryGuid = db.Column("CountryGuid",UUID(as_uuid=True),unique=True)
	CountryName = db.Column("CountryName",db.String(50),nullable=False)
	CountryDesc = db.Column("CountryDesc",db.String(500))
	City = db.relationship("City",backref='country',lazy=True)
	Location = db.relationship("Location",backref='country',lazy=True)

	def to_json_api(self):
		data = {
			"CountryId": self.CountryId,
			"CountryGuid": self.CountryGuid,
			"CountryName": self.CountryName,
			"CountryDesc": self.CountryDesc
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data