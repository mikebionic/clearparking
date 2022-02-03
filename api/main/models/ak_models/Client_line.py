# CREATE TABLE doner_test.dbo.tbl_mg_clientlines (
# 	cl_id int IDENTITY(1,1) NOT NULL,
# 	cl_datetime datetime DEFAULT getdate() NULL,
# 	cl_total decimal(18,5) NULL,
# 	cl_type int NULL,
# 	cl_trans_name nvarchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
# 	inv_id int NULL,
# 	bank_fich_head_id int NULL,
# 	arap_id int NULL,
# 	ks_line_id int NULL,
# 	cl_credit decimal(18,5) NULL,
# 	arap_id_acc_card_id int NULL,
# 	op_bl_l_id int NULL,
# 	inv_real_code nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
# 	spe_code nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
# 	group_code nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
# 	security_code nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
# 	cl_desc nvarchar(200) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
# 	p_id int NULL,
# 	rep_rate decimal(18,5) DEFAULT 0 NULL,
# 	rep_debit decimal(18,5) DEFAULT 0 NULL,
# 	rep_credit decimal(18,5) DEFAULT 0 NULL,
# 	cl_id_guid nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS DEFAULT newid() NULL,
# 	CONSTRAINT PK_tbl_mg_clientlines PRIMARY KEY (cl_id)
# );

from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from main import db

class Client_line_akhasap(db.Model):
	__tablename__ = "tbl_mg_clientlines"
	__table_args__ = {'implicit_returning': False}
	cl_id = db.Column("cl_id",db.Integer,nullable=False,primary_key=True)
	cl_datetime = db.Column("cl_datetime",db.DateTime,default=datetime.now())
	cl_total = db.Column("cl_total",db.Float)
	cl_type = db.Column("cl_type",db.Integer)
	cl_trans_name = db.Column("cl_trans_name",db.String)
	inv_id = db.Column("inv_id",db.Integer)
	bank_fich_head_id = db.Column("bank_fich_head_id",db.Integer)
	arap_id = db.Column("arap_id",db.Integer)
	ks_line_id = db.Column("ks_line_id",db.Integer)
	cl_credit = db.Column("cl_credit",db.Float)
	arap_id_acc_card_id = db.Column("arap_id_acc_card_id",db.Integer)
	op_bl_l_id = db.Column("op_bl_l_id",db.Integer)
	inv_real_code = db.Column("inv_real_code",db.String)
	spe_code = db.Column("spe_code",db.String)
	group_code = db.Column("group_code",db.String)
	security_code = db.Column("security_code",db.String)
	cl_desc = db.Column("cl_desc",db.String)
	p_id = db.Column("p_id",db.Integer)
	rep_rate = db.Column("rep_rate",db.Float)
	rep_debit = db.Column("rep_debit",db.Float)
	rep_credit = db.Column("rep_credit",db.Float)
	cl_id_guid = db.Column("cl_id_guid",UUID(as_uuid=True),unique=True)

	def to_json_api(self):
		data = {
			"cl_id": self.cl_id,
			"cl_datetime": self.cl_datetime,
			"cl_total": self.cl_total,
			"cl_type": self.cl_type,
			"cl_trans_name": self.cl_trans_name,
			"inv_id": self.inv_id,
			"bank_fich_head_id": self.bank_fich_head_id,
			"arap_id": self.arap_id,
			"ks_line_id": self.ks_line_id,
			"cl_credit": self.cl_credit,
			"arap_id_acc_card_id": self.arap_id_acc_card_id,
			"op_bl_l_id": self.op_bl_l_id,
			"inv_real_code": self.inv_real_code,
			"spe_code": self.spe_code,
			"group_code": self.group_code,
			"security_code": self.security_code,
			"cl_desc": self.cl_desc,
			"p_id": self.p_id,
			"rep_rate": self.rep_rate,
			"rep_debit": self.rep_debit,
			"rep_credit": self.rep_credit,
			"cl_id_guid": self.cl_id_guid,
		}

		return data
