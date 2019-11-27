import requests
from redis import Redis

red = Redis(host='localhost')
from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
# 初始化client,apikey作为所有请求的默认值


class YunPian:

    def __init__(self, api_key):
        self.api_key = api_key
        self.send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_msg(self, mobile, code):
        # 60秒内再次请求不会再发短信
        r_code = red.get(mobile)
        if r_code:
            return 'exist'
        clnt = YunpianClient(self.api_key)
        param = {
            YC.MOBILE: mobile,
            YC.TEXT: "【】您的验证码是{}。如非本人操作，请忽略本短信".format(code)
        }
        r = clnt.sms().single_send(param)
        print(r_code)
        print(r.msg())
        print(r.data())
        if str(r.msg()) == '发送成功':
            red.set(mobile, value=code, ex=60)
            return 'ok'
        else:
            return 'failed'
