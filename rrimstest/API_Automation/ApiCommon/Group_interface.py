from Common.Request import *
from Params.params import *
import time


class Group_interface():

    def __init__(self):
        self.request = Request()

    def add_group(self, domain, cookie, groupName):

        url, data, header = request_data("group_interface", "addGroup")

        apiUrl = domain + url
        data["groupInfo.groupName"] = groupName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_group(self, domain, cookie, groupName=None):

        url, data, header = request_data("group_interface", "findGroup")

        apiUrl = domain + url
        data["groupInfo.searchValue"] = groupName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_groupMenu(self, domain, cookie, groupId):
        url, data, header = request_data("group_interface", "updateGroupMenu")

        apiUrl = domain + url

        data["groupInfo.groupId"] = groupId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response


    def edit_group(self, domain, cookie, groupId, groupName):
        url, data, header = request_data("group_interface", "editGroup")

        apiUrl = domain + url

        data["groupInfo.groupId"] = groupId
        data["groupInfo.groupName"] = groupName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def disable_group(self, domain, cookie, groupId, groupName):
        url, data, header = request_data("group_interface", "disableGroup")

        apiUrl = domain + url

        data["groupInfo.groupId"] = groupId
        data["groupInfo.groupName"] = groupName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
