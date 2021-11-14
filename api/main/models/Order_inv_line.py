from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db
from main.models import AddInf, BaseModel
from main.base.dataMethods import configureFloat, apiDataFormat


class Order_inv_line(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_order_inv_line"
	OInvLineId = db.Column("OInvLineId",db.Integer,nullable=False,primary_key=True)
	OInvLineGuid = db.Column("OInvLineGuid",UUID(as_uuid=True),unique=True)
	OInvId = db.Column("OInvId",db.Integer,db.ForeignKey("tbl_dk_order_inv.OInvId"))
	UnitId = db.Column("UnitId",db.Integer,db.ForeignKey("tbl_dk_unit.UnitId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	LastVendorId = db.Column("LastVendorId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	OInvLineRegNo = db.Column("OInvLineRegNo",db.String(100),nullable=False,unique=True)
	OInvLineDesc = db.Column("OInvLineDesc",db.String(500))
	OInvLineAmount = db.Column("OInvLineAmount",db.Float,default=0.0)
	OInvLinePrice = db.Column("OInvLinePrice",db.Float,default=0.0)
	OInvLineTotal = db.Column("OInvLineTotal",db.Float,default=0.0)
	OInvLineExpenseAmount = db.Column("OInvLineExpenseAmount",db.Float,default=0.0)
	OInvLineTaxAmount = db.Column("OInvLineTaxAmount",db.Float,default=0.0)
	OInvLineDiscAmount = db.Column("OInvLineDiscAmount",db.Float,default=0.0)
	OInvLineFTotal = db.Column("OInvLineFTotal",db.Float,default=0.0)
	OInvLineDate = db.Column("OInvLineDate",db.DateTime,default=datetime.now)
	ExcRateValue = db.Column("ExcRateValue",db.Float,default=0.0)

	def to_json_api(self):
		data = {
			"OInvLineId": self.OInvLineId,
			"OInvLineGuid": self.OInvLineGuid,
			"OInvId": self.OInvId,
			"UnitId": self.UnitId,
			"CurrencyId": self.CurrencyId,
			"ResId": self.ResId,
			"LastVendorId": self.LastVendorId,
			"OInvLineRegNo": self.OInvLineRegNo,
			"OInvLineDesc": self.OInvLineDesc,
			"OInvLineAmount": configureFloat(self.OInvLineAmount),
			"OInvLinePrice": configureFloat(self.OInvLinePrice),
			"OInvLineTotal": configureFloat(self.OInvLineTotal),
			"OInvLineExpenseAmount": configureFloat(self.OInvLineExpenseAmount),
			"OInvLineTaxAmount": configureFloat(self.OInvLineTaxAmount),
			"OInvLineDiscAmount": configureFloat(self.OInvLineDiscAmount),
			"OInvLineFTotal": configureFloat(self.OInvLineFTotal),
			"OInvLineDate": apiDataFormat(self.OInvLineDate),
			"ExcRateValue": configureFloat(self.ExcRateValue)
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data