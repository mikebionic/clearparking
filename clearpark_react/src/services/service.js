import {parking_invoices_mock} from './mock/parking_invoices_mock'

const server_url = process.env.REACT_APP_SERVER_URL || 'http://127.0.0.1:5000'
const rpAccsPath = process.env.REACT_APP_RP_ACCS_PATH || '/clearpark/rp-accs/'
const invoicesPath = process.env.REACT_APP_INVOICES_PATH || '/clearpark/invoices/'
const devicesPath = process.env.REACT_APP_DEVICES_PATH || '/clearpark/devices/'


export const fetchRpAccs = async () => {
	var data = await fetch(`${server_url}${rpAccsPath}`)
	var resp_data = await data.json()
	return resp_data.data
}

export const fetchInvoices = async (RpAccId = null) => {
	var url_args = RpAccId ? `?RpAccId=${RpAccId}` : ''
	// return parking_invoices_mock
	var data = await fetch(`${server_url}${invoicesPath}${url_args}`)
	var resp_data = await data.json()
	return resp_data.data
}

export const fetchDevices = () => {
	return fetch(`${server_url}${devicesPath}`)
}