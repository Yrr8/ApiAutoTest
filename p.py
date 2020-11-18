import requests
from unittest import mock

'''
class Quxian:
    def quxian(self, data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/withdraw",data=data).json()
        return r

    def chongzhi(self,data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/recharge",data=data).json()
        return r


class TestQuxian:
    def test_quxian(self):
        q = Quxian()
        data = {"mobilephone":"18012345678","amount":"1000"}
        r = q.chongzhi(data)
        assert r["status"] == 1
        assert r["code"] == '10001'

        # q.quxian = mock.Mock(return_value={'status': 1, 'code': '10001', 'data': None, 'msg': '取现成功'})
        data = {"mobilephone":"18012345678","amount":"100"}
        s = q.quxian(data)
        assert s["status"] == 1
        assert s["code"] == '10001'
'''
r = requests.post("http://jy001:8081/futureloan/mvc/api/member/recharge",data={"mobilephone":"13838383838",'amount':0})
print(r.json())