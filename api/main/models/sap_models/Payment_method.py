from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Payment_method(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_payment_method"
	PmId = db.Column("PmId",db.Integer,nullable=False,primary_key=True)
	PmGuid = db.Column("PmGuid",UUID(as_uuid=True),unique=True)
	PmName = db.Column("PmName",db.String(100),nullable=False)
	PmDesc = db.Column("PmDesc",db.String(500))
	PmVisibleIndex = db.Column("PmVisibleIndex",db.Integer,default=0)
	Order_inv = db.relationship("Order_inv",backref='payment_method',lazy=True)
	Invoice = db.relationship("Invoice",backref='payment_method',lazy=True)

	def to_json_api(self):
		data = {
			"PmId": self.PmId,
			"PmGuid": self.PmGuid,
			"PmName": self.PmName,
			"PmDesc": self.PmDesc,
			"PmVisibleIndex": self.PmVisibleIndex
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data