from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Password_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_password_type"
	PwdTypeId = db.Column("PsswTypeId",db.Integer,nullable=False,primary_key=True)
	PwdTypeGuid = db.Column("PsswTypeGuid",UUID(as_uuid=True),unique=True)
	PwdTypeName = db.Column("PsswTypeName",db.String(100),nullable=False)
	PwdTypeDesc = db.Column("PsswTypeDesc",db.String(500))
	Password = db.relationship("Password",backref='password_type',lazy=True)

	def to_json_api(self):
		data = {
			"PsswTypeId": self.PwdTypeId,
			"PsswTypeGuid": self.PwdTypeGuid,
			"PsswTypeName": self.PwdTypeName,
			"PsswTypeDesc": self.PwdTypeDesc
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data