import httpx

class Package:
    def __init__(self, client: httpx.Client):
        self.client = client

    def list(self, locationCode: str = "", type: str = "", packageCode: str = "", iccid: str = "") -> str:
        """
        Request a list of all the available data packages offered. Optionally filter by country or region.
        
        :param locationCode: Filter by Alpha-2 ISO Country Code. !RG = Regional. !GL = Global
        :param type: BASE - Default product list  TOPUP - Top up product list
        :param packageCode: Used with TOPUP to view top up package for a packageCode slug is alias of packageCode
        :param iccid: Include iccid with TOPUP to see available TOPUP plans
        :return: A list of all the available data packages offered. An example is as follows:

            {
              "errorCode": null,
              "errorMsg": null,
              "success": true,
              "obj": {
                "packageList": [
                  {
                    "packageCode": "CKH139",
                    "name": "Slovenia 5GB 30Days",
                    "price": 112500,
                    "currencyCode": "USD",
                    "volume": 5368709120,
                    "unusedValidTime": 180,
                    "duration": 30,
                    "durationUnit": "DAY",
                    "location": "SI",
                    "description": "Slovenia 5GB 30Days",
                    "activeType": 1,
                    "favorite": false,
                    "retailPrice": 112500,
                    "speed": "3G/4G",
                    "locationNetworkList": [
                      {
                        "locationName": "Slovenia",
                        "locationLogo": "https://static.redteago.com/img/logos/SloveniaFlag.png",
                        "operatorList": []
                      }
                    ]
                  }
                ]
              }
            }
        """
        import http.client

        conn = http.client.HTTPSConnection("api.esimaccess.com")
        payload = {
            "locationCode": locationCode,
            "type": type,
            "packageCode": packageCode,
            "iccid": iccid
        }
        headers = {}
        conn.request("POST", "/api/v1/open/package/list", payload, headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")