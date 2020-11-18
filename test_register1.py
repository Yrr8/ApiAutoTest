import pytest, requests, openpyxl


def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r


# 获取excel中的数据
def get_excel(workbook, worksheet):
    # 获取工作簿
    book = openpyxl.load_workbook(workbook)
    # 获取工作表
    sheet = book[worksheet]
    # 获取数据


@pytest.fixture(params=[{"casedata": {"mobilephone": "12345678912", "pwd": "12345"},
                         "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
                        {"casedata": {"mobilephone": "12345678913", "pwd": "123456789qwertyuiop"},
                         "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}}])
def data(request):
    return request.param


def test_register(data):
    real = register(data["casedata"])
    assert real.json()["status"] == data["expect"]["status"]
    assert real.json()["code"] == data["expect"]["code"]
    print(f"使用{data['casedata']}注册,返回{real.json()}")
