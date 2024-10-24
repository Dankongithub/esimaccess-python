# Esimaccess Python Library

Python SDK for the Esimaccess API, using httpx.

## Documentation

See the [API Docs](https://docs.esimaccess.com/).
## Installation

```
pip install esimaccess-python
```
## Usage

The library needs to be configured with your account's access code which is availible in your developer dashboard.
```python
from esimaccess_python import Package, authenticate

client = Package(authenticate("Access code"))
```


#### To Get All Data Packages
```python
print(client.list())
```

#### To Order Profiles
```python
print(client.order(transactionId="your_txn_id", amount=15000, packageInfoList=[{"packageCode": "7aa948d363", "count": 1, "price": 15000}]))
```

#### To Query All Allocated Profiles
```python
from esimaccess_python import PageParam

print(client.query(orderNo="B23120118131854", iccid="", pager=PageParam(pageNum=1, pageSize=20)))
```

#### To Cancel Profile
```python
print(client.cancel(iccid='8943108170000775671'))
```

#### To Suspend Profile
```python
print(client.suspend(iccid='8943108170000775671'))
```

#### To Unsuspend Profile
```python
print(client.unsuspend(iccid='8943108170000775671'))
```

#### To Revoke Profile
```python
print(client.revoke(iccid='8943108170000775671'))
```

#### To Get Balance
```python
print(client.balance())
```

#### To Top Up
```python
print(client.topup(iccid='89852245280001354019', topUpCode='TOPUP_CKH491', transactionId='top_up_for_existing_plan_CKH491', amount=15000))
```

#### To Set Webhook
```python
print(client.set_webhook(webhook='https://webhook.endpoint.site/unique-webhook'))
```

#### To Get Current Webhook
```python
print(client.query_webhook(webhook='https://webhook.endpoint.site/unique-webhook'))
```

#### To Send SMS
```python
print(client.sendSms(iccid='89852000261098474477', message='Your Message!'))
```