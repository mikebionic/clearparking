from main import db
from main.models import BaseModel


class AdditionalInf1(BaseModel, db.Model):
	__tablename__ = "tbl_dk_additional_inf1"
	AddInf1Id = db.Column("AddInf1Id",db.Integer,nullable=False,primary_key=True)
	AddInf1Name = db.Column("AddInf1Name",db.String(100),nullable=False)
	AddInf1Desc = db.Column("AddInf1Desc",db.String(500))
	AddInfTypeId = db.Column("AddInfTypeId",db.Integer,default=0)


class AdditionalInf2(BaseModel, db.Model):
	__tablename__ = "tbl_dk_additional_inf2"
	AddInf2Id = db.Column("AddInf2Id",db.Integer,nullable=False,primary_key=True)
	AddInf2Name = db.Column("AddInf2Name",db.String(100),nullable=False)
	AddInf2Desc = db.Column("AddInf2Desc",db.String(500))
	AddInfTypeId = db.Column("AddInfTypeId",db.Integer,default=0)


class AdditionalInf3(BaseModel, db.Model):
	__tablename__ = "tbl_dk_additional_inf3"
	AddInf3Id = db.Column("AddInf3Id",db.Integer,nullable=False,primary_key=True)
	AddInf3Name = db.Column("AddInf3Name",db.String(100),nullable=False)
	AddInf3Desc = db.Column("AddInf3Desc",db.String(500))
	AddInfTypeId = db.Column("AddInfTypeId",db.Integer,default=0)


class AdditionalInf4(BaseModel, db.Model):
	__tablename__ = "tbl_dk_additional_inf4"
	AddInf4Id = db.Column("AddInf4Id",db.Integer,nullable=False,primary_key=True)
	AddInf4Name = db.Column("AddInf4Name",db.String(100),nullable=False)
	AddInf4Desc = db.Column("AddInf4Desc",db.String(500))
	AddInfTypeId = db.Column("AddInfTypeId",db.Integer,default=0)


class AdditionalInf5(BaseModel, db.Model):
	__tablename__ = "tbl_dk_additional_inf5"
	AddInf5Id = db.Column("AddInf5Id",db.Integer,nullable=False,primary_key=True)
	AddInf5Name = db.Column("AddInf5Name",db.String(100),nullable=False)
	AddInf5Desc = db.Column("AddInf5Desc",db.String(500))
	AddInfTypeId = db.Column("AddInfTypeId",db.Integer,default=0)


class AdditionalInf6(BaseModel, db.Model):
	__tablename__ = "tbl_dk_additional_inf6"
	AddInf6Id = db.Column("AddInf6Id",db.Integer,nullable=False,primary_key=True)
	AddInf6Name = db.Column("AddInf6Name",db.String(100),nullable=False)
	AddInf6Desc = db.Column("AddInf6Desc",db.String(500))
	AddInfTypeId = db.Column("AddInfTypeId",db.Integer,default=0)