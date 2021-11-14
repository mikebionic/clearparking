from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.base.dataMethods import configureFloat
from main.models import AddInf, BaseModel


class Resource(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_resource"
	ResId = db.Column("ResId",db.Integer,nullable=False,primary_key=True)
	ResGuid = db.Column("ResGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	# ResCatId = db.Column("ResCatId",db.Integer,db.ForeignKey("tbl_dk_res_category.ResCatId"))
	# UnitId = db.Column("UnitId",db.Integer,db.ForeignKey("tbl_dk_unit.UnitId"))
	# BrandId = db.Column("BrandId",db.Integer,db.ForeignKey("tbl_dk_brand.BrandId"))
	# UsageStatusId = db.Column("UsageStatusId",db.Integer,db.ForeignKey("tbl_dk_usage_status.UsageStatusId"))
	# ResTypeId = db.Column("ResTypeId",db.Integer,db.ForeignKey("tbl_dk_res_type.ResTypeId"))
	# ResMainImgId = db.Column("ResMainImgId",db.Integer,default=0)
	# ResMakerId = db.Column("ResMakerId",db.Integer,db.ForeignKey("tbl_dk_res_maker.ResMakerId"))
	ResLastVendorId = db.Column("ResLastVendorId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	ResRegNo = db.Column("ResRegNo",db.String(50),nullable=False,unique=True)
	ResName = db.Column("ResName",db.String(255),nullable=False)
	ResDesc = db.Column("ResDesc",db.String(1000))
	ResFullDesc = db.Column("ResFullDesc",db.String(50000))
	IsMain = db.Column("IsMain",db.Integer)
	ResVisibleIndex = db.Column("ResVisibleIndex",db.Integer)
	ResViewCnt = db.Column("ResViewCnt",db.Integer)
	ResWidth = db.Column("ResWidth",db.Float,default=0.0)
	ResHeight = db.Column("ResHeight",db.Float,default=0.0)
	ResLength = db.Column("ResLength",db.Float,default=0.0)
	ResWeight = db.Column("ResWeight",db.Float,default=0.0)
	ResProductionOnSale = db.Column("ResProductionOnSale",db.Boolean,default=False)
	ResMinSaleAmount = db.Column("ResMinSaleAmount",db.Float,default=0.0)
	ResMaxSaleAmount = db.Column("ResMaxSaleAmount",db.Float,default=0.0)
	ResMinSalePrice = db.Column("ResMinSalePrice",db.Float,default=0.0)
	ResMaxSalePrice = db.Column("ResMaxSalePrice",db.Float,default=0.0)
	Inv_line = db.relationship("Inv_line",backref='resource',lazy=True)
	Inv_line_det = db.relationship("Inv_line_det",backref='resource',lazy=True)	
	Res_price = db.relationship("Res_price",backref='resource',lazy=True)
	Res_total = db.relationship("Res_total",backref='resource',lazy=True)

	def to_json_api(self):
		data = {
			"ResId": self.ResId,
			"ResGuid": self.ResGuid,
			"CId": self.CId,
			"DivId": self.DivId,
			# "ResCatId": self.ResCatId,
			# "UnitId": self.UnitId,
			# "BrandId": self.BrandId,
			# "UsageStatusId": self.UsageStatusId,
			# "ResTypeId": self.ResTypeId,
			# "ResMainImgId": self.ResMainImgId,
			# "ResMakerId": self.ResMakerId,
			"ResLastVendorId": self.ResLastVendorId,
			"ResRegNo": self.ResRegNo,
			"ResName": self.ResName,
			"ResDesc": self.ResDesc,
			"ResFullDesc": self.ResFullDesc,
			"IsMain": self.IsMain,
			"ResVisibleIndex": self.ResVisibleIndex,
			"ResViewCnt": self.ResViewCnt,
			"ResWidth": configureFloat(self.ResWidth),
			"ResHeight": configureFloat(self.ResHeight),
			"ResLength": configureFloat(self.ResLength),
			"ResWeight": configureFloat(self.ResWeight),
			"ResProductionOnSale": self.ResProductionOnSale,
			"ResMinSaleAmount": configureFloat(self.ResMinSaleAmount),
			"ResMaxSaleAmount": configureFloat(self.ResMaxSaleAmount),
			"ResMinSalePrice": configureFloat(self.ResMinSalePrice),
			"ResMaxSalePrice": configureFloat(self.ResMaxSalePrice),
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data