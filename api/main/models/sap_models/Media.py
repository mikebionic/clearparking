from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db
from . import AddInf, BaseModel
from main.base.dataMethods import apiDataFormat


# !!! TODO: Tags many to many
class Media(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_me_media"
	MediaId = db.Column("MediaId",db.Integer,nullable=False,primary_key=True)
	LangId = db.Column("LangId",db.Integer,db.ForeignKey("tbl_dk_language.LangId"))
	MediaCatId = db.Column("MediaCatId",db.Integer,db.ForeignKey("tbl_me_media_category.MediaCatId"))
	TagId = db.Column("TagId",db.Integer,db.ForeignKey("tbl_me_tag.TagId"))
	MediaGuid = db.Column("MediaGuid",UUID(as_uuid=True),unique=True)
	IsHidden = db.Column("IsHidden",db.Boolean,default=False)
	MediaName = db.Column("MediaName",db.String(500))
	MediaTitle = db.Column("MediaTitle",db.String(500))
	MediaDesc = db.Column("MediaDesc",db.String)
	MediaBody = db.Column("MediaBody",db.String)
	MediaAuthor = db.Column("MediaAuthor",db.String(500))
	MediaUrl = db.Column("MediaUrl",db.String(1000))
	MediaDate = db.Column("MediaDate",db.DateTime,default=datetime.now)
	MediaIsFeatured = db.Column("MediaIsFeatured",db.Boolean,default=False)
	MediaViewCnt = db.Column("MediaViewCnt",db.Integer)
	# Tag = db.relationship("Tag",foreign_keys=MediaId,backref='media',lazy=True)

	def to_json_api(self):
		data = {
			"MediaId": self.MediaId,
			"LangId": self.LangId,
			"MediaCatId": self.MediaCatId,
			"TagId": self.TagId,
			"MediaGuid": self.MediaGuid,
			"IsHidden": self.IsHidden,
			"MediaName": self.MediaName,
			"MediaTitle": self.MediaTitle,
			"MediaDesc": self.MediaDesc,			
			"MediaBody": self.MediaBody,
			"MediaAuthor": self.MediaAuthor,
			"MediaUrl": self.MediaUrl,
			"MediaDate": apiDataFormat(self.MediaDate),
			"MediaIsFeatured": self.MediaIsFeatured,
			"MediaViewCnt": self.MediaViewCnt,
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data