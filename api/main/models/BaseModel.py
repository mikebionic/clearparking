from main import db
from datetime import datetime
from main.base.dataMethods import apiDataFormat


class BaseModel(object):
	CreatedDate = db.Column("CreatedDate",db.DateTime,default=datetime.now())
	ModifiedDate = db.Column("ModifiedDate",db.DateTime,default=datetime.now(),onupdate=datetime.now())
	SyncDateTime = db.Column("SyncDateTime",db.DateTime,default=datetime.now())
	CreatedUId = db.Column("CreatedUId",db.Integer)
	ModifiedUId = db.Column("ModifiedUId",db.Integer)
	GCRecord = db.Column("GCRecord",db.Integer)

	def createdInfo(self, UId):
		self.CreatedUId = UId

	def modifiedInfo(self, UId):
		self.ModifiedDate = datetime.now()
		self.ModifiedUId = UId
	
	@property
	def is_deleted(self):
		return 1 if self.GCRecord else 0

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)
	
	def to_json_api(self):
		return {
			"CreatedDate": apiDataFormat(self.CreatedDate),
			"ModifiedDate": apiDataFormat(self.ModifiedDate),
			"SyncDateTime": apiDataFormat(self.SyncDateTime),
			"CreatedUId": self.CreatedUId,
			"ModifiedUId": self.ModifiedUId,
			"GCRecord": self.GCRecord
		}