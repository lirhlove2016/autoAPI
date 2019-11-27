# coding:utf-8
import requests


# 封装requests
class ApiRequest:
    def __init__(self, method, url, data, timeout, headers=None):
        if headers is None:
            headers = {}
        self.url = url
        self.method = method
        self.data = data
        self.headers = headers
        self.timeout=timeout

    # 根据不同方法访问接口
    def api_request(self):
        # print('start request-----------------------------------------------')
        # print(self.method,self.url,self.data,self.headers)

        if self.method == 'post':

            r = requests.post(self.url, data=self.data,timeout=self.timeout, headers=self.headers)
            return r

        elif self.method == 'get':
            r = requests.get(self.url, params=self.data,timeout=self.timeout,headers=self.headers)
            return r
        elif self.method == 'put':
            r = requests.put(self.url, params=self.data,timeout=self.timeout,headers=self.headers)
            return r
        elif self.method == 'delete':
            r = requests.delete(self.url, timeout=self.timeout,headers=self.headers)
            return r
        else:
            print('%s is error.' % self.method)

    def get_code(self):
        # 获取返回接口的状态码
        code = self.api_request().status_code
        return code

    def get_json(self):
        # 获取返回信息json数据
        json_data = self.api_request().json()
        return json_data


if __name__ == "__main__":
    pass