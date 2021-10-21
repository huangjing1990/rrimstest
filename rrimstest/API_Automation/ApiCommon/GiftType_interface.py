from Common.Request import *
from Params.params import *
import time


class GiftType_interface():

    def __init__(self):
        self.request = Request()

    def add_giftType(self, domain, cookie, giftTypeName):
        url, data, header = request_data("giftType_interface", "addGiftType")

        apiUrl = domain + url
        data["giftTypeInfo.giftTypeName"] = giftTypeName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_giftType(self, domain, cookie, giftTypeName=None):
        url, data, header = request_data("giftType_interface", "findGiftType")

        apiUrl = domain + url
        data["giftTypeInfo.searchValue"] = giftTypeName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response


    def edit_giftType(self, domain, cookie, giftTypeId, giftTypeName=None, giftTypeName1=None ):
        url, data, header = request_data("giftType_interface", "editGiftType")

        apiUrl = domain + url

        data["giftTypeName"] = giftTypeName
        data["giftTypeInfo.giftTypeId"] = giftTypeId
        data["giftTypeInfo.giftTypeName"] = giftTypeName1

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def disable_giftType(self, domain, cookie, giftTypeId,  giftTypeName=None):
        url, data, header = request_data("giftType_interface", "disableGiftType")

        apiUrl = domain + url

        data["giftTypeName"] = giftTypeName
        data["giftTypeInfo.giftTypeId"] = giftTypeId
        data["giftTypeInfo.giftTypeName"] = giftTypeName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
