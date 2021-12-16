from main import db
from . import BaseModel


class Acc_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_acc_type"
	AccTypeId = db.Column("AccTypeId",db.Integer,primary_key=True)
	AccTypeName_tkTM = db.Column("AccTypeName_tkTM",db.String(100))
	AccTypeDesc_tkTm = db.Column("AccTypeDesc_tkTm",db.String(500))
	AccTypeName_ruRU = db.Column("AccTypeName_ruRU",db.String(100))
	AccTypeDesc_ruRU = db.Column("AccTypeDesc_ruRU",db.String(500))
	AccTypeName_enUS = db.Column("AccTypeName_enUS",db.String(100))
	AccTypeDesc_enUS = db.Column("AccTypeDesc_enUS",db.String(500))
	Accounting_info = db.relationship("Accounting_info",backref='acc_type',lazy=True)

	def to_json_api(self):
		data = {
			"AccTypeId": self.AccTypeId,
			"AccTypeName_tkTM": self.AccTypeName_tkTM,
			"AccTypeDesc_tkTm": self.AccTypeDesc_tkTm,
			"AccTypeName_ruRU": self.AccTypeName_ruRU,
			"AccTypeDesc_ruRU": self.AccTypeDesc_ruRU,
			"AccTypeName_enUS": self.AccTypeName_enUS,
			"AccTypeDesc_enUS": self.AccTypeDesc_enUS,
		}

		for key, value in BaseModel.to_json(self).items():
			data[key] = value

		return data