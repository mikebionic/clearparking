from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Reg_num_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_reg_num_type"
	RegNumTypeId = db.Column("RegNumTypeId",db.Integer,nullable=False,primary_key=True)
	RegNumTypeGuid = db.Column("RegNumTypeGuid",UUID(as_uuid=True),unique=True)
	RegNumTypeName_tkTM = db.Column("RegNumTypeName_tkTM",db.String(50),nullable=False)
	RegNumTypeDesc_tkTM = db.Column("RegNumTypeDesc_tkTM",db.String(500))
	RegNumTypeName_ruRU = db.Column("RegNumTypeName_ruRU",db.String(50),nullable=False)
	RegNumTypeDesc_ruRU = db.Column("RegNumTypeDesc_ruRU",db.String(500))
	RegNumTypeName_enUS = db.Column("RegNumTypeName_enUS",db.String(50),nullable=False)
	RegNumTypeDesc_enUS = db.Column("RegNumTypeDesc_enUS",db.String(500))
	Reg_num = db.relationship("Reg_num",backref='reg_num_type',lazy=True)
	Pred_reg_num = db.relationship("Pred_reg_num",backref='reg_num_type',lazy=True)

	def to_json_api(self):
		data = {
			"RegNumTypeId": self.RegNumTypeId,
			"RegNumTypeGuid": self.RegNumTypeGuid,
			"RegNumTypeName_tkTM": self.RegNumTypeName_tkTM,
			"RegNumTypeDesc_tkTM": self.RegNumTypeDesc_tkTM,
			"RegNumTypeName_ruRU": self.RegNumTypeName_ruRU,
			"RegNumTypeDesc_ruRU": self.RegNumTypeDesc_ruRU,
			"RegNumTypeName_enUS": self.RegNumTypeName_enUS,
			"RegNumTypeDesc_enUS": self.RegNumTypeDesc_enUS,
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data