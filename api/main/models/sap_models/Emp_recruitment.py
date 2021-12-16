from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel
from main.base.dataMethods import apiDataFormat


class Emp_recruitment(BaseModel, db.Model):
	__tablename__ = "tbl_dk_emp_recruitment"
	EmpRecrId = db.Column("EmpRecrId",db.Integer,nullable=False,primary_key=True)
	EmpRecrGuid = db.Column("EmpRecrGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	EmpRecrRegNo = db.Column("EmpRecrRegNo",db.String(128),nullable=False,unique=True)
	OrderNo = db.Column("OrderNo",db.String(128))
	EmpRecrDate = db.Column("EmpRecrDate",db.DateTime)

	def to_json_api(self):
		data = {
			"EmpRecrId": self.EmpRecrId,
			"EmpRecrGuid": self.EmpRecrGuid,
			"CId": self.CId,
			"DivId": self.DivId,
			"EmpRecrRegNo": self.EmpRecrRegNo,
			"OrderNo": self.OrderNo,
			"EmpRecrDate": apiDataFormat(self.EmpRecrDate),
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data