from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from main import db
from main.models import AddInf, BaseModel
from main.base.dataMethods import apiDataFormat


class Contract(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_contract"
	ContractId = db.Column("ContractId",db.Integer,nullable=False,primary_key=True)
	ContractTypeId = db.Column("ContractTypeId",db.Integer,db.ForeignKey("tbl_dk_contract_type.ContractTypeId"))
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	ContractGuid = db.Column("ContractGuid",UUID(as_uuid=True),unique=True)
	ContractRegNo = db.Column("ContractRegNo",db.String(100),nullable=False,unique=True)
	ContractName = db.Column("ContractName",db.String(500))
	ContractDesc = db.Column("ContractDesc",db.String)
	ContractDate = db.Column("ContractDate",db.DateTime,default=datetime.now)
	ContractEndDate = db.Column("ContractEndDate",db.DateTime)
	ContractCondition = db.Column("ContractCondition",db.String(500))
	ContractBody = db.Column("ContractBody",db.String(500))

	def to_json_api(self):
		data = {
			"ContractId": self.ContractId,
			"ContractTypeId": self.ContractTypeId,
			"CId": self.CId,
			"DivId": self.DivId,
			"EmpId": self.EmpId,
			"RpAccId": self.RpAccId,
			"ContractGuid": self.ContractGuid,
			"ContractRegNo": self.ContractRegNo,
			"ContractName": self.ContractName,
			"ContractDesc": self.ContractDesc,
			"ContractDate": apiDataFormat(self.ContractDate),
			"ContractEndDate": apiDataFormat(self.ContractEndDate),
			"ContractCondition": self.ContractCondition,
			"ContractBody": self.ContractBody
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data