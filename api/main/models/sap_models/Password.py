from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Password(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_password"
	PwdId = db.Column("PsswId",db.Integer,nullable=False,primary_key=True)
	PwdGuid = db.Column("PsswGuid",UUID(as_uuid=True),unique=True)
	PwdUId = db.Column("PsswUId",db.Integer,db.ForeignKey("tbl_dk_users.UId"))
	PwdTypeId = db.Column("PsswTypeId",db.Integer,db.ForeignKey("tbl_dk_password_type.PsswTypeId"))
	PwdPassHash = db.Column("PsswPassHash",db.String(255))
	PwdPassword = db.Column("PsswPasswor",db.String(100),nullable=False)

	def to_json_api(self):
		data = {
			"PsswId": self.PwdId,
			"PsswGuid": self.PwdGuid,
			"PsswUId": self.PwdUId,
			"PsswTypeId": self.PwdTypeId,
			"PsswPassHash": self.PwdPassHash,
			"PsswPassword": self.PwdPassword,
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data