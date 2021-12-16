from main.config import Config

if Config.DB_STRUCTURE == 'saphasap':
	from .sap_models import *

elif Config.DB_STRUCTURE == 'akhasap':
	from .ak_models import *