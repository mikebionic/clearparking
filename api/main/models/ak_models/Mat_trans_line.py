# CREATE TABLE doner_test.dbo.tbl_mg_mat_trans_line (
# 	mat_trans_line_id int IDENTITY(1,1) NOT NULL,
# 	mat_trans_line_date datetime DEFAULT getdate() NULL,
# 	material_id int NULL,
# 	fich_line_id int NULL,
# 	mat_inv_line_id int NULL,
# 	arap_id int NULL,
# 	mat_trans_type_id int NULL,
# 	mat_trans_type_code nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
# 	mat_trans_line_amount_out decimal(18,5) NULL,
# 	mat_trans_line_price_out decimal(18,5) NULL,
# 	mat_trans_line_totalprice decimal(18,5) NULL,
# 	mat_trans_line_nettotal decimal(18,5) NULL,
# 	mat_trans_line_amount_in decimal(18,5) NULL,
# 	mat_trans_line_price_in decimal(18,5) NULL,
# 	mat_trans_line_totalprice_in decimal(18,5) NULL,
# 	mat_trans_line_nettotal_in decimal(18,5) NULL,
# 	mat_trans_line_wh_id_out int NULL,
# 	mat_trans_line_wh_id_in int NULL,
# 	mat_trans_line_wh_amount decimal(18,5) NULL,
# 	p_id int NULL,
# 	fich_type_id int NULL,
# 	mat_inv_type_id int NULL,
# 	mat_trans_line_cdate datetime DEFAULT getdate() NULL,
# 	unit_det_id int DEFAULT 0 NULL,
# 	mat_trans_line_wh_id_amount float DEFAULT 0 NULL,
# 	inv_real_code nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
# 	fich_line_expiredate datetime DEFAULT '1.1.1900' NULL,
# 	mat_trans_line_id_out int DEFAULT 0 NULL,
# 	mat_trans_line_amount_in_onhand decimal(18,5) DEFAULT 0 NULL,
# 	mat_trans_line_outcost decimal(18,5) DEFAULT 0 NULL,
# 	mat_trans_line_retcost decimal(18,5) DEFAULT 0 NULL,
# 	mat_trans_line_out_remain_amount decimal(18,5) DEFAULT 0 NULL,
# 	mat_trans_line_id_guid nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS DEFAULT newid() NULL,
# 	rep_rate decimal(18,5) DEFAULT 0 NULL,
# 	rep_currency_id int DEFAULT 0 NULL,
# 	CONSTRAINT PK_tbl_mg_mat_trans_line PRIMARY KEY (mat_trans_line_id)
# );


from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from main import db

