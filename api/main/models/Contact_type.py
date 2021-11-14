from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Contact_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_contact_type"
	ContTypeId = db.Column("ContTypeId",db.Integer,nullable=False,primary_key=True)
	ContTypeGuid = db.Column("ContTypeGuid",UUID(as_uuid=True),unique=True)
	ContTypeName_tkTM = db.Column("ContTypeName_tkTM",db.String(100))
	ContTypeDesc_tkTM = db.Column("ContTypeDesc_tkTM",db.String(500))
	ContTypeName_ruRU = db.Column("ContTypeName_ruRU",db.String(100))
	ContTypeDesc_ruRU = db.Column("ContTypeDesc_ruRU",db.String(500))
	ContTypeName_enUS = db.Column("ContTypeName_enUS",db.String(100))
	ContTypeDesc_enUS = db.Column("ContTypeDesc_enUS",db.String(500))
	Contact = db.relationship("Contact",backref='contact_type',lazy=True)

	def to_json_api(self):
		data = {
			"ContactTypeId": self.ContactTypeId,
			"ContactTypeGuid": self.ContactTypeGuid,
			"ContactTypeName_tkTM": self.ContactTypeName_tkTM,
			"ContactTypeDesc_tkTM": self.ContactTypeDesc_tkTM,
			"ContactTypeName_ruRU": self.ContactTypeName_ruRU,
			"ContactTypeDesc_ruRU": self.ContactTypeDesc_ruRU,
			"ContactTypeName_enUS": self.ContactTypeName_enUS,
			"ContactTypeDesc_enUS": self.ContactTypeDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data