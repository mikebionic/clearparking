from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Reg_num(BaseModel, db.Model):
	__tablename__ = "tbl_dk_reg_num"
	RegNumId = db.Column("RegNumId",db.Integer,nullable=False,primary_key=True)
	RegNumGuid = db.Column("RegNumGuid",UUID(as_uuid=True),unique=True)
	RegNumTypeId = db.Column("RegNumTypeId",db.Integer,db.ForeignKey("tbl_dk_reg_num_type.RegNumTypeId"))
	UId = db.Column("UId",db.Integer,db.ForeignKey("tbl_dk_users.UId"))
	RegNumPrefix = db.Column("RegNumPrefix",db.String(100))
	RegNumLastNum = db.Column("RegNumLastNum",db.Integer,nullable=False)
	RegNumSuffix = db.Column("RegNumSuffix",db.String(100))

	def registerLastNum(self,RegNumLastNum):
		self.RegNumLastNum+=1

	def to_json_api(self):
		data = {
			"RegNumId": self.RegNumId,
			"RegNumGuid": self.RegNumGuid,
			"RegNumTypeId": self.RegNumTypeId,
			"UId": self.UId,
			"RegNumPrefix": self.RegNumPrefix,
			"RegNumLastNum": self.RegNumLastNum,
			"RegNumSuffix": self.RegNumSuffix
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data