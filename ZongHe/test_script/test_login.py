"""
登录的测试脚本
"""

import pytest

from ZongHe.baw import DbOp
from ZongHe.caw import DataRead, Member


# 获取测试数据
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_setup.yaml"))
def setup_data(request):
    return request.param


# 测试前置和后置
@pytest.fixture()
def register(url, baserquests, setup_data, db):
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    Member.register(url, baserquests, setup_data['casedata'])
    yield
    DbOp.deleteUser(db,phone)


def test_pass(url, baserquests, login_data,register):

    print(f"测试数据为：{login_data['casedata']}")
    print(f"期望结果为：{login_data['expect']}")
    r = Member.login(url, baserquests, login_data['casedata']).json()
    assert r['status'] == login_data['expect']['status']
    assert r['code'] == login_data['expect']['code']
    assert r['msg'] == login_data['expect']['msg']
