from sqlalchemy.dialects.postgresql import UUID

from main import db

class Resource_akhasap(db.Model):
	__tablename__ = "tbl_mg_materials"
	ResId = db.Column("material_id",db.Integer,nullable=False,primary_key=True)
	ResGuid = db.Column("ResGuid",UUID(as_uuid=True),unique=True)
	ResName = db.Column("material_name",db.String)
	ResDesc = db.Column("spe_code2",db.String)

	def to_json_api(self):
		data = {
			"ResId": self.ResId,
			"ResGuid": self.ResGuid,
			"ResName": self.ResName,
			"ResDesc": self.ResDesc
		}


		return data
