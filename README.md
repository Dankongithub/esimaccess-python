# Esimaccess Python Library

Python SDK for the Esimaccess API

## Documentation

See the [API Docs](https://docs.esimaccess.com/).

## Usage

The library needs to be configured with your account's access code which is availible in your developer dashboard.

### To list all available data packages
```python
from esimaccess_python import Package, authenticate

client = Package(authenticate("Access code"))

print(client.list())
```