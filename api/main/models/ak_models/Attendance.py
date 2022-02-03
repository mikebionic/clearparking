
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from main import db

class Attendance_akhasap(db.Model):
	__tablename__ = "tbl_mg_arap_attandence"
	AttId = db.Column("arap_att_id",db.Integer,nullable=False,primary_key=True)
	AttGuid = db.Column("arap_att_id_guid",UUID(as_uuid=True),unique=True)
	RpAccId = db.Column("arap_id",db.Integer)
	AttTypeId = db.Column("arap_att_type",db.Integer)
	AttDate = db.Column("arap_att_date",db.DateTime,default=datetime.now(),nullable=False)

	def to_json_api(self):
		data = {
			"AttId": self.AttId,
			"AttGuid": self.AttGuid,
			"RpAccId": self.RpAccId,
			"AttTypeId": self.AttTypeId,
			"AttDate": self.AttDate,
		}

		return data
