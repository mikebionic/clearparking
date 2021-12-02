from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Bank(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_bank"
	BankId = db.Column("BankId",db.Integer,nullable=False,primary_key=True)
	BankGuid = db.Column("BankGuid",UUID(as_uuid=True),unique=True)
	MainContId = db.Column("MainContId",db.Integer,default=0)
	MainLocId = db.Column("MainLocId",db.Integer,default=0)
	BankName = db.Column("BankName",db.String(200),nullable=False)
	BankDesc = db.Column("BankDesc",db.String(500))
	BankCorAcc = db.Column("BankCorAcc",db.String(50))
	BankAccBik = db.Column("BankAccBik",db.String(50))
	Accounting_info = db.relationship("Accounting_info",backref='bank',lazy=True)
	Contact = db.relationship("Contact",backref='bank',lazy=True)
	Location = db.relationship("Location",backref='bank',lazy=True)

	def to_json_api(self):
		data = {
			"BankId": self.BankId,
			"BankGuid": self.BankGuid,
			"MainContId": self.MainContId,
			"MainLocId": self.MainLocId,
			"BankName": self.BankName,
			"BankDesc": self.BankDesc,
			"BankCorAcc": self.BankCorAcc,
			"BankAccBik": self.BankAccBik
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data