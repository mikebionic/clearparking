from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel
from main.base.dataMethods import apiDataFormat


# !!! TODO: Link with UId, Attachments, Tags (hashtags)
class App_release(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_me_app_release"
	AppReleaseId = db.Column("AppReleaseId",db.Integer,nullable=False,primary_key=True)
	AppReleaseGuid = db.Column("AppReleaseGuid",UUID(as_uuid=True),unique=True)
	AppReleaseDate = db.Column("AppReleaseDate",db.DateTime)
	AppVersion = db.Column("AppVersion",db.String(100))
	AppPlatform = db.Column("AppPlatform",db.String(100))
	AppName = db.Column("AppName",db.String(100))
	AppDesc = db.Column("AppDesc",db.String)
	AppMinimalOsVersion = db.Column("AppMinimalOsVersion",db.String(100))
	AppDownloadUrl = db.Column("AppDownloadUrl",db.String(100))

	def to_json_api(self):
		data = {
			"AppReleaseId": self.AppReleaseId,
			"AppReleaseGuid": self.AppReleaseGuid,
			"AppReleaseDate": apiDataFormat(self.AppReleaseDate),
			"AppVersion": self.AppVersion,
			"AppPlatform": self.AppPlatform,
			"AppName": self.AppName,
			"AppDesc": self.AppDesc,
			"AppMinimalOsVersion": self.AppMinimalOsVersion,
			"AppDownloadUrl": self.AppDownloadUrl,
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data