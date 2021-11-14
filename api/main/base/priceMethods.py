from datetime import datetime

from main import Config
from main.models import Res_price_group
from main.models import Exc_rate
from main.models import Currency
from .dataMethods import configureDecimal

# main_currency = "USD"
# from_currency = "USD"
# to_currency = "TMT"
def price_currency_conversion(
	priceValue = None,
	from_currency = None,
	to_currency = None,
	currencies_dbModel = None,
	exc_rates_dbModel = None,
	value_type = "out",
	from_exc_rate_value = None,
	to_exc_rate_value = None,
):

	data = {}

	try:
		main_currency = Config.MAIN_CURRENCY_CODE
		view_currency = Config.DEFAULT_VIEW_CURRENCY_CODE

		if not currencies_dbModel:
			currencies_dbModel = Currency.query.filter_by(GCRecord = None).all()

		if not exc_rates_dbModel:
			exc_rates_dbModel = Exc_rate.query.filter_by(GCRecord = None).all()

		main_currency_data = [currency for currency in currencies_dbModel if currency.CurrencyCode == main_currency]
		view_currency_data = [currency for currency in currencies_dbModel if currency.CurrencyCode == view_currency]

		if (not main_currency_data or not view_currency_data):
			raise Exception

		from_currency = from_currency if from_currency else main_currency
		to_currency = to_currency if to_currency else view_currency

		from_currency_data = [currency for currency in currencies_dbModel if currency.CurrencyCode == from_currency]
		from_currency_data = from_currency_data[0] if from_currency_data else main_currency_data[0]

		to_currency_data = [currency for currency in currencies_dbModel if currency.CurrencyCode == to_currency]
		to_currency_data = to_currency_data[0] if to_currency_data else view_currency_data[0]

		from_exchange_rate = [exc_rate.to_json_api() for exc_rate in exc_rates_dbModel if exc_rate.CurrencyId == from_currency_data.CurrencyId and not exc_rate.GCRecord]
		from_exchange_rate = (sorted(from_exchange_rate, key = lambda i: i["ExcRateDate"]))

		to_exchange_rate = [exc_rate.to_json_api() for exc_rate in exc_rates_dbModel if exc_rate.CurrencyId == to_currency_data.CurrencyId and not exc_rate.GCRecord]
		to_exchange_rate = (sorted(to_exchange_rate, key = lambda i: i["ExcRateDate"]))

		from_rate_value = 1
		if from_exchange_rate:
			from_rate_value = from_exchange_rate[-1]["ExcRateOutValue"] if value_type == "out" else from_exchange_rate[-1]["ExcRateInValue"]
			from_rate_value = from_rate_value if from_rate_value else 1
		from_rate_value = from_rate_value if from_currency != main_currency else 1

		to_rate_value = 1
		if to_exchange_rate:
			to_rate_value = to_exchange_rate[-1]["ExcRateOutValue"] if value_type == "out" else to_exchange_rate[-1]["ExcRateInValue"]
			to_rate_value = to_rate_value if to_rate_value else 1
		to_rate_value = to_rate_value if to_currency != main_currency else 1

		if from_exc_rate_value:
			from_rate_value = from_exc_rate_value

		if to_exc_rate_value:
			to_rate_value = to_exc_rate_value

		priceValue = float(configureDecimal(priceValue / from_rate_value * to_rate_value))

		data = {
			"ResPriceValue": priceValue,
			"CurrencyCode": to_currency_data.CurrencyCode,
			"CurrencyId": to_currency_data.CurrencyId,
			"ExcRateValue": to_rate_value
		}

	except Exception as ex:
		print(f"{datetime.now()} | Price currency conversion Exception: {ex}")

	return data


def calculatePriceByGroup(
	ResPriceGroupId,
	Res_price_dbModels,
	Res_pice_group_dbModels = None):

	data = []
	try:
		if not Res_price_dbModels:
			raise Exception

		if not Res_pice_group_dbModels:
			Res_pice_group_dbModels = Res_price_group.query.filter_by(GCRecord = None).all()

		if not ResPriceGroupId:
			data = [res_price.to_json_api() 
				for res_price in Res_price_dbModels
				if res_price.ResPriceTypeId == 2
				and not res_price.GCRecord]

		if ResPriceGroupId:
			data = [res_price.to_json_api() 
				for res_price in Res_price_dbModels 
				if res_price.ResPriceTypeId == 2 
				and res_price.ResPriceGroupId == ResPriceGroupId
				and not res_price.GCRecord]

			if not data:
				thisPriceGroupList = [priceGroup for priceGroup in Res_pice_group_dbModels if priceGroup.ResPriceGroupId == ResPriceGroupId]
				if thisPriceGroupList:
					if not thisPriceGroupList[0].ResPriceGroupAMEnabled:
						raise Exception

					FromResPriceTypeId = thisPriceGroupList[0].FromResPriceTypeId
					ResPriceGroupAMPerc = thisPriceGroupList[0].ResPriceGroupAMPerc

					data = [res_price.to_json_api() 
						for res_price in Res_price_dbModels 
						if res_price.ResPriceTypeId == FromResPriceTypeId
						and not res_price.GCRecord]

					if not data:
						raise Exception

					CalculatedPriceValue = float(data[0]["ResPriceValue"]) + (float(data[0]["ResPriceValue"]) * float(ResPriceGroupAMPerc) / 100)
					data[0]["ResPriceValue"] = float(configureDecimal(CalculatedPriceValue))

	except Exception as ex:
		print(f"{datetime.now()} | Res price calculation Exception: {ex}")
		pass

	return data