from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from main import db
# from main.models import BaseModel


class Attendance(db.Model):
	__tablename__ = "tbl_dk_attendance"
	AttId = db.Column("AttId",db.Integer,nullable=False,primary_key=True)
	AttGuid = db.Column("AttGuid",UUID(as_uuid=True),unique=True)
	EmpId = db.Column("EmpId",db.Integer)
	RpAccId = db.Column("RpAccId",db.Integer)
	DevId = db.Column("DevId",db.Integer)
	UId = db.Column("UId",db.Integer)
	# EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	# RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	# DevId = db.Column("DevId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.DevId"))
	# UId = db.Column("UId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.UId"))
	AttTypeId = db.Column("AttTypeId",db.Integer)
	AttDate = db.Column("AttDate",db.DateTime,default=datetime.now(),nullable=False)
	AttDesc = db.Column("AttDesc",db.String)
	# CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	# AttTypeId = db.Column("AttTypeId",db.Integer,db.ForeignKey("tbl_dk_attendance_type.AttTypeId"))

	def to_json_api(self):
		data = {
			"AttId": self.AttId,
			"AttGuid": self.AttGuid,
			"EmpId": self.EmpId,
			"RpAccId": self.RpAccId,
			"DevId": self.DevId,
			"UId": self.UId,
			"AttTypeId": self.AttTypeId,
			"AttDate": self.AttDate,
			"AttDesc": self.AttDesc
			# "CId": self.CId,
		}

		return data