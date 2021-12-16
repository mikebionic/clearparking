from sqlalchemy.dialects.postgresql import UUID

from main import db
from . import BaseModel
from main.base.apiMethods import fileToURL


class Image(BaseModel, db.Model):
	__tablename__ = "tbl_dk_image"
	ImgId = db.Column("ImgId",db.Integer,nullable=False,primary_key=True)
	ImgGuid = db.Column("ImgGuid",UUID(as_uuid=True),unique=True)
	EmpId = db.Column("EmpId",db.Integer,db.ForeignKey("tbl_dk_employee.EmpId"))
	BrandId = db.Column("BrandId",db.Integer,db.ForeignKey("tbl_dk_brand.BrandId"))
	CId = db.Column("CId",db.Integer,db.ForeignKey("tbl_dk_company.CId"))
	UId = db.Column("UId",db.Integer,db.ForeignKey("tbl_dk_users.UId"))
	RpAccId = db.Column("RpAccId",db.Integer,db.ForeignKey("tbl_dk_rp_acc.RpAccId"))
	ResId = db.Column("ResId",db.Integer,db.ForeignKey("tbl_dk_resource.ResId"))
	ResCatId = db.Column("ResCatId",db.Integer,db.ForeignKey("tbl_dk_res_category.ResCatId"))
	ProdId = db.Column("ProdId",db.Integer,db.ForeignKey("tbl_dk_production.ProdId"))
	FileName = db.Column("FileName",db.String(100),default="")
	FilePath = db.Column("FilePath",db.String(255))
	FileHash = db.Column("FileHash",db.String(100))
	MinDarkFileName = db.Column("MinDarkFileName",db.String(100),default="")
	MinDarkFilePath = db.Column("MinDarkFilePath",db.String(255),default="")
	MaxDarkFileName = db.Column("MaxDarkFileName",db.String(100),default="")
	MaxDarkFilePath = db.Column("MaxDarkFilePath",db.String(255),default="")
	MinLightFileName = db.Column("MinLightFileName",db.String(100),default="")
	MinLightFilePath = db.Column("MinLightFilePath",db.String(255),default="")
	MaxLightFileName = db.Column("MaxLightFileName",db.String(100),default="")
	MaxLightFilePath = db.Column("MaxLightFilePath",db.String(255),default="")
	Image = db.Column("Image",db.LargeBinary)
	Tag = db.relationship("Tag",backref='image',lazy=True)

	def to_json_api(self):
		data = {
			"ImgId": self.ImgId,
			"ImgGuid": self.ImgGuid,
			"EmpId": self.EmpId,
			"BrandId": self.BrandId,
			"CId": self.CId,
			"UId": self.UId,
			"RpAccId": self.RpAccId,
			"ResId": self.ResId,
			"ResCatId": self.ResCatId,
			"ProdId": self.ProdId,
			"FileName": self.FileName,
			"FilePath": fileToURL(file_type='image',file_size='M',file_name=self.FileName),
			"FilePathS": fileToURL(file_type='image',file_size='S',file_name=self.FileName),
			"FilePathM": fileToURL(file_type='image',file_size='M',file_name=self.FileName),
			"FilePathR": fileToURL(file_type='image',file_size='R',file_name=self.FileName),
			"FileHash": self.FileHash,
			"MinDarkFileName": self.MinDarkFileName,			
			"MinDarkFilePath": self.MinDarkFilePath,
			"MaxDarkFileName": self.MaxDarkFileName,
			"MaxDarkFilePath": self.MaxDarkFilePath,
			"MinLightFileName": self.MinLightFileName,
			"MinLightFilePath": self.MinLightFilePath,
			"MaxLightFileName": self.MaxLightFileName,
			"MaxLightFilePath": self.MaxLightFilePath,
			# # "Image": base64.encodebytes(self.Image).decode('ascii'),
			# "Image": apiCheckImageByte(self.Image)
		}

		for key, value in BaseModel.to_json_api(self).items():
			data[key] = value

		return data