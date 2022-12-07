# -*- coding: utf-8 -*-
import requests
class ApiRequest(object):
    def send_requests(self,method,url,data=None,params=None,headers=None,cookies=None,json=None,
                      files=None,auth=None,timeout=None,proxies=None,verify=None,cert=None):
        self.r=requests.request(method=method,url=url,headers=headers,data=data,params=params,cookies=cookies,
                                json=json,files=files,auth=auth,timeout=timeout,proxies=proxies,verify=verify,
                                cert=cert)
        return self.r