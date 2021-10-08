from Common.Request import *
from Params.params import *
import time


class Company_interface():

    def __init__(self):
        self.request = Request()

    def add_company(self, domain, cookie, comName):
        url, data, header = request_data("company_interface", "addCompany")

        apiUrl = domain + url
        data["companyInfo.comName"] = comName

        data["companyInfo.enablingTime"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def find_company(self, domain, cookie):
        url, data, header = request_data("company_interface", "findCompany")

        apiUrl = domain + url

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def edit_company(self, domain, cookie, comId, comName):
        url, data, header = request_data("company_interface", "editCompany")

        apiUrl = domain + url

        data["companyInfo.comId"] = comId
        data["companyInfo.comName"] = comName
        data["companyInfo.enablingTime"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response

    def disable_company(self, domain, cookie, comId, comName):
        url, data, header = request_data("company_interface", "disableCompany")

        apiUrl = domain + url

        data["companyInfo.comId"] = comId
        data["companyInfo.comName"] = comName
        data["companyInfo.enablingTime"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data["companyInfo.state"] = "0"

        response = self.request.post_request(apiUrl, data, header, cookie)

        return response
