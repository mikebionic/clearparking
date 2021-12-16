from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Size(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_size"
	SizeId = db.Column("SizeId",db.Integer,nullable=False,primary_key=True)
	SizeGuid = db.Column("SizeGuid",UUID(as_uuid=True),unique=True)
	SizeName = db.Column("SizeName",db.String(100),nullable=False)
	SizeDesc = db.Column("SizeDesc",db.String(500))
	SizeTypeId = db.Column("SizeTypeId",db.Integer,db.ForeignKey("tbl_dk_size_type.SizeTypeId"))
	Res_size = db.relationship("Res_size",backref='size',lazy=True)

	def to_json_api(self):
		json_data = {
			"SizeId": self.SizeId,
			"SizeGuid": self.SizeGuid,
			"SizeName": self.SizeName,
			"SizeDesc": self.SizeDesc,
			"SizeTypeId": self.SizeTypeId
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data