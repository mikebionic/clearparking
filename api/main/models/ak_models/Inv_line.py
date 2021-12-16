from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db

class Inv_line(db.Model):
	__tablename__ = "tbl_mg_fich_line"
	__table_args__ = {'implicit_returning': False}
	InvLineId = db.Column("fich_line_id",db.Integer,nullable=False,primary_key=True)
	InvLineGuid = db.Column("fich_line_id_guid",UUID(as_uuid=True),unique=True)
	InvId = db.Column("fich_id",db.Integer)
	UnitId = db.Column("unit_det_id",db.Integer)
	ResId = db.Column("material_id",db.Integer)
	InvLineRegNo = db.Column("spe_code",db.String(100))
	InvLineDesc = db.Column("fich_line_desc",db.String(500))
	InvLineAmount = db.Column("fich_line_amount",db.Float)
	InvLinePrice = db.Column("fich_line_price",db.Float,default=0.0)
	InvLineTotal = db.Column("fich_line_total",db.Float,default=0.0)
	InvLineDiscAmount = db.Column("fich_line_disc_amount",db.Float,default=0.0)
	InvLineFTotal = db.Column("fich_line_nettotal",db.Float,default=0.0)
	InvLineDate = db.Column("fich_line_date",db.DateTime,default=datetime.now)
	ExcRateValue = db.Column("rep_rate",db.Float,default=0.0)

	def to_json_api(self):
		data = {
			"InvLineId": self.InvLineId,
			"InvLineGuid": self.InvLineGuid,
			"InvId": self.InvId,
			"UnitId": self.UnitId,
			"ResId": self.ResId,
			"InvLineRegNo": self.InvLineRegNo,
			"InvLineDesc": self.InvLineDesc,
			"InvLineAmount": self.InvLineAmount,
			"InvLinePrice": self.InvLinePrice,
			"InvLineTotal": self.InvLineTotal,
			"InvLineDiscAmount": self.InvLineDiscAmount,
			"InvLineFTotal": self.InvLineFTotal,
			"InvLineDate": self.InvLineDate,
			"ExcRateValue": self.ExcRateValue,
		}

		return data
