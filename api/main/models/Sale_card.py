from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db
from main.models import AddInf, BaseModel


class Sale_card(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_sale_card"
	SaleCardId = db.Column("SaleCardId",db.Integer,nullable=False,primary_key=True)
	SaleCardGuid = db.Column("SaleCardGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	WpId = db.Column("WpId",db.Integer,db.ForeignKey("tbl_dk_work_period.WpId"))
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	CurrencyId = db.Column("CurrencyId",db.Integer,db.ForeignKey("tbl_dk_currency.CurrencyId"))
	SaleAgrId = db.Column("SaleAgrId",db.Integer,db.ForeignKey("tbl_dk_sale_agreement.SaleAgrId"))
	ResPriceGroupId = db.Column("ResPriceGroupId",db.Integer,db.ForeignKey("tbl_dk_res_price_group.ResPriceGroupId"))
	ResDiscId = db.Column("ResDiscId",db.Integer,db.ForeignKey("tbl_dk_res_discount.ResDiscId"))
	SaleCardStatusId = db.Column("SaleCardStatusId",db.Integer,db.ForeignKey("tbl_dk_sale_card_status.SaleCardStatusId"))
	SaleCardRegNo = db.Column("SaleCardRegNo",db.String(100),nullable=False)
	SaleCardName = db.Column("SaleCardName",db.String(100),nullable=False)
	SaleCardDesc = db.Column("SaleCardDesc",db.String(500))
	SaleCardStartDate = db.Column("SaleCardStartDate",db.DateTime,default=datetime.now)
	SaleCardEndDate = db.Column("SaleCardEndDate",db.DateTime,default=datetime.now)
	SaleCardMinSaleAmount = db.Column("SaleCardMinSaleAmount",db.Float,default=0.0)
	SaleCardMaxSaleAmount = db.Column("SaleCardMaxSaleAmount",db.Float,default=0.0)
	SaleCardMinSalePrice = db.Column("SaleCardMinSalePrice",db.Float,default=0.0)
	SaleCardMaxSalePrice = db.Column("SaleCardMaxSalePrice",db.Float,default=0.0)
	SaleCardMaxManualDiscPerc = db.Column("SaleCardMaxManualDiscPerc",db.Float,default=0.0)
	SaleCardIsPayable = db.Column("SaleCardIsPayable",db.Boolean,default=True)
	SaleCardCustName = db.Column("SaleCardCustName",db.String(100))
	SaleCardCustBirthDate = db.Column("SaleCardCustBirthDate",db.String(100))
	SaleCardCustTel = db.Column("SaleCardCustTel",db.String(100))
	SaleCardCustEmail = db.Column("SaleCardCustEmail",db.String(100))
	SaleCardCustAddress = db.Column("SaleCardCustAddress",db.String(100))
	Res_discount = db.relationship("Res_discount",backref='sale_card',foreign_keys='Res_discount.SaleCardId',lazy=True)

	def to_json_api(self):
		data = {
			"SaleCardId": self.SaleCardId,
			"SaleCardGuid": self.SaleCardGuid,
			"CId": self.CId,
			"DivId": self.DivId,
			"WpId": self.WpId,
			"RpAccId": self.RpAccId,
			"CurrencyId": self.CurrencyId,
			"SaleAgrId": self.SaleAgrId,
			"ResPriceGroupId": self.ResPriceGroupId,
			"ResDiscId": self.ResDiscId,
			"SaleCardStatusId": self.SaleCardStatusId,
			"SaleCardRegNo": self.SaleCardRegNo,
			"SaleCardName": self.SaleCardName,
			"SaleCardDesc": self.SaleCardDesc,
			"SaleCardStartDate": self.SaleCardStartDate,
			"SaleCardEndDate": self.SaleCardEndDate,
			"SaleCardMinSaleAmount": self.SaleCardMinSaleAmount,
			"SaleCardMaxSaleAmount": self.SaleCardMaxSaleAmount,
			"SaleCardMinSalePrice": self.SaleCardMinSalePrice,
			"SaleCardMaxSalePrice": self.SaleCardMaxSalePrice,
			"SaleCardMaxManualDiscPerc": self.SaleCardMaxManualDiscPerc,
			"SaleCardIsPayable": self.SaleCardIsPayable,
			"SaleCardCustName": self.SaleCardCustName,
			"SaleCardCustBirthDate": self.SaleCardCustBirthDate,
			"SaleCardCustTel": self.SaleCardCustTel,
			"SaleCardCustEmail": self.SaleCardCustEmail,
			"SaleCardCustAddress": self.SaleCardCustAddress
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data