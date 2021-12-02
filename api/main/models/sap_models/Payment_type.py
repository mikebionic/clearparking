from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Payment_type(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_payment_type"
	PtId = db.Column("PtId",db.Integer,nullable=False,primary_key=True)
	PtGuid = db.Column("PtGuid",UUID(as_uuid=True),unique=True)
	PtName = db.Column("PtName",db.String(100),nullable=False)
	PtDesc = db.Column("PtDesc",db.String(500))
	PtVisibleIndex = db.Column("PtVisibleIndex",db.Integer,default=0)
	Order_inv = db.relationship("Order_inv",backref='payment_type',lazy=True)
	Invoice = db.relationship("Invoice",backref='payment_type',lazy=True)

	def to_json_api(self):
		data = {
			"PtId": self.PtId,
			"PtGuid": self.PtGuid,
			"PtName": self.PtName,
			"PtDesc": self.PtDesc,
			"PtVisibleIndex": self.PtVisibleIndex
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data