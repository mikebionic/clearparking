from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Rating(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_rating"
	RtId = db.Column("RtId",db.Integer,nullable=False,primary_key=True)
	RtGuid = db.Column("RtGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	UId = db.Column("UId",db.Integer,db.ForeignKey("tbl_dk_users.UId"))
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	RtRemark = db.Column("RtRemark",db.String(500),default='')
	RtRatingValue = db.Column("RtRatingValue",db.Float,nullable=False,default=0)
	RtValidated = db.Column("RtValidated",db.Boolean,default=False)

	def to_json_api(self):
		data = {
			"RtId": self.RtId,
			"RtGuid": self.RtGuid,
			"CId": self.CId,
			"DivId": self.DivId,
			"UId": self.UId,
			"ResId": self.ResId,
			"RpAccId": self.RpAccId,
			"EmpId": self.EmpId,
			"RtRemark": self.RtRemark,
			"RtRatingValue": self.RtRatingValue,
			"RtValidated": self.RtValidated
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data