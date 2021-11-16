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