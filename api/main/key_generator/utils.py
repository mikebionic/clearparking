from main.config import Config
from main import db
from main.models import Reg_num, Reg_num_type, Pred_reg_num
import uuid

from random import randint

RegNumTypeNamesDict = {
	"employee_code": 1,
	"user_code": 2,
	"goods_code": 3,
	"account_code": 4,
	"price_code": 5,
	"rp_code": 6,
	"sale_invoice_code": 7,
	"purchase_invoice_code": 8,
	"sale_order_invoice_code": 9,
	"purchase_order_invoice_code": 10,
	"sale_return_invoice_code": 11,
	"purchase_return_invoice_code": 12,
	"order_invoice_line_code": 13,
	"invoice_line_code": 14
}

def generate(UId, RegNumTypeName=None, RegNumTypeId=None):
	if not RegNumTypeId:
		RegNumTypeId = RegNumTypeNamesDict[RegNumTypeName]

	reg_num = Reg_num.query\
		.filter_by(UId = UId, RegNumTypeId = RegNumTypeId)\
		.first()
	if not reg_num:
		regNumType = Reg_num_type.query.filter_by(RegNumTypeId = RegNumTypeId).first()
		RegNumPrefix = makeShortType(regNumType.RegNumTypeName_tkTM)
		reg_num = Reg_num(
			UId = UId,
			RegNumTypeId = regNumType.RegNumTypeId,
			RegNumPrefix = RegNumPrefix,
			RegNumLastNum = 0,
			RegNumGuid = uuid.uuid4()
		)
		db.session.add(reg_num)
		db.session.commit()
	response = reg_num

	return response

def validate(
	UId,
	RegNumLastNum,
	dbModel,
	RegNumTypeName = None,
	RegNumTypeId = None
):
	try:
		if not RegNumTypeId:
			RegNumTypeId = RegNumTypeNamesDict[RegNumTypeName]
		reg_num = Reg_num.query\
			.filter_by(UId = UId, RegNumTypeId = RegNumTypeId)\
			.first()
		if not dbModel and (RegNumLastNum > reg_num.RegNumLastNum):
			response = {
				"status": True,
				"RegNumLastNum": RegNumLastNum
			}
		else:
			while (RegNumLastNum <= reg_num.RegNumLastNum):
				RegNumLastNum += 1

			response = {
				"status": False,
				"RegNumLastNum": RegNumLastNum
			}
	except Exception as ex:
		print(f"Reg Num validation exception: {ex}")
		response = {
			"status": "error",
			"responseText": "Wrong prefix type or missing in database"
		}
	return response

def makeRegNo(
	shortName,
	prefix,
	lastNum,
	suffix = '',
	random_mode = False,
	RegNumTypeId = None,
	RegNumTypeName = None
):
	if not RegNumTypeId:
		RegNumTypeId = RegNumTypeNamesDict[RegNumTypeName]

	if random_mode:
		lastNum = randint(1,Config.REG_NUM_RANDOM_RANGE)

	while True:
		regNo = f"{shortName.upper()}{prefix}{str(lastNum)}{suffix}"
		existingObj = checkPredExistence(RegNum=regNo,RegNumTypeId=RegNumTypeId)
		if not existingObj:
			break
		lastNum += 1
	return regNo

def checkPredExistence(RegNum,RegNumTypeId=None):
	filtering = {
		"RegNum": RegNum,
	}
	if RegNumTypeId:
		filtering["RegNumTypeId"] = RegNumTypeId
	registeredRegNo = Pred_reg_num.query\
		.filter_by(**filtering)\
		.first()
	return registeredRegNo
	
# returnes first leters of typeName
def makeShortType(text):
	words = text.split()
	short = [word[0] for word in words]
	short = (''.join(short)).upper()
	return short

# returnes first and last letter of UName
def makeShortName(name):
	short = (name[0]+name[-1]).upper()
	return short