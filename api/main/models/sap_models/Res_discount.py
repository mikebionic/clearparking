from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Res_discount(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_discount"
	ResDiscId = db.Column("ResDiscId",db.Integer,nullable=False,primary_key=True)
	ResDiscGuid = db.Column("ResDiscGuid",UUID(as_uuid=True),unique=True)
	SaleCardId = db.Column("SaleCardId",db.Integer,db.ForeignKey("tbl_dk_sale_card.SaleCardId"))
	ResDiscRegNo = db.Column("ResDiscRegNo",db.String(100),nullable=False)
	SaleResId = db.Column("SaleResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	SaleResAmount = db.Column("SaleResAmount",db.Float,default=0.0)
	DiscTypeId = db.Column("DiscTypeId",db.Integer,db.ForeignKey("tbl_dk_discount_type.DiscTypeId"))
	DiscValue = db.Column("DiscValue",db.Float,default=0.0)
	DiscDesc = db.Column("DiscDesc",db.String(500))
	ResDiscStartDate = db.Column("ResDiscStartDate",db.DateTime)
	ResDiscEndDate = db.Column("ResDiscEndDate",db.DateTime)
	ResDiscIsActive = db.Column("ResDiscIsActive",db.Boolean,default=True)
	GiftResId = db.Column("GiftResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	GiftResAmount = db.Column("GiftResAmount",db.Float,default=0.0)
	GiftResDiscValue = db.Column("GiftResDiscValue",db.Float,default=0.0)
	Sale_card = db.relationship("Sale_card",backref='res_discount',foreign_keys='Sale_card.ResDiscId',lazy=True)

	def to_json_api(self):
		data = {
			"ResDiscId": self.ResDiscId,
			"ResDiscGuid": self.ResDiscGuid,
			"SaleCardId": self.SaleCardId,
			"ResDiscRegNo": self.ResDiscRegNo,
			"SaleResId": self.SaleResId,
			"SaleResAmount": self.SaleResAmount,
			"DiscTypeId": self.DiscTypeId,
			"DiscValue": self.DiscValue,
			"DiscDesc": self.DiscDesc,
			"ResDiscStartDate": self.ResDiscStartDate,
			"ResDiscEndDate": self.ResDiscEndDate,
			"ResDiscIsActive": self.ResDiscIsActive,
			"GiftResId": self.GiftResId,
			"GiftResAmount": self.GiftResAmount,
			"GiftResDiscValue": self.GiftResDiscValue
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data