from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Contact(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_contact"
	ContId = db.Column("ContId",db.Integer,nullable=False,primary_key=True)
	ContGuid = db.Column("ContGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	BankId = db.Column("BankId",db.Integer,db.ForeignKey("tbl_dk_bank.BankId"))
	ContTypeId = db.Column("ContTypeId",db.Integer,db.ForeignKey("tbl_dk_contact_type.ContTypeId"))
	ContValue = db.Column("ContValue",db.String(200),nullable=False)
	ContDesc = db.Column("ContDesc",db.String(500))

	def to_json_api(self):
		data = {
			"ContId": self.ContId,
			"ContGuid": self.ContGuid,
			"CId": self.CId,
			"EmpId": self.EmpId,
			"RpAccId": self.RpAccId,
			"BankId": self.BankId,
			"ContTypeId": self.ContTypeId,
			"ContValue": self.ContValue,
			"ContDesc": self.ContDesc
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data