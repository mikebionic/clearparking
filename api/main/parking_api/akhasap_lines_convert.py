
import uuid

from main import db
from main.models.ak_models.Client_line import Client_line
from main.models.ak_models.Mat_trans_line import Mat_trans_line


def akhasap_line_convert(invoice, inv_line, RpAccId):
	client_line_data = {
		"cl_total": inv_line.InvLineFTotal,
		"cl_type": 2,
		"cl_trans_name": "Satuw Fakturasy",
		"inv_id": inv_line.InvId,
		"bank_fich_head_id": 0,
		"arap_id": RpAccId,
		"ks_line_id": 0,
		"cl_credit": 0,
		# "arap_id_acc_card_id": arap_id_acc_card_id,
		# "op_bl_l_id": op_bl_l_id,
		"inv_real_code": invoice.InvRegNo,
		# "spe_code": spe_code,
		"group_code": "Parking_client_line",
		# "security_code": security_code,
		"cl_desc": "Parking_client_line",
		"p_id": 1,
		# "rep_rate": rep_rate,
		# "rep_debit": rep_debit,
		# "rep_credit": rep_credit,
		"cl_id_guid": uuid.uuid4(),
	}

	new_trans_line = Client_line(**client_line_data)
	db.session.add(new_trans_line)
	db.session.commit()

	mat_line_data = {
		"material_id": inv_line.ResId,
		"fich_line_id": inv_line.InvLineId,
		"mat_inv_line_id": 0,
		"arap_id": RpAccId,
		"mat_trans_type_id": 1,
		"mat_trans_type_code": "Satuw_Fich",
		"mat_trans_line_amount_out": inv_line.InvLineAmount,
		"mat_trans_line_price_out": inv_line.InvLinePrice,
		"mat_trans_line_totalprice": inv_line.InvLineTotal,
		"mat_trans_line_nettotal": inv_line.InvLineFTotal,
		# "mat_trans_line_amount_in": mat_trans_line_amount_in,
		# "mat_trans_line_price_in": mat_trans_line_price_in,
		# "mat_trans_line_totalprice_in": mat_trans_line_totalprice_in,
		# "mat_trans_line_nettotal_in": mat_trans_line_nettotal_in,
		# "mat_trans_line_wh_id_out": mat_trans_line_wh_id_out,
		# "mat_trans_line_wh_id_in": mat_trans_line_wh_id_in,
		# "mat_trans_line_wh_amount": mat_trans_line_wh_amount,
		"p_id": 1,
		"fich_type_id": invoice.InvTypeId,
		"mat_inv_type_id": 0,
		"unit_det_id": 1,
		# "mat_trans_line_wh_id_amount": mat_trans_line_wh_id_amount,
		"inv_real_code": invoice.InvRegNo,
		# "fich_line_expiredate": fich_line_expiredate,
		# "mat_trans_line_id_out": mat_trans_line_id_out,
		# "mat_trans_line_amount_in_onhand": mat_trans_line_amount_in_onhand,
		# "mat_trans_line_outcost": mat_trans_line_outcost,
		# "mat_trans_line_retcost": mat_trans_line_retcost,
		# "mat_trans_line_out_remain_amount": mat_trans_line_out_remain_amount,
		"mat_trans_line_id_guid": uuid.uuid4(),
		# "rep_rate": rep_rate,
		# "rep_currency_id": rep_currency_id,
	}

	new_mat_line = Mat_trans_line(**mat_line_data)
	db.session.add(new_mat_line)
	db.session.commit()
















	