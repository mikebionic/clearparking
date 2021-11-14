from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class School(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_school"
	SchoolId = db.Column("SchoolId",db.Integer,nullable=False,primary_key=True)
	SchoolGuid = db.Column("SchoolGuid",UUID(as_uuid=True),unique=True)
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	SchoolTypeId = db.Column("SchoolTypeId",db.Integer,db.ForeignKey("tbl_dk_school_type.SchoolTypeId"))
	SchoolName = db.Column("SchoolName",db.String(255),nullable=False)
	SchoolDesc = db.Column("SchoolDesc",db.String(500))
	SchoolPlace = db.Column("SchoolPlace",db.String(255))
	SchoolEduStartDate = db.Column("SchoolEduStartDate",db.DateTime)
	SchoolEduEndDate = db.Column("SchoolEduEndDate",db.DateTime)
	SchoolProfession = db.Column("SchoolProfession",db.String(255))
	SchoolIsGraduated = db.Column("SchoolIsGraduated",db.Boolean,default=False)

	def to_json_api(self):
		data = {
			"SchoolId": self.SchoolId,
			"SchoolGuid": self.SchoolGuid,
			"EmpId": self.EmpId,
			"SchoolTypeId": self.SchoolTypeId,
			"SchoolName": self.SchoolName,
			"SchoolDesc": self.SchoolDesc,
			"SchoolPlace": self.SchoolPlace,
			"SchoolEduStartDate": self.SchoolEduStartDate,
			"SchoolEduEndDate": self.SchoolEduEndDate,
			"SchoolProfession": self.SchoolProfession,
			"SchoolIsGraduated": self.SchoolIsGraduated
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data
