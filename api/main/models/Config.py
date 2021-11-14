from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Config(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_config"
	CfId = db.Column("CfId",db.Integer,primary_key=True)
	MainCfId = db.Column("MainCfId",db.Integer)
	CfTypeId = db.Column("CfTypeId",db.Integer,db.ForeignKey("tbl_dk_config_type.CfTypeId"))
	CfGuid = db.Column("CfGuid",UUID(as_uuid=True))
	CfName = db.Column("CfName",db.String(100),nullable=False)
	CfDesc = db.Column("CfDesc",db.String(500))
	CfIntVal = db.Column("CfIntVal",db.Integer)
	CfStringVal = db.Column("CfStringVal",db.String(500))

	def to_json_api(self):
		data = {
			"CfId": self.CfId,
			"MainCfId": self.MainCfId,
			"CfTypeId": self.CfTypeId,
			"CfGuid": self.CfGuid,
			"CfName": self.CfName,
			"CfDesc": self.CfDesc,
			"CfIntVal": self.CfIntVal,
			"CfStringVal": self.CfStringVal
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data