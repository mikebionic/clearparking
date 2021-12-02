from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Production(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_production"
	ProdId = db.Column("ProdId",db.Integer,nullable=False,primary_key=True)
	ProdGuid = db.Column("ProdGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	WhIdIn = db.Column("WhIdIn",db.Integer,db.ForeignKey("tbl_dk_warehouse.WhId"))
	WhIdOut = db.Column("WhIdOut",db.Integer,db.ForeignKey("tbl_dk_warehouse.WhId"))
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	ProdName = db.Column("ProdName",db.String(100),nullable=False)
	ProdDesc = db.Column("ProdDesc",db.String(500),default='')
	ProdTime = db.Column("ProdTime",db.Float)
	ProdCostPrice = db.Column("ProdCostPrice",db.Float)
	Production_line = db.relationship("Production_line",backref='production',lazy=True)
	Image = db.relationship("Image",backref='production',lazy=True)
	Translation = db.relationship("Translation",backref='production',lazy=True)

	def to_json_api(self):
		data = {
			"ProdId": self.ProdId,
			"ProdGuid": self.ProdGuid,
			"CId": self.CId,
			"DivId": self.DivId,
			"WhIdIn": self.WhIdIn,
			"WhIdOut": self.WhIdOut,
			"ResId": self.ResId,
			"ProdName": self.ProdName,
			"ProdDesc": self.ProdDesc,
			"ProdTime": self.ProdTime,
			"ProdCostPrice": self.ProdCostPrice
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data