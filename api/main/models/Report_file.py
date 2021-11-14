from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Report_file(BaseModel, db.Model):
	__tablename__ = "tbl_dk_report_file"
	RpFileId = db.Column("RpFileId",db.Integer,nullable=False,primary_key=True)
	RpFileGuid = db.Column("RpFileGuid",UUID(as_uuid=True),unique=True)
	RpFileTypeId = db.Column("RpFileTypeId",db.Integer,nullable=False,default=0)
	RpFileName = db.Column("RpFileName",db.String(100))
	RpFileDesc = db.Column("RpFileDesc",db.String(100))
	RpFileFileName = db.Column("RpFileFileName",db.String(100))
	RpIsDefault = db.Column("RpIsDefault",db.Boolean,default=False)

	def to_json_api(self):
		data = {
			"RpFileId": self.RpFileId,
			"RpFileGuid": self.RpFileGuid,
			"RpFileTypeId": self.RpFileTypeId,
			"RpFileName": self.RpFileName,
			"RpFileDesc": self.RpFileDesc,
			"RpFileFileName": self.RpFileFileName,
			"RpIsDefault": self.RpIsDefault
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data