import React from 'react'

function UserName(props) {

	return (
		<div>
			<div className="p-2">
				<h3 className="text-center text-xl text-gray-900 font-medium leading-8">{props.RpAccUName}</h3>
				<div className="text-center text-gray-400 text-xs font-semibold">
						<p>Kody: {props.RpAccRegNo}</p>
						<p>Tel: {props.RpAccMobilePhoneNumber}</p>
				</div>
				<table className="justify-center flex text-xs my-3">
					<tbody>
						<tr>
							<td className="px-2 py-2 text-gray-500 font-semibold">Balance</td>
							<td className="px-2 py-2">{props.Rp_acc_trans_total.RpAccTrTotBalance}</td>
						</tr>
					</tbody>
				</table>
      </div>
		</div>
	)
}

export default UserName
