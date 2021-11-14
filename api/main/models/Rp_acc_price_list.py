from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Rp_acc_price_list(BaseModel, db.Model):
	__tablename__ = "tbl_dk_rp_acc_price_list"
	RpAccPLId = db.Column("RpAccPLId",db.Integer,nullable=False,primary_key=True)
	RpAccPLGuid = db.Column("RpAccPLGuid",UUID(as_uuid=True),unique=True)
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	UnitName = db.Column("UnitName",db.String(100))
	ResBarcode = db.Column("ResBarcode",db.String(100),nullable=False)
	ResName = db.Column("ResName",db.String(100),nullable=False)
	ResDesc = db.Column("ResDesc",db.String(500))
	RpAccPLValue = db.Column("RpAccPLValue",db.Float,default=0)
	RpAccPLDesc = db.Column("RpAccPLDesc",db.String(500))
	RpAccPLStartDate = db.Column("RpAccPLStartDate",db.DateTime)
	RpAccPLEndDate = db.Column("RpAccPLEndDate",db.DateTime)

	def to_json_api(self):
		data = {
			"RpAccPLId": self.RpAccPLId,
			"RpAccPLGuid": self.RpAccPLGuid,
			"RpAccId": self.RpAccId,
			"UnitName": self.UnitName,
			"ResBarcode": self.ResBarcode,
			"ResName": self.ResName,
			"ResDesc": self.ResDesc,
			"RpAccPLValue": self.RpAccPLValue,
			"RpAccPLDesc": self.RpAccPLDesc,
			"RpAccPLStartDate": self.RpAccPLStartDate,
			"RpAccPLEndDate": self.RpAccPLEndDate
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data