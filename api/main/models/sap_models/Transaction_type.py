from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Transaction_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_transaction_type"
	TransTypeId = db.Column("TransTypeId",db.Integer,nullable=False,primary_key=True)
	TransTypeGuid = db.Column("TransTypeGuid",UUID(as_uuid=True),unique=True)
	TransTypeName = db.Column("TransTypeName",db.String(100),nullable=False)
	TransTypeDesc = db.Column("TransTypeDesc",db.String(500))
	Rp_acc_transaction = db.relationship("Rp_acc_transaction",backref='transaction_type',lazy=True)

	def to_json_api(self):
		json_data = {
			"TransTypeId": self.TransTypeId,
			"TransTypeGuid": self.TransTypeGuid,
			"TransTypeName": self.TransTypeName,
			"TransTypeDesc": self.TransTypeDesc
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data