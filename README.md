# ClearParking Smart parking IoT System

## Workflow

So there should be a resource in database with its price and all data.. (total, etc..)
The Res_price is a price for a minute used by resource.

We take the Resource ResGuid and put into .env

There should be a user (Rp_acc) with it's registered Device (qr-code), and Rp_acc should have it's Rp_acc_trans_total.

In the entrance, scanner scans the QR-code and finds a Device and its Rp_acc, it records the Attendance AttStartDate, Specify it by AttTypeId.
In the exit, scanner scans the QR and records the Attendance AttEndDate, then calculates the Whole time spent or used by Resource and returns its price.

------
> Note! It supports saphasap and akhsasap! Just switch the DB_STRUCTURE in .env file

------ 
in case if you don't have attendance table:
```sql
create table tbl_dk_attendance("AttId" int, "AttGuid" varchar, "EmpId" int, "RpAccId" int, "DevId" int, "UId" int, "AttTypeId" int, "AttDesc" varchar, "AttDate" timestamp without time zone,"CreatedDate" timestamp without time zone,"ModifiedDate" timestamp without time zone);
```

----------

## API

Route: "/find-device/"
Method: POST
URL: ${hostname}${url_prefix}
Headers: {`"Authorization": "Bearer ${token}"`}
Payload: {"data": ${qr_data}}
urlParams: type=["entrance", "exit"]

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

---

> Example response 

```json
{
  "data": {
    "AddInf1": null,
    "AddInf2": null,
    "AddInf3": null,
    "AddInf4": null,
    "AddInf5": null,
    "AddInf6": null,
    "CId": 1,
    "CreatedDate": "2021-10-22 14:40:02",
    "CreatedUId": null,
    "DbGuid": null,
    "Device": {
      "AddInf1": null,
      "AddInf2": null,
      "AddInf3": null,
      "AddInf4": null,
      "AddInf5": null,
      "AddInf6": "id=QP1A.190711.020,androidId=e4d788879fbe6635,baseOS=,release=10,brand=samsung,device=a7y18lte,display=QP1A.190711.020.A750FXXU5CTK1,manufacturer=samsung,model=SM-A750F,isPhysicalDevice=true",
      "AllowedDate": null,
      "CreatedDate": "2021-01-15 20:04:55",
      "CreatedUId": null,
      "DevDesc": null,
      "DevGuid": "d1bddb81-2c27-4b93-b79f-5d1e5576eb78",
      "DevId": 2,
      "DevName": "2021-01-14 23:44:26.778464",
      "DevUniqueId": "788879fbe6635",
      "DevVerifyDate": "2021-01-15 20:04:57",
      "DevVerifyKey": null,
      "DisallowedDate": null,
      "GCRecord": null,
      "IsAllowed": false,
      "ModifiedDate": "2021-01-21 20:52:16",
      "ModifiedUId": null,
      "RpAccId": 50,
      "SyncDateTime": "2021-01-15 20:04:55",
      "UId": null
    },
    "DeviceQty": null,
    "DivId": 1,
    "EmpId": null,
    "GCRecord": null,
    "GenderId": null,
    "IsMain": null,
    "ModifiedDate": "2021-10-22 14:40:02",
    "ModifiedUId": null,
    "NatId": null,
    "ReprId": null,
    "ResPriceGroupId": null,
    "RpAccAddress": "helloworlddd",
    "RpAccBirthDate": null,
    "RpAccEMail": null,
    "RpAccFirstName": null,
    "RpAccGuid": "9d40a40d-cf50-4bbd-a7e5-733a0314beb0",
    "RpAccHomePhoneNumber": "",
    "RpAccId": 50,
    "RpAccLangSkills": null,
    "RpAccLastActivityDate": "2021-10-22 15:01:02",
    "RpAccLastActivityDevice": "Browser: chrome, Platform: linux, Details: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "RpAccLastName": null,
    "RpAccLatitude": 0.0,
    "RpAccLongitude": 0.0,
    "RpAccMobilePhoneNumber": "+99361509038",
    "RpAccName": "bionicccccc",
    "RpAccPassportIssuePlace": null,
    "RpAccPassportNo": null,
    "RpAccPatronomic": null,
    "RpAccPurchBalanceLimit": 0.0,
    "RpAccRegNo": "ARAK12",
    "RpAccResidency": null,
    "RpAccSaleBalanceLimit": 0.0,
    "RpAccStatusId": 1,
    "RpAccTypeId": 2,
    "RpAccUName": "mike",
    "RpAccViewCnt": null,
    "RpAccVisibleIndex": null,
    "RpAccWebAddress": "",
    "RpAccWorkFaxNumber": "",
    "RpAccWorkPhoneNumber": "",
    "RpAccZipCode": "",
    "SyncDateTime": "2021-10-22 14:40:02",
    "UnusedDeviceQty": null,
    "WpId": null
  },
  "message": "Find Device",
  "total": 1
}
```

-------------
## IoT Device Set Ip function to update it if changes:

Route: "/set-ip/"
Method: GET
urlParams: device_key={secret_key_of_device_in_env}

-------------

## Other data routes for UI

/clearpark/attendances/
/clearpark/rp-accs/
/clearpark/devices/

> Response

```json
{
  "status": 1,
  "data": "[...data]",
  "message": "Info"
}
```