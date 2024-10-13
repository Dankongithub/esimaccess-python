import httpx
from typing import List, Optional
from esimaccess_python.api.pageparam import PageParam

class Package:
    def __init__(self, client: httpx.Client):
        self.client = client

    def list(self, locationCode: Optional[str] = None, type: Optional[str] = "", packageCode: Optional[str] = "", iccid: Optional[str] = ""):
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

    def order(self, transactionId: str, packageInfoList: List, amount: Optional[int] = None):
        """
        Order profiles individualy or in batch. After successful ordering, the SM-DP+ server will return the OrderNo and allocate profiles asynchronously for the order.

        :param transactionId: Unique transaction ID for the order (max 50 characters).
        :param packageInfoList: List of packages to order with packageCode, count, and optional price and periodNum.
        :param amount: Total order amount.
        :return: Response, including the orderNo.
        """
        payload = {
            "transactionId": transactionId,
            "amount": amount,
            "packageInfoList": packageInfoList
        }

        response = self.client.post("https://api.esimaccess.com/api/v1/open/esim/order", json=payload)
        return response.text

    def query(self, pager: PageParam, orderNo: Optional[str] = None, iccid: Optional[str] = None, startTime: Optional[str] = None, endTime: Optional[str] = None):
        """
        Query all eSIM profile details allocated to partner and their status.
        :param pager: Page parameters for querying.
        :param orderNo: Order number
        :param iccid: eSIM ICCID
        :param startTime: Start time (ISO UTC time)
        :param endTime: End time (ISO UTC time).
        """
        payload = {
            "orderNo": orderNo,
            "iccid": iccid,
            "pager": pager.to_dict(),
            "startTime": startTime,
            "endTime": endTime
        }

        response = self.client.post('https://api.esimaccess.com/api/v1/open/esim/query', json=payload)

        return response.text



