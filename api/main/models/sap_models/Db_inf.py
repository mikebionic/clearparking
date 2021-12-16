from sqlalchemy.dialects.postgresql import UUID

from main import db


class Db_inf(db.Model):
	__tablename__ = "tbl_dk_db_inf"
	DbInfId = db.Column("DbInfId",db.Integer,nullable=False,primary_key=True)
	DbInfDbVer = db.Column("DbInfDbVer",db.String(100),nullable=False)
	DbInfGuid = db.Column("DbInfGuid",UUID(as_uuid=True))
	GCRecord = db.Column("GCRecord",db.Integer)

	def to_json_api(self):
		data = {
			"DbInfId": self.DbInfId,
			"DbInfDbVer": self.DbInfDbVer,
			"DbInfGuid": self.DbInfGuid,
			"GCRecord": self.GCRecord
		}
		return data