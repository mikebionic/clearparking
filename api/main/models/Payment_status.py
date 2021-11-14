from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Payment_status(BaseModel, db.Model):
	__tablename__ = "tbl_dk_payment_status"
	PaymStatusId = db.Column("PaymStatusId",db.Integer,nullable=False,primary_key=True)
	PaymStatusGuid = db.Column("PaymStatusGuid",UUID(as_uuid=True),unique=True)
	PaymStatusName_tkTM = db.Column("PaymStatusName_tkTM",db.String(100))
	PaymStatusDesc_tkTM = db.Column("PaymStatusDesc_tkTM",db.String(500))
	PaymStatusName_ruRU = db.Column("PaymStatusName_ruRU",db.String(100))
	PaymStatusDesc_ruRU = db.Column("PaymStatusDesc_ruRU",db.String(500))
	PaymStatusName_enUS = db.Column("PaymStatusName_enUS",db.String(100))
	PaymStatusDesc_enUS = db.Column("PaymStatusDesc_enUS",db.String(500))
	Order_inv = db.relationship("Order_inv",backref='payment_status',lazy=True)

	def to_json_api(self):
		data = {
			"PaymStatusId": self.PaymStatusId,
			"PaymStatusGuid": self.PaymStatusGuid,
			"PaymStatusName_tkTM": self.PaymStatusName_tkTM,
			"PaymStatusDesc_tkTM": self.PaymStatusDesc_tkTM,
			"PaymStatusName_ruRU": self.PaymStatusName_ruRU,
			"PaymStatusDesc_ruRU": self.PaymStatusDesc_ruRU,
			"PaymStatusName_enUS": self.PaymStatusName_enUS,
			"PaymStatusDesc_enUS": self.PaymStatusDesc_enUS,
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data