from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel

# !!! TODO: AddInf + Ip and User-agent info
class Register_request(BaseModel, db.Model):
	__tablename__ = "tbl_me_register_request"
	RegReqId = db.Column("RegReqId",db.Integer,nullable=False,primary_key=True)
	RegReqGuid = db.Column("RegReqGuid",UUID(as_uuid=True),unique=True)
	RegReqPhoneNumber = db.Column("RegReqPhoneNumber",db.String(100))
	RegReqVerifyCode = db.Column("RegReqVerifyCode",db.String(1000))
	RegReqVerified = db.Column("RegReqVerified",db.Integer)
	RegReqExpDate = db.Column("RegReqExpDate",db.DateTime)
	RegReqIpAddress = db.Column("RegReqIpAddress",db.String(100))
	RegReqInfo = db.Column("RegReqInfo",db.String(500))

	def to_json_api(self):
		data = {
			"RegReqId": self.RegReqId,
			"RegReqGuid": self.RegReqGuid,
			"RegReqPhoneNumber": self.RegReqPhoneNumber,
			"RegReqVerifyCode": self.RegReqVerifyCode,
			"RegReqVerified": self.RegReqVerified,
			"RegReqExpDate": self.RegReqExpDate,
			"RegReqIpAddress": self.RegReqIpAddress,
			"RegReqInfo": self.RegReqInfo,			
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data
