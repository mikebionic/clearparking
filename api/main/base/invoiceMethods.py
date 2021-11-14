from main.config import Config

#### balance and qty substitution function ####
def totalQtySubstitution(totalBalance,amount):
	resultingTotal = totalBalance - amount
	result = {
		"totalBalance": resultingTotal,
		"amount": amount,
		"status": 1
	}
	if resultingTotal > totalBalance:
		result = {
			"totalBalance": totalBalance,
			"amount": 0,
			"status": 0
		}
		return result
	if Config.NEGATIVE_WH_QTY_ORDER == False:
		if resultingTotal<0:
			result = {
				"totalBalance": 0,
				"amount": totalBalance,
				"status": 1
			}
		if totalBalance <= 0:
			result = {
				"totalBalance": totalBalance,
				"amount": 0,
				"status": 0
			}
	return result

# Res_total.ResTotBalance table required
# method is old and usage stopped
def resource_config_check(dbModel):
	if Config.SHOW_NEGATIVE_WH_QTY_RESOURCE == False:
		for res_total in dbModel.Res_total:
			if res_total.WhId == 1 and res_total.ResTotBalance > 0:
				return True
		return False
	else:
		return True

#### if errors in order invoice ####
def get_order_error_type(error_type):
	fail_statuses = {
		0: "Unknown error",
		1: "Deleted",
		2: "Usage satus: Inactive",
		3: "Resource ended",
		4: "False price"
	}
	# print(fail_statuses[error_type])
	return fail_statuses[error_type]

###### invoice status UI styling ######
invStatSelector = {
	# Waiting
	1:{
		"class": "warning",
		"color_hash": "#eda514", 
		"percentage": 10,
		"icon": "loader",
	},
	# Received (not order maybe, discuss with dovlet)
	2:{
		"class": "success",
		"color_hash": "#00b289", 
		"percentage": 30,
		"icon": "dollar-sign",
	},
	# Talked with a client
	3:{
		"class": "success",
		"color_hash": "#00b289", 
		"percentage": 30,
		"icon": "thumbs-up",
	},
	# Approved
	4:{
		"class": "success",
		"color_hash": "#00b289", 
		"percentage": 30,
		"icon": "check",
	},
	# Not approved
	5:{
		"class": "danger",
		"color_hash": "#FF7273", 
		"percentage": 30,
		"icon": "x-circle",
	},
	# Collecting goods
	6:{
		"class": "success",
		"color_hash": "#00b289", 
		"percentage": 40,
		"icon": "package",
	},
	# Order sent
	7:{
		"class": "info",
		"color_hash": "#63d3fa", 
		"percentage": 65,
		"icon": "truck",
	},
	# Transfered to customer
	8:{
		"class": "info",
		"color_hash": "#63d3fa", 
		"percentage": 88,
		"icon": "gift",
	},
	# Returned
	9:{
		"class": "danger",
		"color_hash": "#FF7273", 
		"percentage": 60,
		"icon": "corner-up-left",
	},
	# Note
	10:{
		"class": "warning",
		"color_hash": "#eda514", 
		"percentage": 50,
		"icon": "alert-octagon",
	},
	# Modified
	11:{
		"class": "warning",
		"color_hash": "#eda514", 
		"percentage": 60,
		"icon": "edit-2",
	},
	# Complete
	12:{
		"class": "primary",
		"color_hash": "#0023ff", 
		"percentage": 100,
		"icon": "award",
	},
	13:{
		"class": "warning",
		"color_hash": "#eda514", 
		"percentage": 20,
		"icon": "dollar-sign",
	},
	14:{
		"class": "danger",
		"color_hash": "#FF7273", 
		"percentage": 40,
		"icon": "dollar-sign",
	},
}

def getInvStatusUi(statusId):
	invStatusUi = invStatSelector[1]
	for status in invStatSelector:
		if status == statusId:
			invStatusUi = invStatSelector[status]				
	return invStatusUi