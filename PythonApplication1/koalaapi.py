import urllib.request
import http.client
import urllib.parse
import json
class client(object):
    """提供koala系统的接口"""
    base_address = ""
    port = ""
    user_name = ""
    password = ""
    def __init__(self, **kwargs):
        """构造方法"""
        self.__dict__ = kwargs
        
    def login(self):
        url = "/auth/login"
        data = {"username" : self.user_name, "password" : self.password }
        params = urllib.parse.urlencode(data)
        headers = {"user-agent":"Koala Admin","Content-Type":"application/x-www-form-urlencoded"}
        #with urllib.request.urlopen(self.base_address, data) as response:
        #    json_str = response.read().decode("utf-8")
        #    result = json.loads(json_str)
        #    return result
        conn = http.client.HTTPConnection(self.base_address, self.port)
        conn.request("POST", url, params, headers)
        response = conn.getresponse()
        json_str = response.read().decode("utf-8")
        result = json.loads(json_str)
        return result