import React from 'react'

const ClientsTable = ({data = []}) => {

	return ( 
		<div >
			<div>
				<div className="mt-2 py-2 align-middle inline-block w-full px-4 py-4">
					<div className="shadow overflow-auto h-100 w-full	border-b border-gray-200 sm:rounded-lg">
						<table className="w-full">
							<thead>
							<tr className="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
								<th className="py-3 px-3 text-center w-auto">Ady</th>
								<th className="py-3 px-3 text-center w-auto">Kody</th>
								<th className="py-3 px-3 text-center w-auto">Balans</th>
								{/* <th className="py-3 px-3 text-center w-auto">Actions</th> */}
							</tr>
							</thead>
							<tbody className="overflow-auto text-gray-600 text-sm font-light h-100">
								{data.map((person, idx) => (
									<tr key={idx}>
										<td className="px-3 py-4 whitespace-nowrap">
											<div className="flex items-center justify-center">
												<div className="ml-4">
													<div className="text-sm font-medium text-gray-900">{person.RpAccUName}</div>
													<div className="text-sm text-gray-500">{person.RpAccMobilePhoneNumber}</div>
												</div>
											</div>
										</td>
										<td className="px-3 py-4 whitespace-nowrap">
											<div className="text-sm text-gray-900">{person.RpAccRegNo}</div>
										</td>
										<td className="px-3 py-4 whitespace-nowrap">
											<span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
												{person.Rp_acc_trans_total.RpAccTrTotBalance} TMT
											</span>
										</td>
										 {/* <td className="py-3 px-3 text-center">
												<div className="flex items-center justify-center">
													<div className="w-4 mr-2 transform hover:text-purple-500 hover:scale-110">
														<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
																<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
																<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
														</svg>
													</div>
													<div className="w-4 mr-2 transform hover:text-purple-500 hover:scale-110">
														<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
																<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
														</svg>
													</div>
													<div className="w-4 mr-2 transform hover:text-purple-500 hover:scale-110">
														<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
																<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
														</svg>
													</div>
												</div>
										</td> */}
									</tr>
								))}

							</tbody>
						</table>
					</div>
				</div>
			</div>
		</div>
	)

}

export default ClientsTable
