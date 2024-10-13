import httpx
from typing import List, Optional
from esimaccess_python.api.pageparam import PageParam
import json

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
        return json.loads(response.text)

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
        return json.loads(response.text)

    def query(self, pager: PageParam, orderNo: Optional[str] = None, iccid: Optional[str] = None, startTime: Optional[str] = None, endTime: Optional[str] = None) -> dict:
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

        return json.loads(response.text)

    def cancel(self, iccid: str) -> dict:
        """
        Cancel an inactive unused eSIM profile removing all information associated with it. Refunded to your balance.

        :param iccid: eSIM ICCID
        :return: Request results
        """

        payload = {
            "iccid": iccid
        }

        response = self.client.post('https://api.esimaccess.com/api/v1/open/esim/cancel', json=payload)

        return json.loads(response.text)

    def suspend(self, iccid: str) -> dict:
        """
        Request to suspend or pause data service to an esim profile.

        :param iccid: eSIM ICCID
        :return: Request results
        """

        payload = {
            "iccid": iccid
        }

        response = self.client.post('https://api.esimaccess.com/api/v1/open/esim/suspend', json=payload)

        return json.loads(response.text)

    def unsuspend(self, iccid: str) -> dict:
        """
        Request to unsuspend or reactivate data service to an esim profile.

        :param iccid: eSIM ICCID
        :return: Query results
        """

        payload = {
            "iccid": iccid
        }

        response = self.client.post('https://api.esimaccess.com/api/v1/open/esim/unsuspend', json=payload)

        return json.loads(response.text)

    def revoke(self, iccid: str) -> dict:
        """
        Request to close and remove an active eSIM and data plan. Non-refundable.

        :param iccid: eSIM ICCID
        :return: Query results
        """

        payload = {
            "iccid": iccid
        }

        response = self.client.post('https://api.esimaccess.com/api/v1/open/esim/revoke', json=payload)

        return json.loads(response.text)

    def balance(self) -> dict:
        """
        Request to close and remove an active eSIM and data plan. Non-refundable.

        :return: Query results
        """

        response = self.client.post('https://api.esimaccess.com/api/v1/open/balance/query')

        return json.loads(response.text)

    def topup(self, iccid: str, packageCode: str, transactionId: str, amount: Optional[int] = None) -> dict:
        """
        Request to close and remove an active eSIM and data plan. Non-refundable.

        :param iccid: eSIM ICCID
        :param packageCode: Recharge Package Number
        :param transactionId: User created transaction ID
        :return: Request results
        """
        payload = {
            "iccid": iccid,
            "packageCode": packageCode,
            "transactionId": transactionId,
            "amount": amount
        }

        response = self.client.post('https://api.esimaccess.com/api/v1/open/esim/topup', json=payload)

        return json.loads(response.text)

    def set_webhook(self, webhook: str) -> dict:
        """
        Set or update your webhook URL via an API call.

        :param webhook: webhook URL
        :return: Request results
        """

        payload = {
            "webhook": webhook
        }

        response = self.client.post('https://api.esimaccess.com/api/v1/open/webhook/save', json=payload)

        return json.loads(response.text)

    def query_webhook(self) -> dict:
        """
        View the currently set webhook

        :return: Currently set webhook URL
        """
        response = self.client.post('https://api.esimaccess.com/api/v1/open/webhook/query')

        return json.loads(response.text)

    def sendSms(self, iccid: str, message: str) -> dict:
        """
        Supported by some networks. Only installed eSIMs that supports receiving SMS will work.

        :param iccid: eSIM ICCID
        :param message: SMS message (max 500 characters)
        :return: Currently set webhook URL
        """
        response = self.client.post('https://api.esimaccess.com/api/v1/open/esim/sendSms')

        return json.loads(response.text)
