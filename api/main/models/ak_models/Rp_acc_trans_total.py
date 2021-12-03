from sqlalchemy.dialects.postgresql import UUID

from main import db

class Rp_acc_trans_total(db.Model):
	__tablename__ = "tbl_dk_rp_acc_trans_total"
	RpAccTrTotId = db.Column("arap_total_id",db.Integer,nullable=False,primary_key=True)
	RpAccTrTotGuid = db.Column("arap_total_id_guid",UUID(as_uuid=True),unique=True)
	RpAccId = db.Column("arap_id",db.Integer)
	RpAccTrTotBalance = db.Column("arap_total_balance",db.Float,default=0.0)
	RpAccTrTotDebit = db.Column("arap_total_debit",db.Float,default=0.0)
	RpAccTrTotCredit = db.Column("arap_total_credit",db.Float,default=0.0)

	def to_json_api(self):
		data = {
			"RpAccTrTotId": self.RpAccTrTotId,
			"RpAccTrTotGuid": self.RpAccTrTotGuid,
			"RpAccId": self.RpAccId,
			"RpAccTrTotBalance": self.RpAccTrTotBalance,
			"RpAccTrTotDebit": self.RpAccTrTotDebit,
			"RpAccTrTotCredit": self.RpAccTrTotCredit,
		}

		return data