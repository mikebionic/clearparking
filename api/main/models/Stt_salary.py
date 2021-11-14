from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


# !!! TODO: GUID is missing SttSalaryGuid
class Stt_salary(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_stt_salary"
	SttSalaryId = db.Column("SttSalaryId",db.Integer,nullable=False,primary_key=True)
	# SttSalaryGuid = db.Column("SttSalaryGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	# SalaryId = db.Column("SalaryId",db.Integer,db.ForeignKey("tbl_dk_stt_salary.SttSalaryId"))
	SttSalaryDesc = db.Column("SttSalaryDesc",db.String(500))
	SttSalaryAmount = db.Column("SttSalaryAmount",db.Float,default=0.0)

	def to_json_api(self):
		data = {
			"SttSalaryId": self.SttSalaryId,
			# "SttSalaryGuid": self.SttSalaryGuid,
			"CId": self.CId,
			"DivId": self.DivId,
			# "SalaryId": self.SalaryId,
			"SttSalaryDesc": self.SttSalaryDesc,
			"SttSalaryAmount": self.SttSalaryAmount,
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data