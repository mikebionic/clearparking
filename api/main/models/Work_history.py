from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Work_history(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_work_history"
	WorkHistId = db.Column("WorkHistId",db.Integer,nullable=False,primary_key=True)
	WorkHistGuid = db.Column("WorkHistGuid",UUID(as_uuid=True),unique=True)
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	WorkHistoryWorkPlace = db.Column("WorkHistoryWorkPlace",db.String(100),nullable=False)
	WorkHistoryWorkDesc = db.Column("WorkHistoryWorkDesc",db.String(500))
	WorkHistoryWorkDept = db.Column("WorkHistoryWorkDept",db.String(255))
	WorkHistoryWorkPos = db.Column("WorkHistoryWorkPos",db.String(255))
	WorkHistoryWorkStartDate = db.Column("WorkHistoryWorkStartDate",db.DateTime)
	WorkHistoryWorkEndDate = db.Column("WorkHistoryWorkEndDate",db.DateTime)
	WorkHistoryWorkEndReason = db.Column("WorkHistoryWorkEndReason",db.String(500))

	def to_json_api(self):
		data = {
			"WorkHistId": self.WorkHistId,
			"WorkHistGuid": self.WorkHistGuid,
			"EmpId": self.EmpId,
			"WorkHistoryWorkPlace": self.WorkHistoryWorkPlace,
			"WorkHistoryWorkDesc": self.WorkHistoryWorkDesc,
			"WorkHistoryWorkDept": self.WorkHistoryWorkDept,
			"WorkHistoryWorkPos": self.WorkHistoryWorkPos,
			"WorkHistoryWorkStartDate": self.WorkHistoryWorkStartDate,
			"WorkHistoryWorkEndDate": self.WorkHistoryWorkEndDate,
			"WorkHistoryWorkEndReason": self.WorkHistoryWorkEndReason,
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data