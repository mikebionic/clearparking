from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Warehouse(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_warehouse"
	WhId = db.Column("WhId",db.Integer,nullable=False,primary_key=True)
	WhGuid = db.Column("WhGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	UsageStatusId = db.Column("UsageStatusId",db.Integer,db.ForeignKey("tbl_dk_usage_status.UsageStatusId"))
	WhName = db.Column("WhName",db.String(100),nullable=False)
	WhDesc = db.Column("WhDesc",db.String(500))
	Res_transaction = db.relationship("Res_transaction",backref='warehouse',lazy=True)
	Invoice = db.relationship("Invoice",backref='warehouse',lazy=True)
	Order_inv = db.relationship("Order_inv",backref='warehouse',lazy=True)
	Res_total = db.relationship("Res_total",backref='warehouse',lazy=True)
	Res_trans_inv = db.relationship("Res_trans_inv",foreign_keys='Res_trans_inv.WhIdIn',backref='warehouse',lazy=True)
	Res_trans_inv = db.relationship("Res_trans_inv",foreign_keys='Res_trans_inv.WhIdOut',backref='warehouse',lazy=True)
	Production = db.relationship("Production",foreign_keys='Production.WhIdIn',backref='warehouse',lazy=True)
	Production = db.relationship("Production",foreign_keys='Production.WhIdOut',backref='warehouse',lazy=True)

	def to_json_api(self):
		data = {
			"WhId": self.WhId,
			"WhGuid": self.WhGuid,
			"CId": self.CId,
			"DivId": self.DivId,
			"UsageStatusId": self.UsageStatusId,
			"WhName": self.WhName,
			"WhDesc": self.WhDesc,
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data