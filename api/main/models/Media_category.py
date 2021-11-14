from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel

# !!! TODO: add image and translation references
class Media_category(BaseModel, db.Model):
	__tablename__ = "tbl_me_media_category"
	MediaCatId = db.Column("MediaCatId",db.Integer,nullable=False,primary_key=True)
	MediaCatGuid = db.Column("MediaCatGuid",UUID(as_uuid=True),unique=True)
	MediaOwnerCatId = db.Column("MediaOwnerCatId",db.Integer,db.ForeignKey("tbl_me_media_category.MediaCatId"))
	MediaCatVisibleIndex = db.Column("MediaCatVisibleIndex",db.Integer,default=0)
	IsMain = db.Column("IsMain",db.Boolean,default=False)
	MediaCatName = db.Column("MediaCatName",db.String(100),nullable=False)
	MediaCatDesc = db.Column("MediaCatDesc",db.String(500),default='')
	MediaCatIconName = db.Column("MediaCatIconName",db.String(100))
	MediaCatIconFilePath = db.Column("MediaCatIconFilePath",db.String(255))
	MediaCatIconData = db.Column("MediaCatIconData",db.String(100000))
	Media = db.relationship("Media",backref='media_category',lazy=True)
	Media_category = db.relationship("Media_category",remote_side=MediaCatId,backref='subcategory',lazy=True)

	def to_json_api(self):
		data = {
			"MediaCatId": self.MediaCatId,
			"MediaCatGuid": self.MediaCatGuid,
			"MediaOwnerCatId": self.MediaOwnerCatId or 0,
			"MediaCatVisibleIndex": self.MediaCatVisibleIndex or 0,
			"IsMain": self.IsMain,
			"MediaCatName": self.MediaCatName,
			"MediaCatDesc": self.MediaCatDesc,
			"MediaCatIconName": self.MediaCatIconName,
			"MediaCatIconFilePath": self.MediaCatIconFilePath,
			"MediaCatIconData": self.MediaCatIconData
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data