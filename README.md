# ClearParking — Smart Parking IoT System

![ClearParking Demo](https://mikebionic.github.io/portfolio/static/projects/using/clearparking.webp)
**Demo Video:** [https://youtu.be/48IGrkGlwJY](https://youtu.be/48IGrkGlwJY)

ClearParking — Small, microserviced IoT parking management system.
Microservice design (connected small applications) — components are small, replaceable and independent.

Built using **Python, Go, C#, JavaScript and Arduino**. Each component is modular and can be swapped thanks to the microservice architecture and clean project design. UI / accounting integrations are exchangeable.

Dedicated React Web App for user-facing flows and a separate monitoring web app to watch application activity.

---

## Key concepts / workflow

* There is a **Resource** in database with its price and all related data (totals, groups, etc.).
* `Res_price` — price **per minute** for the resource.
* Put the target `ResGuid` into `.env` when needed.
* There should be a **user account** (`Rp_acc`) with a registered device (QR code). Each `Rp_acc` has fields such as `Rp_acc_trans_total` to reflect accumulated totals.
* **Entrance**: scanner scans QR -> finds Device -> finds `Rp_acc` -> records attendance start (`AttStartDate`) with `AttTypeId`.
* **Exit**: scanner scans QR -> records attendance end (`AttEndDate`) -> system calculates whole time used and returns the price.

> Note: It supports **Saphasap** and **AkHasap (akhsasap)** schemas. Switch the `DB_STRUCTURE` value in `.env` to select which schema your deployment uses.

---

## Important DB note

If you don't have an attendance table, you can create it like this:

```sql
create table tbl_dk_attendance(
  "AttId" int,
  "AttGuid" varchar,
  "EmpId" int,
  "RpAccId" int,
  "DevId" int,
  "UId" int,
  "AttTypeId" int,
  "AttDesc" varchar,
  "AttDate" timestamp without time zone,
  "CreatedDate" timestamp without time zone,
  "ModifiedDate" timestamp without time zone
);
```

If using **AkHasap** schema, **disable triggers** in the `tbl_mg_arap_attandence` table to avoid duplicate logging.

---

## API (full request + response examples preserved)

### Find Device

* **Route:** `/find-device/`
* **Method:** `POST`
* **URL:** `${hostname}${url_prefix}`
* **Headers:** `{ "Authorization": "Bearer ${token}" }`
* **Payload:** `{ "data": ${qr_data} }`
* **urlParams:** `type=["entrance", "exit"]`

**Responses**

**200 (device found)**

```json
{
    "status": 1,
    "data": {...ulanyjy}
}
```

**200 (device not found)**

```json
{
    "status": 0,
    "data": {}
}
```

**401 (unauthorized)**

```json
{
    "status": 0,
    "data": {}
}
```

**Example successful response (full payload)**

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

---

### IoT Device: set IP

* **Route:** `/set-ip/`
* **Method:** `GET`
* **URL params:** `device_key={secret_key_of_device_in_env}`

This endpoint is used by the device to update its current public IP (or local IP, as configured) — useful for remote devices with dynamic IPs.

Example:

```
GET /set-ip/?device_key=YOUR_DEVICE_SECRET
```

---

### Other data routes for UI

These endpoints return lists used by the UI for admin/monitoring:

* `/clearpark/attendances/`
* `/clearpark/rp-accs/`
* `/clearpark/devices/`

**Example response**

```json
{
  "status": 1,
  "data": "[...data]",
  "message": "Info"
}
```

---

## Price calculation (behavior & example)

* `Res_price` is **per-minute**.
* Compute duration in seconds: `diff = AttEndDate - AttStartDate`.
* Convert to minutes and round up to the next integer minute (common parking behavior):
  `minutes = ceil(diff_seconds / 60)`.
* `total_price = minutes * Res_price`.
* Always store timestamps in **UTC** and apply timezone conversion only at presentation layer.

**Example:** start 10:00:00, end 10:07:15 -> diff 435s -> 7.25 min -> ceil -> 8 minutes -> `total_price = 8 * Res_price`.


## Hardware & IO integration

* **Arduino** reads sensors (presence, IR, etc.) and QR/barcode scanner triggers.
* **Go-based IO interface** handles barcode scanning, printing, and motor control.

  * When barcode is read, Go service happily receives the read and forwards to the API.
  * After checkout, Arduino runs motor to open the gate and keeps it open until car fully enters/exits (safety latch via sensors).
* Thermal printing (tickets/receipts) and barcode scanning are accessible through the IO interface.


## Quick Start (local / dev)

1. Copy `.env.example` to `.env`.
2. Fill required keys:

   * `DB_STRUCTURE` — `saphasap` or `akhsasap`
   * `ResGuid` — resource GUID for the parking service
   * `SECRET_KEY` / `JWT_SECRET` — API auth
   * Device-specific secrets where needed (used by `/set-ip/`)
3. Start services (example microservice order):

   * Start DB
   * Start backend API (Python/Go/C# service)
   * Start React UI
   * Start Arduino service (or simulator)
4. Test:

   * Use `/find-device/` with a QR data string in `data` body and `type=entrance`, then `type=exit` later.


## Example curl commands

Find device:

```bash
curl -X POST "https://example.com/api/find-device/?type=entrance" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"data":"<QR_STRING>"}'
```

Set device IP:

```bash
curl "https://example.com/api/set-ip/?device_key=DEVICE_SECRET"
```

Get attendances (UI):

```bash
curl -H "Authorization: Bearer $TOKEN" "https://example.com/clearpark/attendances/"
```


---

## Security & operations

* Use **HTTPS** in production. Do not expose device secrets publicly.
* All API calls should be authenticated with Bearer JWT / token.
* Validate QR payloads on server-side to avoid injection.
* Keep device secrets rotated periodically.
* Log attendance events and errors to a central place for troubleshooting (centralized logging helps debugging IoT edge cases).


## Troubleshooting tips

* If device not found: check `DevUniqueId` and `DevGuid` mapping in `tbl_device`.
* If price calculation mismatches: ensure both start/end timestamps use the same timezone (store as UTC).
* If duplicate attendances on AkHasap: verify that triggers in `tbl_mg_arap_attandence` are disabled (as noted above).


## Project notes / finishing remarks

Clearparking connects small microservices and hardware to provide a flexible parking management system. Because of the modular design you can replace the accounting system (AkHasap, 1C, Atlant, manual CSV, etc.) or swap the UI without touching the IoT code.

Which one do you want next?
