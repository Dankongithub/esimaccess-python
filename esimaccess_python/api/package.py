import httpx
from typing import List

class Package:
    def __init__(self, client: httpx.Client):
        self.client = client

    def list(self, locationCode: str = "", type: str = "", packageCode: str = "", iccid: str = ""):
        """
        Request a list of all the available data packages offered. Optionally filter by country or region.
        
        :param locationCode: Filter by Alpha-2 ISO Country Code. !RG = Regional. !GL = Global
        :param type: BASE - Default product list  TOPUP - Top up product list
        :param packageCode: Used with TOPUP to view top up package for a packageCode slug is alias of packageCode
        :param iccid: Include iccid with TOPUP to see available TOPUP plans
        :return: A list of all the available data packages offered.
        """
        payload = {
            "locationCode": locationCode,
            "type": type,
            "packageCode": packageCode,
            "iccid": iccid
        }

        response = self.client.post("https://api.esimaccess.com/api/v1/open/package/list", json=payload)
        return response.text

    def order(self, transactionId: str, packageInfoList: List, amount: int = -1):
        """
        Order profiles individualy or in batch. After successful ordering, the SM-DP+ server will return the OrderNo and allocate profiles asynchronously for the order.

        :param transactionId: Unique transaction ID for the order (max 50 characters).
        :param packageInfoList: List of packages to order with packageCode, count, and optional price and periodNum.
        :param amount: Total order amount.
        :return: Response, including the orderNo.
        """
        payload = {
            "transactionId": transactionId,
            "packageInfoList": packageInfoList
        }
        if amount != -1:
            payload["amount"] = amount

        response = self.client.post("https://api.esimaccess.com/api/v1/open/esim/order", json=payload)
        return response.text