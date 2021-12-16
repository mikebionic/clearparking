from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Emp_status(BaseModel,db.Model):
	__tablename__ = "tbl_dk_emp_status"
	EmpStatId = db.Column("EmpStatId",db.Integer,nullable=False,primary_key=True)
	EmpStatGuid = db.Column("EmpStatGuid",UUID(as_uuid=True),unique=True)
	EmpStatName_tkTM = db.Column("EmpStatName_tkTM",db.String(100))
	EmpStatDesc_tkTM = db.Column("EmpStatDesc_tkTM",db.String(500))
	EmpStatName_ruRU = db.Column("EmpStatName_ruRU",db.String(100))
	EmpStatDesc_ruRU = db.Column("EmpStatDesc_ruRU",db.String(500))
	EmpStatName_enUS = db.Column("EmpStatName_enUS",db.String(100))
	EmpStatDesc_enUS = db.Column("EmpStatDesc_enUS",db.String(500))
	Employee = db.relationship("Employee",backref='emp_status',lazy=True)

	def to_json_api(self):
		data = {
			"EmpStatId": self.EmpStatId,
			"EmpStatGuid": self.EmpStatGuid,
			"EmpStatName_tkTM": self.EmpStatName_tkTM,
			"EmpStatDesc_tkTM": self.EmpStatDesc_tkTM,
			"EmpStatName_ruRU": self.EmpStatName_ruRU,
			"EmpStatDesc_ruRU": self.EmpStatDesc_ruRU,
			"EmpStatName_enUS": self.EmpStatName_enUS,
			"EmpStatDesc_enUS": self.EmpStatDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data