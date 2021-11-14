from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import AddInf, BaseModel


class Production_line(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_production_line"
	ProdLineId = db.Column("ProdLineId",db.Integer,nullable=False,primary_key=True)
	ProdLineGuid = db.Column("ProdLineGuid",UUID(as_uuid=True),unique=True)
	ProdId = db.Column("ProdId",db.Integer,db.ForeignKey("tbl_dk_production.ProdId"))
	UnitId = db.Column("UnitId",db.Integer,db.ForeignKey("tbl_dk_unit.UnitId"))
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	ProdLineAmount = db.Column("ProdLineAmount",db.Float,nullable=False,default=0)
	ProdLinePrice = db.Column("ProdLinePrice",db.Float)
	ProdLineDesc = db.Column("ProdLineDesc",db.String(500),default='')

	def to_json_api(self):
		data = {
			"ProdLineId": self.ProdLineId,
			"ProdLineGuid": self.ProdLineGuid,
			"ProdId": self.ProdId,
			"UnitId": self.UnitId,
			"ResId": self.ResId,
			"ProdLineAmount": self.ProdLineAmount,
			"ProdLinePrice": self.ProdLinePrice,
			"ProdLineDesc": self.ProdLineDesc
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data