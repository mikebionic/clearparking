from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Rp_acc_resource(BaseModel, db.Model):
	__tablename__ = "tbl_dk_rp_acc_resource"
	RpAccResId = db.Column("RpAccResId",db.Integer,nullable=False,primary_key=True)
	RpAccResGuid = db.Column("RpAccResGuid",UUID(as_uuid=True),unique=True)
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))

	def to_json_api(self):
		data = {
			"RpAccResId": self.RpAccResId,
			"RpAccResGuid": self.RpAccResGuid,
			"RpAccId": self.RpAccId,
			"ResId": self.ResId
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data