from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Visited_country(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_visited_countries"
	VCId = db.Column("VCId",db.Integer,nullable=False,primary_key=True)
	VCGuid = db.Column("VCGuid",UUID(as_uuid=True),unique=True)
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	VCCountryName = db.Column("VCCountryName",db.String(50),nullable=False)
	VCCountryDesc = db.Column("VCCountryDesc",db.String(500))
	VCPurpose = db.Column("VCPurpose",db.String(500))
	VCStartDate = db.Column("VCStartDate",db.DateTime)
	VCEndDate = db.Column("VCEndDate",db.DateTime)

	def to_json_api(self):
		json_data = {
			"VCId": self.VCId,
			"VCGuid": self.VCGuid,
			"EmpId": self.EmpId,
			"VCCountryName": self.VCCountryName,
			"VCCountryDesc": self.VCCountryDesc,
			"VCPurpose": self.VCPurpose,
			"VCStartDate": self.VCStartDate,
			"VCEndDate": self.VCEndDate
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data