class Mat_trans_line(db.Model):
	__tablename__ = "tbl_mg_mat_trans_line"
	__table_args__ = {'implicit_returning': False}
	mat_trans_line_id = db.Column("mat_trans_line_id",db.Integer,nullable=False,primary_key=True)
	mat_trans_line_date = db.Column("mat_trans_line_date",db.DateTime,default=datetime.now())
	material_id = db.Column("material_id",db.Integer)
	fich_line_id = db.Column("fich_line_id",db.Integer)
	mat_inv_line_id = db.Column("mat_inv_line_id",db.Integer)
	arap_id = db.Column("arap_id",db.Integer)
	mat_trans_type_id = db.Column("mat_trans_type_id",db.Integer)
	mat_trans_type_code = db.Column("mat_trans_type_code",db.String)
	mat_trans_line_amount_out = db.Column("mat_trans_line_amount_out",db.Float)
	mat_trans_line_price_out = db.Column("mat_trans_line_price_out",db.Float)
	mat_trans_line_totalprice = db.Column("mat_trans_line_totalprice",db.Float)
	mat_trans_line_nettotal = db.Column("mat_trans_line_nettotal",db.Float)
	mat_trans_line_amount_in = db.Column("mat_trans_line_amount_in",db.Float)
	mat_trans_line_price_in = db.Column("mat_trans_line_price_in",db.Float)
	mat_trans_line_totalprice_in = db.Column("mat_trans_line_totalprice_in",db.Float)
	mat_trans_line_nettotal_in = db.Column("mat_trans_line_nettotal_in",db.Float)
	mat_trans_line_wh_id_out = db.Column("mat_trans_line_wh_id_out",db.Integer)
	mat_trans_line_wh_id_in = db.Column("mat_trans_line_wh_id_in",db.Integer)
	mat_trans_line_wh_amount = db.Column("mat_trans_line_wh_amount",db.Float)
	p_id = db.Column("p_id",db.Integer)
	fich_type_id = db.Column("fich_type_id",db.Integer)
	mat_inv_type_id = db.Column("mat_inv_type_id",db.Integer)
	mat_trans_line_cdate = db.Column("mat_trans_line_cdate",db.DateTime,default=datetime.now())
	unit_det_id = db.Column("unit_det_id",db.Integer)
	mat_trans_line_wh_id_amount = db.Column("mat_trans_line_wh_id_amount",db.Integer)
	inv_real_code = db.Column("inv_real_code",db.String)
	fich_line_expiredate = db.Column("fich_line_expiredate",db.DateTime)
	mat_trans_line_id_out = db.Column("mat_trans_line_id_out",db.Integer)
	mat_trans_line_amount_in_onhand = db.Column("mat_trans_line_amount_in_onhand",db.Float)
	mat_trans_line_outcost = db.Column("mat_trans_line_outcost",db.Float)
	mat_trans_line_retcost = db.Column("mat_trans_line_retcost",db.Float)
	mat_trans_line_out_remain_amount = db.Column("mat_trans_line_out_remain_amount",db.Float)
	mat_trans_line_id_guid = db.Column("mat_trans_line_id_guid",UUID(as_uuid=True),unique=True)
	rep_rate = db.Column("rep_rate",db.Float)
	rep_currency_id = db.Column("rep_currency_id",db.Integer)

	def to_json_api(self):
		data = {
			"mat_trans_line_id": self.mat_trans_line_id,
			"mat_trans_line_date": self.mat_trans_line_date,
			"material_id": self.material_id,
			"fich_line_id": self.fich_line_id,
			"mat_inv_line_id": self.mat_inv_line_id,
			"arap_id": self.arap_id,
			"mat_trans_type_id": self.mat_trans_type_id,
			"mat_trans_type_code": self.mat_trans_type_code,
			"mat_trans_line_amount_out": self.mat_trans_line_amount_out,
			"mat_trans_line_price_out": self.mat_trans_line_price_out,
			"mat_trans_line_totalprice": self.mat_trans_line_totalprice,
			"mat_trans_line_nettotal": self.mat_trans_line_nettotal,
			"mat_trans_line_amount_in": self.mat_trans_line_amount_in,
			"mat_trans_line_price_in": self.mat_trans_line_price_in,
			"mat_trans_line_totalprice_in": self.mat_trans_line_totalprice_in,
			"mat_trans_line_nettotal_in": self.mat_trans_line_nettotal_in,
			"mat_trans_line_wh_id_out": self.mat_trans_line_wh_id_out,
			"mat_trans_line_wh_id_in": self.mat_trans_line_wh_id_in,
			"mat_trans_line_wh_amount": self.mat_trans_line_wh_amount,
			"p_id": self.p_id,
			"fich_type_id": self.fich_type_id,
			"mat_inv_type_id": self.mat_inv_type_id,
			"mat_trans_line_cdate": self.mat_trans_line_cdate,
			"unit_det_id": self.unit_det_id,
			"mat_trans_line_wh_id_amount": self.mat_trans_line_wh_id_amount,
			"inv_real_code": self.inv_real_code,
			"fich_line_expiredate": self.fich_line_expiredate,
			"mat_trans_line_id_out": self.mat_trans_line_id_out,
			"mat_trans_line_amount_in_onhand": self.mat_trans_line_amount_in_onhand,
			"mat_trans_line_outcost": self.mat_trans_line_outcost,
			"mat_trans_line_retcost": self.mat_trans_line_retcost,
			"mat_trans_line_out_remain_amount": self.mat_trans_line_out_remain_amount,
			"mat_trans_line_id_guid": self.mat_trans_line_id_guid,
			"rep_rate": self.rep_rate,
			"rep_currency_id": self.rep_currency_id,
		}

		return data
