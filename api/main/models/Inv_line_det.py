from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Inv_line_det(BaseModel, db.Model):
	__tablename__ = "tbl_dk_inv_line_det"
	InvLineDetId = db.Column("InvLineDetId",db.Integer,nullable=False,primary_key=True)
	InvLineDetGuid = db.Column("InvLineDetGuid",UUID(as_uuid=True),unique=True)
	InvLineId = db.Column("InvLineId",db.Integer,db.ForeignKey("tbl_dk_inv_line.InvLineId"))
	InvLineDetTypeId = db.Column("InvLineDetTypeId",db.Integer,db.ForeignKey("tbl_dk_inv_line_det_type.InvLineDetTypeId"))
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	InvLineDetResSN = db.Column("InvLineDetResSN",db.String(100))
	InvLineDetSLStartDate = db.Column("InvLineDetSLStartDate",db.DateTime)
	InvLineDetSLEndDate = db.Column("InvLineDetSLEndDate",db.DateTime)
	InvLineDetAmount = db.Column("InvLineDetAmount",db.Float)
	InvLineDetAmountBalance = db.Column("InvLineDetAmountBalance",db.Float)

	def to_json_api(self):
		data = {
			"InvLineDetId": self.InvLineDetId,
			"InvLineDetGuid": self.InvLineDetGuid,
			"InvLineId": self.InvLineId,
			"InvLineDetTypeId": self.InvLineDetTypeId,
			"ResId": self.ResId,
			"InvLineDetResSN": self.InvLineDetResSN,
			"InvLineDetSLStartDate": self.InvLineDetSLStartDate,
			"InvLineDetSLEndDate": self.InvLineDetSLEndDate,
			"InvLineDetAmount": self.InvLineDetAmount,
			"InvLineDetAmountBalance": self.InvLineDetAmountBalance
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data