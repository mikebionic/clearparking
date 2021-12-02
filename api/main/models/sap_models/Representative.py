from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db
from . import AddInf, BaseModel


class Representative(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_representative"
	ReprId = db.Column("ReprId",db.Integer,nullable=False,primary_key=True)
	ReprGuid = db.Column("ReprGuid",UUID(as_uuid=True),unique=True)
	ReprStatusId = db.Column("ReprStatusId",db.Integer,nullable=False,default=1)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	GenderId = db.Column("GenderId",db.Integer,db.ForeignKey("tbl_dk_gender.GenderId"))
	ReprRegNo = db.Column("ReprRegNo",db.String(100),nullable=False)
	ReprName = db.Column("ReprName",db.String(100),nullable=False)
	ReprDesc = db.Column("ReprDesc",db.String(500))
	ReprProfession = db.Column("ReprProfession",db.String(100))
	ReprMobilePhoneNumber = db.Column("ReprMobilePhoneNumber",db.String(100))
	ReprHomePhoneNumber = db.Column("ReprHomePhoneNumber",db.String(100))
	ReprWorkPhoneNumber = db.Column("ReprWorkPhoneNumber",db.String(100))
	ReprWorkFaxNumber = db.Column("ReprWorkFaxNumber",db.String(100))
	ReprZipCode = db.Column("ReprZipCode",db.String(100))
	ReprEMail = db.Column("ReprEMail",db.String(100))
	CreatedDate = db.Column("CreatedDate",db.DateTime,default=datetime.now)
	ModifiedDate = db.Column("ModifiedDate",db.DateTime,default=datetime.now)
	CreatedUId = db.Column("CreatedUId",db.Integer,default=0)
	ModifiedUId = db.Column("ModifiedUId",db.Integer,default=0)
	MyProperty = db.Column("MyProperty",db.Integer)
	Rp_acc = db.relationship("Rp_acc",backref='representative',foreign_keys='Rp_acc.ReprId',lazy='joined')

	def to_json_api(self):
		data = {
			"ReprId": self.ReprId,
			"ReprGuid": self.ReprGuid,
			"ReprStatusId": self.ReprStatusId,
			"CId": self.CId,
			"DivId": self.DivId,
			"RpAccId": self.RpAccId,
			"GenderId": self.GenderId,
			"ReprRegNo": self.ReprRegNo,
			"ReprName": self.ReprName,
			"ReprDesc": self.ReprDesc,
			"ReprProfession": self.ReprProfession,
			"ReprMobilePhoneNumber": self.ReprMobilePhoneNumber,
			"ReprHomePhoneNumber": self.ReprHomePhoneNumber,
			"ReprWorkPhoneNumber": self.ReprWorkPhoneNumber,
			"ReprWorkFaxNumber": self.ReprWorkFaxNumber,
			"ReprZipCode": self.ReprZipCode,
			"ReprEMail": self.ReprEMail,
			"CreatedDate": self.CreatedDate,
			"ModifiedDate": self.ModifiedDate,
			"CreatedUId": self.CreatedUId,
			"ModifiedUId": self.ModifiedUId,
			"MyProperty": self.MyProperty
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data