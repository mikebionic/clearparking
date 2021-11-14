from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Staffing_table(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_staffing_table"
	SttId = db.Column("SttId",db.Integer,nullable=False,primary_key=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	DeptId = db.Column("DeptId",db.Integer,db.ForeignKey("tbl_dk_department.DeptId"))
	ProfessionId = db.Column("ProfessionId",db.Integer,db.ForeignKey("tbl_dk_profession.ProfessionId"))
	SttGuid = db.Column("SttGuid",UUID(as_uuid=True),unique=True)
	SttName = db.Column("SttName",db.String(100),nullable=False)
	SttDesc = db.Column("SttDesc",db.String(500))
	SttStaffAmount = db.Column("SttStaffAmount",db.Float,default=0.0)
	SttVacationDays = db.Column("SttVacationDays",db.Integer)

	def to_json_api(self):
		data = {
			"SttId": self.SttId,
			"CId": self.CId,
			"DivId": self.DivId,
			"DeptId": self.DeptId,
			"ProfessionId": self.ProfessionId,
			"SttGuid": self.SttGuid,
			"SttName": self.SttName,
			"SttDesc": self.SttDesc,
			"SttStaffAmount": self.SttStaffAmount,
			"SttVacationDays": self.SttVacationDays,
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data