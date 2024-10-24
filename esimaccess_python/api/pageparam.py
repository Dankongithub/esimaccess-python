from typing import Optional


class PageParam:
    def __init__(self, pageSize: int, pageNum: int, total: int):
        self.pageSize = pageSize
        self.pageNum = pageNum
        self.total = total

    def __init__(self, pageSize: int, pageNum: int):
        self.pageSize = pageSize
        self.pageNum = pageNum
        self.total = None

    def to_dict(self) -> dict:
        """
        Convert the PageParam instance to a dictionary, suitable for use in an API request.

        :return: A dictionary representing the PageParam.
        """
        return {
            "pageSize": self.pageSize,
            "pageNum": self.pageNum,
            "total": self.total
        }

