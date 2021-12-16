from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class City(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_city"
	CityId = db.Column("CityId",db.Integer,nullable=False,primary_key=True)
	CityGuid = db.Column("CityGuid",UUID(as_uuid=True),unique=True)
	CountryId = db.Column("CountryId",db.Integer,db.ForeignKey("tbl_dk_country.CountryId"))
	CityName = db.Column("CityName",db.String(50),nullable=False)
	CityDesc = db.Column("CityDesc",db.String(500))
	Location = db.relationship("Location",backref='city',lazy=True)

	def to_json_api(self):
		data = {
			"CityId": self.CityId,
			"CityGuid": self.CityGuid,
			"CountryId": self.CountryId,
			"CityName": self.CityName,
			"CityDesc": self.CityDesc,
			"Location": self.Location
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data