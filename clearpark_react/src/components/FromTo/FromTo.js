import React from 'react'

function FromTo({entrance=0, exit=0}) {
	return (
		<div>
			<div className="w-full flex justify-center items-center">
				<div className="container flex flex-col gap-1 mx-5">
						<div className="bg-gray-100 rounded-lg w-full h-auto mt-2 flex flex-row justify-between divide-x divide-solid divide-gray-400">
								<div className="relative flex-1 flex flex-col px-2">
										<label className="text-gray-800  tracking-wider">Giriş</label>
										<label className="text-green-800 text-1xl font-bold">{entrance}</label>
								</div>
								<div className="relative flex-1 flex flex-col px-2">
										<label className="text-gray-800  tracking-wider">Çykyş</label>
										<label className="text-green-800 text-1xl font-bold">{exit}</label>
								</div>
						</div>
				</div>
		</div>
		</div>
	)
}

export default FromTo
