from sqlalchemy.dialects.postgresql import UUID

from main import db


class Department_detail(db.Model):
	__tablename__ = "tbl_dk_department_detail"
	DeptDetId = db.Column("DeptDetId",db.Integer,nullable=False,primary_key=True)
	DeptDetGuid = db.Column("DeptDetGuid",UUID(as_uuid=True),unique=True)
	DeptId = db.Column("DeptId",db.Integer,db.ForeignKey("tbl_dk_department.DeptId"))
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	DeptHeadEmpId = db.Column("DeptHeadEmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))

	def to_json_api(self):
		data = {
			"DeptDetId": self.DeptDetId,
			"DeptDetGuid": self.DeptDetGuid,
			"DeptId": self.DeptId,
			"CId": self.CId,
			"DivId": self.DivId,
			"DeptHeadEmpId": self.DeptHeadEmpId
		}
		return data