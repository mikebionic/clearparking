from main import db

class Resource(db.Model):
	__tablename__ = "tbl_mg_materials"
	ResId = db.Column("material_id",db.Integer,nullable=False,primary_key=True)
	ResName = db.Column("material_name",db.String)
	ResDesc = db.Column("spe_code2",db.String)
	# Barcode = db.relationship("Barcode",backref='resource',lazy=True)
	# Res_price = db.relationship("Res_price",backref='resource',lazy=True)

	def to_json_api(self):
		data = {
			"ResId": self.ResId,
			"ResName": self.ResName,
			"ResDesc": self.ResDesc
		}


		return data