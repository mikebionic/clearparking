from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Order_inv_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_order_inv_type"
	OInvTypeId = db.Column("OInvTypeId",db.Integer,nullable=False,primary_key=True)
	OInvTypeGuid = db.Column("OInvTypeGuid",UUID(as_uuid=True),unique=True)
	OInvTypeName_tkTM = db.Column("OInvTypeName_tkTM",db.String(100),nullable=False)
	OInvTypeDesc_tkTM = db.Column("OInvTypeDesc_tkTM",db.String(500))
	OInvTypeName_ruRU = db.Column("OInvTypeName_ruRU",db.String(100))
	OInvTypeDesc_ruRU = db.Column("OInvTypeDesc_ruRU",db.String(500))
	OInvTypeName_enUS = db.Column("OInvTypeName_enUS",db.String(100))
	OInvTypeDesc_enUS = db.Column("OInvTypeDesc_enUS",db.String(500))
	Order_inv = db.relationship("Order_inv",backref='order_inv_type',lazy=True)

	def to_json_api(self):
		data = {
			"OInvTypeId": self.OInvTypeId,
			"OInvTypeGuid": self.OInvTypeGuid,
			"OInvTypeName_tkTM": self.OInvTypeName_tkTM,
			"OInvTypeDesc_tkTM": self.OInvTypeDesc_tkTM,
			"OInvTypeName_ruRU": self.OInvTypeName_ruRU,
			"OInvTypeDesc_ruRU": self.OInvTypeDesc_ruRU,
			"OInvTypeName_enUS": self.OInvTypeName_enUS,
			"OInvTypeDesc_enUS": self.OInvTypeDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data