from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db

from main.base.dataMethods import configureFloat, apiDataFormat


class InvoiceFich_akhasap(db.Model):
	__tablename__ = "tbl_mg_fich"
	__table_args__ = {'implicit_returning': False}
	FichId = db.Column("fich_id",db.Integer,nullable=False,primary_key=True)
	InvId = db.Column("inv_id",db.Integer)
	InvGuid = db.Column("fich_id_guid",UUID(as_uuid=True),unique=True)
	InvTypeId = db.Column("fich_type_id",db.Integer)
	RpAccId = db.Column("arap_id",db.Integer)
	DivId = db.Column("div_id",db.Integer)
	WhId = db.Column("wh_id",db.Integer)
	WpId = db.Column("p_id",db.Integer)
	InvRegNo = db.Column("fich_code",db.String(100),nullable=False,unique=True)
	InvDesc = db.Column("fich_desc",db.String(500))
	InvDate = db.Column("fich_date",db.DateTime,default=datetime.now)
	InvTotal = db.Column("fich_total",db.Float)
	InvDiscountAmount = db.Column("fich_discount",db.Float,default=0.0)
	InvFTotal = db.Column("fich_nettotal",db.Float,default=0.0)

	def to_json_api(self):
		data = {
			"InvId": self.InvId,
			"InvGuid": self.InvGuid,
			"InvTypeId": self.InvTypeId,
			"RpAccId": self.RpAccId,
			"DivId": self.DivId,
			"WhId": self.WhId,
			"WpId": self.WpId,
			"InvRegNo": self.InvRegNo,
			"InvDesc": self.InvDesc,
			"InvDate": apiDataFormat(self.InvDate),
			"InvTotal": configureFloat(self.InvTotal),
			"InvDiscountAmount": self.InvDiscountAmount,
			"InvFTotal": configureFloat(self.InvTotal),
		}

		return data

class Invoice_akhasap(db.Model):
	__tablename__ = "tbl_mg_invoice"
	__table_args__ = {'implicit_returning': False}
	InvId = db.Column("inv_id",db.Integer,nullable=False,primary_key=True)
	InvGuid = db.Column("inv_id_guid",UUID(as_uuid=True),unique=True)
	InvTypeId = db.Column("inv_type_id",db.Integer)
	RpAccId = db.Column("arap_id",db.Integer)
	DivId = db.Column("div_id",db.Integer)
	WhId = db.Column("wh_id",db.Integer)
	WpId = db.Column("p_id",db.Integer)
	InvRegNo = db.Column("inv_code",db.String(100),nullable=False,unique=True)
	InvDesc = db.Column("inv_desc",db.String(500))
	InvDate = db.Column("inv_date",db.DateTime,default=datetime.now)
	InvTotal = db.Column("inv_total",db.Float)
	InvDiscountAmount = db.Column("inv_discount",db.Float,default=0.0)
	InvFTotal = db.Column("inv_nettotal",db.Float,default=0.0)
	FichId = db.Column("fich_id", db.Integer)

	def to_json_api(self):
		data = {
			"InvId": self.InvId,
			"InvGuid": self.InvGuid,
			"InvTypeId": self.InvTypeId,
			"RpAccId": self.RpAccId,
			"DivId": self.DivId,
			"WhId": self.WhId,
			"WpId": self.WpId,
			"InvRegNo": self.InvRegNo,
			"InvDesc": self.InvDesc,
			"InvDate": apiDataFormat(self.InvDate),
			"InvTotal": configureFloat(self.InvTotal),
			"InvDiscountAmount": self.InvDiscountAmount,
			"InvFTotal": configureFloat(self.InvTotal),
		}

		return data
