from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel
from main.base.dataMethods import apiDataFormat


class Emp_recr_line(BaseModel, db.Model):
	__tablename__ = "tbl_dk_emp_recr_line"
	EmpRecrLineId = db.Column("EmpRecrLineId",db.Integer,nullable=False,primary_key=True)
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	DeptId = db.Column("DeptId",db.Integer,db.ForeignKey("tbl_dk_department.DeptId"))
	ProfessionId = db.Column("ProfessionId",db.Integer,db.ForeignKey("tbl_dk_profession.ProfessionId"))
	Probation = db.Column("Probation",db.Integer)
	EmpRecrLineGuid = db.Column("EmpRecrLineGuid",UUID(as_uuid=True))
	EmploymentDate = db.Column("EmploymentDate",db.DateTime)

	def to_json_api(self):
		data = {
			"EmpRecrLineId": self.EmpRecrLineId,
			"EmpId": self.EmpId,
			"DeptId": self.DeptId,
			"ProfessionId": self.ProfessionId,
			"Probation": self.Probation,
			"EmpRecrLineGuid": self.EmpRecrLineGuid,
			"EmploymentDate": apiDataFormat(self.EmploymentDate),
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data