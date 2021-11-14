from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Res_price_group(BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_price_group"
	ResPriceGroupId = db.Column("ResPriceGroupId",db.Integer,nullable=False,primary_key=True)
	ResPriceGroupGuid = db.Column("ResPriceGroupGuid",UUID(as_uuid=True),unique=True)
	UsageStatusId = db.Column("UsageStatusId",db.Integer,db.ForeignKey("tbl_dk_usage_status.UsageStatusId"))
	ResPriceGroupName = db.Column("ResPriceGroupName",db.String(100),nullable=False)
	ResPriceGroupDesc = db.Column("ResPriceGroupDesc",db.String(500))
	ResPriceGroupAMEnabled = db.Column("ResPriceGroupAMEnabled",db.Boolean,default=False)
	FromResPriceTypeId = db.Column("FromResPriceTypeId",db.Integer,db.ForeignKey("tbl_dk_res_price_type.ResPriceTypeId"))
	ToResPriceTypeId = db.Column("ToResPriceTypeId",db.Integer,db.ForeignKey("tbl_dk_res_price_type.ResPriceTypeId"))
	ResPriceGroupAMPerc = db.Column("ResPriceGroupAMPerc",db.Float,default=0.0)
	RoundingType = db.Column("RoundingType",db.Integer,default=1)
	Res_price = db.relationship("Res_price",backref='res_price_group',lazy=True)
	Sale_card = db.relationship("Sale_card",backref='res_price_group',lazy=True)
	Res_price_rule = db.relationship("Res_price_rule",backref='res_price_group',lazy=True)
	User = db.relationship("User",backref='res_price_group',lazy=True)
	Rp_acc = db.relationship("Rp_acc",backref='res_price_group',lazy=True)

	def to_json_api(self):
		data = {
			"ResPriceGroupId": self.ResPriceGroupId,
			"ResPriceGroupGuid": self.ResPriceGroupGuid,
			"UsageStatusId": self.UsageStatusId,
			"ResPriceGroupName": self.ResPriceGroupName,
			"ResPriceGroupDesc": self.ResPriceGroupDesc,
			"ResPriceGroupAMEnabled": self.ResPriceGroupAMEnabled,
			"FromResPriceTypeId": self.FromResPriceTypeId,
			"ToResPriceTypeId": self.ToResPriceTypeId,
			"ResPriceGroupAMPerc": self.ResPriceGroupAMPerc,
			"RoundingType": self.RoundingType
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data