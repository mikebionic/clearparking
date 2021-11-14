from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Tag(BaseModel, db.Model):
	__tablename__ = "tbl_me_tag"
	TagId = db.Column("TagId",db.Integer,nullable=False,primary_key=True)
	TagGuid = db.Column("TagGuid",UUID(as_uuid=True),unique=True)
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	# MediaId = db.Column("MediaId",db.Integer,db.ForeignKey("tbl_me_media.MediaId"))
	ImgId = db.Column("ImgId",db.Integer,db.ForeignKey("tbl_dk_image.ImgId"))
	IsMain = db.Column("IsMain",db.Boolean,default=False)
	TagName = db.Column("TagName",db.String(100),nullable=False)
	TagSize = db.Column("TagSize",db.String(500))
	TagLabel = db.Column("TagLabel",db.String(255))
	TagStyle = db.Column("TagStyle",db.String(500))
	TagIconName = db.Column("TagIconName",db.String(255))
	TagIconFilePath = db.Column("TagIconFilePath",db.String(255))
	TagIconData = db.Column("TagIconData")
	Media = db.relationship("Media",backref='tag',lazy=True)

	def to_json_api(self):
		data = {
			"TagId": self.TagId,
			"TagGuid": self.TagGuid,
			"ResId": self.ResId,
			"ImgId": self.ImgId,
			"IsMain": self.IsMain,
			"TagName": self.TagName,
			"TagSize": self.TagSize,
			"TagLabel": self.TagLabel,
			"TagStyle": self.TagStyle,
			"TagIconName": self.TagIconName,
			"TagIconFilePath": self.TagIconFilePath,
			"TagIconData": self.TagIconData
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data