# -*- coding: utf-8 -*-
from datetime import datetime

from main.key_generator.utils import (
	generate,
	makeRegNo,
	Pred_reg_num
)

def fetch_and_generate_RegNo(user_id, user_short_name, reg_no_type, RegNo = None):
	pred_reg_num = None
	if not RegNo:
		try:
			reg_num = generate(
				UId = user_id,
				RegNumTypeName = reg_no_type
			)
			RegNo = makeRegNo(
				user_short_name,
				reg_num.RegNumPrefix,
				reg_num.RegNumLastNum+1,
				'',
				True,
				RegNumTypeName = reg_no_type,
			)
		except Exception as ex:
			print(f"{datetime.now()} | RegNum Exception: {ex}. Couldn't generate RegNo using User's credentials")
			RegNo = str(datetime.now().timestamp())

	else:
		pred_reg_num = Pred_reg_num.query\
			.filter_by(GCRecord = None, RegNum = RegNo).first()
		RegNo = RegNo if pred_reg_num else None

	return RegNo, pred_reg_num
