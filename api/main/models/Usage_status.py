from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Usage_status(BaseModel, db.Model):
	__tablename__ = "tbl_dk_usage_status"
	UsageStatusId = db.Column("UsageStatusId",db.Integer,nullable=False,primary_key=True)
	UsageStatusGuid = db.Column("UsageStatusGuid",UUID(as_uuid=True),unique=True)
	UsageStatusName_tkTM = db.Column("UsageStatusName_tkTM",db.String(100))
	UsageStatusDesc_tkTM = db.Column("UsageStatusDesc_tkTM",db.String(500))
	UsageStatusName_ruRU = db.Column("UsageStatusName_ruRU",db.String(100))
	UsageStatusDesc_ruRU = db.Column("UsageStatusDesc_ruRU",db.String(500))
	UsageStatusName_enUS = db.Column("UsageStatusName_enUS",db.String(100))
	UsageStatusDesc_enUS = db.Column("UsageStatusDesc_enUS",db.String(500))
	Resource = db.relationship("Resource",backref='usage_status',lazy=True)
	Res_price_group = db.relationship("Res_price_group",backref='usage_status',lazy=True)
	Res_price_rule = db.relationship("Res_price_rule",backref='usage_status',lazy=True)

	def to_json_api(self):
		data = {
			"UsageStatusId": self.UsageStatusId,
			"UsageStatusGuid": self.UsageStatusGuid,
			"UsageStatusName_tkTM": self.UsageStatusName_tkTM,
			"UsageStatusDesc_tkTM": self.UsageStatusDesc_tkTM,
			"UsageStatusName_ruRU": self.UsageStatusName_ruRU,
			"UsageStatusDesc_ruRU": self.UsageStatusDesc_ruRU,
			"UsageStatusName_enUS": self.UsageStatusName_enUS,
			"UsageStatusDesc_enUS": self.UsageStatusDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data