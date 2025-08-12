import React, { useState, useEffect } from 'react';
import Nav from '../components/Navbar/Navbar';
import ClientsTable from '../components/ClientsTable'

import { fetchRpAccs } from '../services'
import { withRouter } from 'react-router-dom';

function ClientsTablePage({history}) {

	const [data, setData] = useState([])

	useEffect(() => {
		const fetch_rp = async() => {
			const response_data = await fetchRpAccs()
			if (response_data){
				setData(response_data)
			}
		}
		fetch_rp();
		const fetch_interval = setInterval(() => {
			fetch_rp()
		}, 10000);

		return () => {
			clearInterval(fetch_interval);
		}	
	}, [setData, history])

	return (
		<div>
			<Nav />
			<div>
				<ClientsTable data={data} />
			</div>
		</div>
	)
}

export default withRouter(ClientsTablePage)
