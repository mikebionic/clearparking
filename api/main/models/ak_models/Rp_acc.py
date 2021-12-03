from sqlalchemy.dialects.postgresql import UUID

from main import db

class Rp_acc(db.Model):
	__tablename__ = "tbl_mg_arap"
	RpAccId = db.Column("arap_id",db.Integer,nullable=False,primary_key=True)
	RpAccGuid = db.Column("arap_id_guid",UUID(as_uuid=True),unique=True)
	RpAccRegNo = db.Column("arap_code", db.String)
	RpAccUName = db.Column("arap_name", db.String)
	RpAccUPass = db.Column("security_code", db.String)
	RpAccAddress = db.Column("arap_address", db.String)
	CId = db.Column("firm_id", db.Integer)
	RpAccTypeId = db.Column("a_type_id", db.Integer)
	RpAccStatusId = db.Column("a_status_id", db.Integer)
	CreatedDate = db.Column("arap_create_date", db.DateTime)
	ModifiedDate = db.Column("arap_modify_date", db.DateTime)
	RpAccHomePhoneNumber = db.Column("arap_tel_home", db.String)
	RpAccWorkPhoneNumber = db.Column("arap_tel_work", db.String)
	RpAccMobilePhoneNumber = db.Column("arap_tel_mobile1", db.String)
	RpAccWorkFaxNumber = db.Column("arap_tel_fax", db.String)
	RpAccEMail = db.Column("arap_email1", db.String)

	def to_json_api(self):
		data = {
			"RpAccId": self.RpAccId,			
			"RpAccGuid": self.RpAccGuid,			
			"RpAccRegNo": self.RpAccRegNo,
			"RpAccUName": self.RpAccUName,
			"RpAccUPass": self.RpAccUPass,
			"RpAccAddress": self.RpAccAddress,
			"CId": self.CId,
			"RpAccTypeId": self.RpAccTypeId,
			"RpAccStatusId": self.RpAccStatusId,
			"CreatedDate": self.CreatedDate,
			"ModifiedDate": self.ModifiedDate,
			"RpAccHomePhoneNumber": self.RpAccHomePhoneNumber,
			"RpAccWorkPhoneNumber": self.RpAccWorkPhoneNumber,
			"RpAccMobilePhoneNumber": self.RpAccMobilePhoneNumber,
			"RpAccWorkFaxNumber": self.RpAccWorkFaxNumber,
			"RpAccEMail": self.RpAccEMail,
		}

		return data
