from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Company(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_company"
	CId = db.Column("CId",db.Integer,primary_key=True)
	CName = db.Column("CName",db.String(100),nullable=False)
	CFullName = db.Column("CFullName",db.String(500))
	CDesc = db.Column("CDesc",db.String(500))
	CGuid = db.Column("CGuid",UUID(as_uuid=True),unique=True)
	AccInfId = db.Column("AccInfId",db.Integer)
	CAddress = db.Column("CAddress",db.String(500))
	CAddressLegal = db.Column("CAddressLegal",db.String(500))
	CLatitude = db.Column("CLatitude",db.Float)
	CLongitude = db.Column("CLongitude",db.Float)
	Phone1 = db.Column("Phone1",db.String(100))
	Phone2 = db.Column("Phone2",db.String(100))
	Phone3 = db.Column("Phone3",db.String(100))
	Phone4 = db.Column("Phone4",db.String(100))
	CPostalCode = db.Column("CPostalCode",db.String(100))
	WebAddress = db.Column("WebAddress",db.String(100))
	CEmail = db.Column("CEmail",db.String(100))
	Accounting_info = db.relationship("Accounting_info",backref='company',lazy=True)
	Contact = db.relationship("Contact",backref='company',lazy=True)
	Division = db.relationship("Division",backref='company',lazy=True)
	Image = db.relationship("Image",backref='company',lazy=True)
	Location = db.relationship("Location",backref='company',lazy=True)
	Department_detail = db.relationship("Department_detail",backref='company',lazy=True)
	Warehouse = db.relationship("Warehouse",backref='company',lazy=True)
	Barcode = db.relationship("Barcode",backref='company',lazy=True)
	Rp_acc_transaction = db.relationship("Rp_acc_transaction",backref='company',lazy=True)
	Sale_card = db.relationship("Sale_card",backref='company',lazy=True)
	Work_period = db.relationship("Work_period",backref='company',lazy=True)
	Invoice = db.relationship("Invoice",backref='company',lazy=True)
	Order_inv = db.relationship("Order_inv",backref='company',lazy=True)
	Representative = db.relationship("Representative",backref='company',lazy=True)
	Res_total = db.relationship("Res_total",backref='company',lazy=True)
	Res_trans_inv = db.relationship("Res_trans_inv",backref='company',lazy=True)
	Rp_acc = db.relationship("Rp_acc",backref='company',lazy=True)
	User = db.relationship("User",backref='company',lazy=True)
	Wish = db.relationship("Wish",backref='company',lazy=True)
	Production = db.relationship("Production",backref='company',lazy=True)
	Resource = db.relationship("Resource",backref='company',lazy=True)
	Rating = db.relationship("Rating",backref='company',lazy=True)
	Slider = db.relationship("Slider",backref='company',lazy=True)
	Emp_recruitment = db.relationship("Emp_recruitment",backref='company',lazy=True)
	Staffing_table = db.relationship("Staffing_table",backref='company',lazy=True)
	Contract = db.relationship("Contract",backref='company',lazy=True)

	def to_json_api(self):
		data = {
			"CId": self.CId,
			"CName": self.CName,
			"CFullName": self.CFullName,
			"CDesc": self.CDesc,
			"CGuid": self.CGuid,
			"AccInfId": self.AccInfId,
			"CAddress": self.CAddress,
			"CAddressLegal": self.CAddressLegal,
			"CLatitude": self.CLatitude,
			"CLongitude": self.CLongitude,
			"Phone1": self.Phone1,
			"Phone2": self.Phone2,
			"Phone3": self.Phone3,
			"Phone4": self.Phone4,
			"CPostalCode": self.CPostalCode,
			"WebAddress": self.WebAddress,
			"CEmail": self.CEmail
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data