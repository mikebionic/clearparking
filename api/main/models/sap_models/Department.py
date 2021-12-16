from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Department(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_department"
	DeptId = db.Column("DeptId",db.Integer,nullable=False,primary_key=True)
	DeptGuid = db.Column("DeptGuid",UUID(as_uuid=True),unique=True)
	DeptName = db.Column("DeptName",db.String(100),nullable=False)
	DeptDesc = db.Column("DeptDesc",db.String(500))
	Employee = db.relationship("Employee",backref='department',lazy=True)
	Department_detail = db.relationship("Department_detail",backref='department',lazy=True)
	Emp_recr_line = db.relationship("Emp_recr_line",backref='department',lazy=True)
	Staffing_table = db.relationship("Staffing_table",backref='department',lazy=True)

	def to_json_api(self):
		data = {
			"DeptId": self.DeptId,
			"DeptGuid": self.DeptGuid,
			"DeptName": self.DeptName,
			"DeptDesc": self.DeptDesc
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data