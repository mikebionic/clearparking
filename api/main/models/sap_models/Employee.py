from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import AddInf, BaseModel


class Employee(AddInf, BaseModel, db.Model):
	__tablename__ = "tbl_dk_employee"
	EmpId = db.Column("EmpId",db.Integer,nullable=False,primary_key=True)
	EmpGuid = db.Column("EmpGuid",UUID(as_uuid=True),unique=True)
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	DivId = db.Column("DivId",db.Integer,db.ForeignKey("tbl_dk_division.DivId"))
	ContractTypeId = db.Column("ContractTypeId",db.Integer,db.ForeignKey("tbl_dk_contract_type.ContractTypeId"))
	DeptId = db.Column("DeptId",db.Integer,db.ForeignKey("tbl_dk_department.DeptId"))
	ProfessionId = db.Column("ProfessionId",db.Integer,db.ForeignKey("tbl_dk_profession.ProfessionId"))
	EmpStatId = db.Column("EmpStatId",db.Integer,db.ForeignKey("tbl_dk_emp_status.EmpStatId"))
	EmpRegNo = db.Column("EmpRegNo",db.String(128),nullable=False)
	EmpName = db.Column("EmpName",db.String(255),nullable=False)
	EmpLastName = db.Column("EmpLastName",db.String(50))
	EmpFirstName = db.Column("EmpFirstName",db.String(50))
	EmpPatronymic = db.Column("EmpPatronymic",db.String(50))
	GenderId = db.Column("GenderId",db.Integer,db.ForeignKey("tbl_dk_gender.GenderId"))
	EmpBirthDate = db.Column("EmpBirthDate",db.DateTime(50))
	EmpBirthPlace = db.Column("EmpBirthPlace",db.String(500))
	EmpResidency = db.Column("EmpResidency",db.String(500))
	NatId = db.Column("NatId",db.Integer,db.ForeignKey("tbl_dk_nationality.NatId"))
	EmpPassportNo = db.Column("EmpPassportNo",db.String(30))
	EmpPaspIssuePlace = db.Column("EmpPaspIssuePlace",db.String(255))
	EduLevelId = db.Column("EduLevelId",db.Integer,db.ForeignKey("tbl_dk_edu_level.EduLevelId"))
	EmpLangSkills = db.Column("EmpLangSkills",db.String(500))
	MobilePhoneNumber = db.Column("MobilePhoneNumber",db.String(100))
	HomePhoneNumber = db.Column("HomePhoneNumber",db.String(100))
	WorkPhoneNumber = db.Column("WorkPhoneNumber",db.String(100))
	WorkFaxNumber = db.Column("WorkFaxNumber",db.String(100))
	ZipCode = db.Column("ZipCode",db.String(100))
	EMail = db.Column("EMail",db.String(100))
	Contact = db.relationship("Contact",backref='employee',lazy=True)
	Location = db.relationship("Location",backref='employee',lazy=True)
	Award = db.relationship("Award",backref='employee',lazy=True)
	Relatives = db.relationship("Relatives",backref='employee',lazy=True)
	School = db.relationship("School",backref='employee',lazy=True)
	Visited_country = db.relationship("Visited_country",backref='employee',lazy=True)
	Work_history = db.relationship("Work_history",backref='employee',lazy=True)
	Department_detail = db.relationship("Department_detail",backref='employee',lazy=True)
	Image = db.relationship("Image",backref='employee',lazy=True)
	Rp_acc = db.relationship("Rp_acc",backref='employee',lazy=True)
	Invoice = db.relationship("Invoice",backref='employee',lazy=True)
	Order_inv = db.relationship("Order_inv",backref='employee',lazy=True)
	Res_trans_inv = db.relationship("Res_trans_inv",backref='employee',lazy=True)
	Rating = db.relationship("Rating",backref='employee',lazy=True)
	Emp_recr_line = db.relationship("Emp_recr_line",backref='employee',lazy=True)
	Contract = db.relationship("Contract",backref='employee',lazy=True)

	def to_json_api(self):
		data = {
			"EmpId": self.EmpId,
			"EmpGuid": self.EmpGuid,
			"CId": self.CId,
			"ContractTypeId": self.ContractTypeId,
			"DeptId": self.DeptId,
			"ProfessionId": self.ProfessionId,
			"EmpStatId": self.EmpStatId,
			"EmpRegNo": self.EmpRegNo,
			"EmpName": self.EmpName,
			"EmpLastName": self.EmpLastName,
			"EmpFirstName": self.EmpFirstName,
			"EmpPatronymic": self.EmpPatronymic,
			"GenderId": self.GenderId,
			"EmpBirthDate": self.EmpBirthDate,
			"EmpBirthPlace": self.EmpBirthPlace,
			"EmpResidency": self.EmpResidency,
			"NatId": self.NatId,
			"EmpPassportNo": self.EmpPassportNo,
			"EmpPaspIssuePlace": self.EmpPaspIssuePlace,
			"EduLevelId": self.EduLevelId,
			"EmpLangSkills": self.EmpLangSkills,
			"MobilePhoneNumber": self.MobilePhoneNumber,
			"HomePhoneNumber": self.HomePhoneNumber,
			"WorkPhoneNumber": self.WorkPhoneNumber,
			"WorkFaxNumber": self.WorkFaxNumber,
			"ZipCode": self.ZipCode,
			"EMail": self.EMail
		}

		for key, value in AddInf.to_json_api(self).items():
			data[key] = value

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data