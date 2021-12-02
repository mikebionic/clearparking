from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Pred_reg_num(BaseModel, db.Model):
	__tablename__ = "tbl_dk_pred_regnum"
	PredRegNumId = db.Column("PredRegNumId",db.Integer,nullable=False,primary_key=True)
	PredRegNumGuid = db.Column("PredRegNumGuid",UUID(as_uuid=True),unique=True)
	RegNumTypeId = db.Column("RegNumTypeId",db.Integer,db.ForeignKey("tbl_dk_reg_num_type.RegNumTypeId"))
	RegNum = db.Column("RegNum",db.String(100),nullable=False)

	def to_json_api(self):
		data = {
			"PredRegNumId": self.PredRegNumId,
			"PredRegNumGuid": self.PredRegNumGuid,
			"RegNumTypeId": self.RegNumTypeId,
			"RegNum": self.RegNum
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data