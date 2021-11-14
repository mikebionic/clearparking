from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel

class Relatives(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_relatives"
	RelId = db.Column("RelId",db.Integer,nullable=False,primary_key=True)
	RelGuid = db.Column("RelGuid",UUID(as_uuid=True),unique=True)
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	RelStatId = db.Column("RelStatId",db.Integer,db.ForeignKey("tbl_dk_rel_status.RelStatId"))
	RelPersonName = db.Column("RelPersonName",db.String(100),nullable=False)
	GenderId = db.Column("GenderId",db.Integer,db.ForeignKey("tbl_dk_gender.GenderId"))
	RelBirthDate = db.Column("RelBirthDate",db.DateTime)
	RelBirthPlace = db.Column("RelBirthPlace",db.String(255))
	RelWorkPlace = db.Column("RelWorkPlace",db.String(255))
	RelWorkPosition = db.Column("RelWorkPosition",db.String(255))
	RelResidence = db.Column("RelResidence",db.String(255))

	def to_json_api(self):
		data = {
			"RelId": self.RelId,
			"RelGuid": self.RelGuid,
			"EmpId": self.EmpId,
			"RelStatId": self.RelStatId,
			"RelPersonName": self.RelPersonName,
			"GenderId": self.GenderId,
			"RelBirthDate": self.RelBirthDate,
			"RelBirthPlace": self.RelBirthPlace,
			"RelWorkPlace": self.RelWorkPlace,
			"RelWorkPosition": self.RelWorkPosition,
			"RelResidence": self.RelResidence
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data
