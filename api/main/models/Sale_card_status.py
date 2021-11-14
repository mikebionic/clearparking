from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Sale_card_status(BaseModel,db.Model):
	__tablename__ = "tbl_dk_sale_card_status"
	SaleCardStatusId = db.Column("SaleCardStatusId",db.Integer,nullable=False,primary_key=True)
	SaleCardStatusGuid = db.Column("SaleCardStatusGuid",UUID(as_uuid=True),unique=True)
	SaleCardStatusName_tkTM = db.Column("SaleCardStatusName_tkTM",db.String(100))
	SaleCardStatusDesc_tkTM = db.Column("SaleCardStatusDesc_tkTM",db.String(500))
	SaleCardStatusName_ruRU = db.Column("SaleCardStatusName_ruRU",db.String(100))
	SaleCardStatusDesc_ruRU = db.Column("SaleCardStatusDesc_ruRU",db.String(500))
	SaleCardStatusName_enUS = db.Column("SaleCardStatusName_enUS",db.String(100))
	SaleCardStatusDesc_enUS = db.Column("SaleCardStatusDesc_enUS",db.String(500))
	Sale_card = db.relationship("Sale_card",backref='sale_card_status',lazy=True)

	def to_json_api(self):
		data = {
			"SaleCardStatusId": self.SaleCardStatusId,
			"SaleCardStatusGuid": self.SaleCardStatusGuid,
			"SaleCardStatusName_tkTM": self.SaleCardStatusName_tkTM,
			"SaleCardStatusDesc_tkTM": self.SaleCardStatusDesc_tkTM,
			"SaleCardStatusName_ruRU": self.SaleCardStatusName_ruRU,
			"SaleCardStatusDesc_ruRU": self.SaleCardStatusDesc_ruRU,
			"SaleCardStatusName_enUS": self.SaleCardStatusName_enUS,
			"SaleCardStatusDesc_enUS": self.SaleCardStatusDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data