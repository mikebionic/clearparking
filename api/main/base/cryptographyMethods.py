from cryptography.fernet import Fernet
import jwt
from datetime import datetime
import datetime as dt

from main.base.log_print import log_print
from main.config import Config


def encrypt_data(data, fernet_key, db_guid):
	try:
		if not data or not db_guid:
			print(f"cryptography encrypt exception: no data or guid: {str(data)}, {str(db_guid)}")
			raise Exception

		f = Fernet(fernet_key)
		enc = f.encrypt(str(data).encode()).decode()
		more = f"{str(db_guid)}{enc}{str(fernet_key)[::-1]}".encode()
		enc = f.encrypt(more)
		return enc.decode()

	except Exception:
		return None


def decrypt_data(data, fernet_key, db_guid):
	try:
		if not data or not db_guid:
			print(f"cryptography decrypt exception: no data or guid: {str(data)}, {str(db_guid)}")
			raise Exception

		f = Fernet(fernet_key)
		dec = f.decrypt(data.encode()).decode()
		dec.index(str(db_guid))
		dec = dec.replace(str(db_guid), '')
		dec.index(str(fernet_key)[::-1])
		dec = dec.replace(str(fernet_key)[::-1], '')
		dec = f.decrypt(str(dec).encode())
		return dec.decode()

	except Exception:
		return None

def encodeJWT(data):
	token = ''
	try:
		exp = datetime.now() + dt.timedelta(minutes = Config.TOKEN_EXP_TIME_MINUTES)
		exputc = datetime.utcnow() + dt.timedelta(minutes = Config.TOKEN_EXP_TIME_MINUTES)

		token_encoding_data = {
			"exp": exputc,
			"iat": datetime.utcnow(),
			"nbf": datetime.utcnow()
		}
		token_encoding_data.update(data)
		token = jwt.encode(token_encoding_data, Config.SECRET_KEY, algorithm=Config.JWT_ALGORITHM)

	except Exception as ex:
		log_print(f"JWT encoding exception {ex}","danger")

	return token, exp

def decodeJWT(token):
	token_data = ''
	try:
		token_data = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
	except Exception as ex:
		log_print(f"JWT decoding exception {ex}","danger")
	return token_data