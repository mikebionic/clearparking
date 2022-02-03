from main import db

class Barcode_akhasap(db.Model):
	__tablename__ = "tbl_mg_barcode"
	BarcodeId = db.Column("bar_id",db.Integer,nullable=False,primary_key=True)
	ResId = db.Column("material_id",db.Integer)
	BarcodeVal = db.Column("bar_barcode",db.String(100),nullable=False)

	def to_json_api(self):
		data = {
			"BarcodeId": self.BarcodeId,
			"ResId": self.ResId,
			"BarcodeVal": self.BarcodeVal,
		}


		return data