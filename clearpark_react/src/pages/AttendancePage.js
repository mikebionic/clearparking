import React, { useState, useEffect } from 'react'
import { withRouter } from 'react-router-dom'
import InvoicesTable from '../components/InvoicesTable'
import Nav from '../components/Navbar/Navbar'

import { fetchInvoices } from '../services'

const AttendancePage = ({history}) => {

	const [data, setData] = useState([])

	useEffect(() => {
		const fetch_logs = async () => {
			try {
				console.log('starting fetch of inv')
				const invoices_data = await fetchInvoices()
				setData(invoices_data)
			} catch (e){
				console.log(e)
			}
		}
		fetch_logs();
		const fetch_interval = setInterval(() => {
			fetch_logs()
		}, 10000);

		return () => {
			clearInterval(fetch_interval);
		}	
	}, [setData, history])

	return (
		<div>
			<Nav />
			<div>
				<InvoicesTable data={data} />
			</div>
		</div>
	)
}

export default withRouter(AttendancePage)