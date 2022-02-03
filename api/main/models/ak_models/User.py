from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from main import db
from main.config import Config


class User_akhasap(db.Model, UserMixin):
	__tablename__ = "Teachers"
	UId = db.Column("T_ID",db.Integer,nullable=False,primary_key=True)
	UGuid = db.Column("UGuid",UUID(as_uuid=True),unique=True)
	RpAccId = db.Column("arap_id",db.Integer)
	UFullName = db.Column("TName",db.String(100))
	UName = db.Column("T_User_Name",db.String(60),nullable=False)
	UPass = db.Column("T_User_Pass",db.String(60),nullable=False)
	UTypeId = db.Column("User_Type_ID",db.Integer,db.ForeignKey("tbl_dk_user_type.UTypeId"))

	def is_admin(self):
		return self.UTypeId == 1

	def get_id(self):
		return (self.UId)

	def get_reset_token(self,expires_sec=1800):
		s = Serializer(Config.SECRET_KEY,expires_sec)
		return s.dumps({"UId": self.UId}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(Config.SECRET_KEY)
		try:
			UId = s.loads(token)['UId']
		except Exception:
			return None
		return User.query.get(UId)

	def to_json_api(self):
		data = {
			"UId": self.UId,
			"UGuid": self.UGuid,
			"RpAccId": self.RpAccId,
			"UFullName": self.UFullName,
			"UName": self.UName,
			"UPass": self.UPass,
			"UTypeId": self.UTypeId,
		}

		return data