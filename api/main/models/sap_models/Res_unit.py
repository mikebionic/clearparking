from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel


class Res_unit(BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_unit"
	ResUnitId = db.Column("ResUnitId",db.Integer,nullable=False,primary_key=True)
	ResUnitGuid = db.Column("ResUnitGuid",UUID(as_uuid=True),unique=True)
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	ResUnitUnitId = db.Column("ResUnitUnitId",db.Integer,db.ForeignKey("tbl_dk_unit.UnitId"))
	ResUnitConvAmount = db.Column("ResUnitConvAmount",db.Float,nullable=False)
	ResUnitConvTypeId = db.Column("ResUnitConvTypeId",db.Integer,nullable=False)

	def to_json_api(self):
		data = {
			"ResUnitId": self.ResUnitId,
			"ResUnitGuid": self.ResUnitGuid,
			"ResId": self.ResId,
			"ResUnitUnitId": self.ResUnitUnitId,
			"ResUnitConvAmount": self.ResUnitConvAmount,
			"ResUnitConvTypeId": self.ResUnitConvTypeId
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data