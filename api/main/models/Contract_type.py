from sqlalchemy.dialects.postgresql import UUID

from main import db
from main.models import BaseModel


class Contract_type(BaseModel, db.Model):
	__tablename__ = "tbl_dk_contract_type"
	ContractTypeId = db.Column("ContractTypeId",db.Integer,nullable=False,primary_key=True)
	ContractTypeGuid = db.Column("ContractTypeGuid",UUID(as_uuid=True),unique=True)
	ContractTypeName_tkTM = db.Column("ContractTypeName_tkTM",db.String(100))
	ContractTypeDesc_tkTM = db.Column("ContractTypeDesc_tkTM",db.String(100))
	ContractTypeName_ruRU = db.Column("ContractTypeName_ruRU",db.String(100))
	ContractTypeDesc_ruRU = db.Column("ContractTypeDesc_ruRU",db.String(100))
	ContractTypeName_enUS = db.Column("ContractTypeName_enUS",db.String(100))
	ContractTypeDesc_enUS = db.Column("ContractTypeDesc_enUS",db.String(100))
	Employee = db.relationship("Employee",backref='contract_type',lazy=True)
	Contract = db.relationship("Contract",backref='contract_type',lazy=True)

	def to_json_api(self):
		data = {
			"ContractTypeId": self.ContractTypeId,
			"ContractTypeGuid": self.ContractTypeGuid,
			"ContractTypeName_tkTM": self.ContractTypeName_tkTM,
			"ContractTypeDesc_tkTM": self.ContractTypeDesc_tkTM,
			"ContractTypeName_ruRU": self.ContractTypeName_ruRU,
			"ContractTypeDesc_ruRU": self.ContractTypeDesc_ruRU,
			"ContractTypeName_enUS": self.ContractTypeName_enUS,
			"ContractTypeDesc_enUS": self.ContractTypeDesc_enUS
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data