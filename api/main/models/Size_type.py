from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Size_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_size_type"
	SizeTypeId = db.Column("SizeTypeId",db.Integer,nullable=False,primary_key=True)
	SizeTypeGuid = db.Column("SizeTypeGuid",UUID(as_uuid=True),unique=True)
	SizeTypeName = db.Column("SizeTypeName",db.String(100),nullable=False)
	SizeTypeDesc = db.Column("SizeTypeDesc",db.String(500))
	Size = db.relationship("Size",backref='size_type',lazy=True)

	def to_json_api(self):
		data = {
			"SizeTypeId": self.SizeTypeId,
			"SizeTypeGuid": self.SizeTypeGuid,
			"SizeTypeName": self.SizeTypeName,
			"SizeTypeDesc": self.SizeTypeDesc,
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data