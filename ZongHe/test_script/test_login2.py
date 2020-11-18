"""
测试登录功能
"""
import pytest

from ZongHe.baw import DbOp
from ZongHe.caw import DataRead, Member


@pytest.fixture(params=DataRead.readyaml('ZongHe/data_case/login_data.yaml'))
def login_data(request):
    return request.param


@pytest.fixture(params=DataRead.readyaml('ZongHe/data_case/login_setup.yaml'))
def setup_data(request):
    return request.param


# 测试前置和后置
@pytest.fixture()
def register(setup_data, url, baserquests, db):
    # 注册
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    r = Member.register(url, baserquests, setup_data['casedata'])
    yield
    # 删除注册用户
    DbOp.deleteUser(db, phone)


def test_login(login_data, url, baserquests, register):
    # 登录
    print(f"测试数据为：{login_data['casedata']}")
    print(f"期望结果为：{login_data['expect']}")
    r = Member.login(url, baserquests, login_data['casedata']).json()
    # 检查登录的结果
    assert r['status'] == login_data['expect']['status']
    assert r['code'] == login_data['expect']['code']
    assert r['msg'] == login_data['expect']['msg']
