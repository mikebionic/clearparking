# ClearParking Smart parking IoT System

## API

Route: "/find-device/"
Method: POST
URL: ${hostname}${url_prefix}
Headers: {`"Authorization": "Bearer ${token}"`}
Payload: {"data": ${qr_data}}

> Response

200
{
    "status": 1,
    "data": {...ulanyjy}
}

---

200
{
    "status": 0,
    "data": {}
}

---

401
{
    "status": 0,
    "data": {}
}

------------------------------------

## Workflow

So there should be a resource in database with its price and all data.. (total, etc..)
The Res_price is a price for a minute used by resource.

We take the Resource ResGuid and put into .env

There should be a user (Rp_acc) with it's registered Device (qr-code), and Rp_acc should have it's Rp_acc_trans_total.

In the entrance, scanner scans the QR-code and finds a Device and its Rp_acc, it records the Attendance AttStartDate, Specify it by AttTypeId.
In the exit, scanner scans the QR and records the Attendance AttEndDate, then calculates the Whole time spent or used by Resource and returns its price.
