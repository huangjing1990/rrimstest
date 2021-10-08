from Common.Request import *
from Params.params import *
import time


class User_interface():

    def __init__(self):
        self.request = Request()

    def add_user(self, domain, cookie, userId, userName):

        url, data, header = request_data("user_interface", "addUser")

        apiUrl = domain + url
        data["userInfo.userId"] = userId

        data["userInfo.userName"] = userName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_user(self, domain, cookie, userName=None):

        url, data, header = request_data("user_interface", "findUser")

        apiUrl = domain + url
        data["userInfo.searchValue"] = userName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_userHas(self, domain, cookie, userId):
        url, data, header = request_data("user_interface", "updateUserHas")

        apiUrl = domain + url

        data["userInfo.userId"] = userId

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response


    def edit_user(self, domain, cookie, userId, userName):
        url, data, header = request_data("user_interface", "editUser")

        apiUrl = domain + url

        data["userInfo.userId"] = userId
        data["userInfo.userName"] = userName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def resetPass_worduser(self, domain, cookie, userId, userName):
        url, data, header = request_data("user_interface", "resetPasswordUser")

        apiUrl = domain + url

        data["userInfo.userId"] = userId
        data["userInfo.userName"] = userName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def unLock_worduser(self, domain, cookie, userId, userName):
        url, data, header = request_data("user_interface", "unLockUser")

        apiUrl = domain + url

        data["userInfo.userId"] = userId
        data["userInfo.userName"] = userName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def disable_user(self, domain, cookie, userId, userName):
        url, data, header = request_data("user_interface", "disableUser")

        apiUrl = domain + url

        data["userInfo.userId"] = userId
        data["userInfo.userName"] = userName

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
