from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Division(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_division"
	DivId = db.Column("DivId",db.Integer,nullable=False,primary_key=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivName = db.Column("DivName",db.String(100),nullable=False)
	DivDesc = db.Column("DivDesc",db.String(500))
	DivGuid = db.Column("DivGuid",UUID(as_uuid=True),unique=True)
	OwnerDivisionId = db.Column("OwnerDivisionId",db.Integer,default=0)
	User = db.relationship("User",backref='division')
	Department_detail = db.relationship("Department_detail",backref='division',lazy=True)
	Accounting_info = db.relationship("Accounting_info",backref='division',lazy=True)
	Barcode = db.relationship("Barcode",backref='division',lazy=True)
	Rp_acc = db.relationship("Rp_acc",backref='division',lazy=True)
	Res_trans_inv = db.relationship("Res_trans_inv",backref='division',lazy=True)
	Rp_acc_transaction = db.relationship("Rp_acc_transaction",backref='division',lazy=True)
	Sale_card = db.relationship("Sale_card",backref='division',lazy=True)
	Work_period = db.relationship("Work_period",backref='division',lazy=True)
	Invoice = db.relationship("Invoice",backref='division',lazy=True)
	Order_inv = db.relationship("Order_inv",backref='division',lazy=True)
	Representative = db.relationship("Representative",backref='division',lazy=True)
	Res_total = db.relationship("Res_total",backref='division',lazy=True)
	Wish = db.relationship("Wish",backref='division',lazy=True)
	Warehouse = db.relationship("Warehouse",backref='division',lazy=True)
	Production = db.relationship("Production",backref='division',lazy=True)
	Rating = db.relationship("Rating",backref='division',lazy=True)
	Resource = db.relationship("Resource",backref='division',lazy=True)
	Slider = db.relationship("Slider",backref='division',lazy=True)
	Employee = db.relationship("Employee",backref='division',lazy=True)
	Emp_recruitment = db.relationship("Emp_recruitment",backref='division',lazy=True)
	Staffing_table = db.relationship("Staffing_table",backref='division',lazy=True)
	Contract = db.relationship("Contract",backref='division',lazy=True)

	def to_json_api(self):
		data = {
			"DivId": self.DivId,
			"CId": self.CId,
			"DivName": self.DivName,
			"DivDesc": self.DivDesc,
			"DivGuid": self.DivGuid,
			"OwnerDivisionId": self.OwnerDivisionId
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data