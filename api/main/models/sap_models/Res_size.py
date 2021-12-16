from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel

class Res_size(BaseModel, db.Model):
	__tablename__ = "tbl_dk_res_size"
	RsId = db.Column("RsId",db.Integer,nullable=False,primary_key=True)
	RsGuid = db.Column("RsGuid",UUID(as_uuid=True),unique=True)
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	SizeId = db.Column("SizeId",db.Integer,db.ForeignKey("tbl_dk_size.SizeId"))

	def to_json_api(self):
		data = {
			"RsId": self.RsId,
			"RsGuid": self.RsGuid,
			"ResId": self.ResId,
			"SizeId": self.SizeId
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data