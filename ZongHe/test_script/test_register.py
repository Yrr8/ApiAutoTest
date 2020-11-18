"""
注册的测试脚本（pytest）
"""
import pytest

from ZongHe.baw import DbOp
from ZongHe.caw import DataRead
from ZongHe.caw import Member


# 测试前置：获取测试数据，数据是列表，通过readyaml读取来的
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_fial.yaml"))
def fail_data(request):
    return request.param


# 注册失败
def test_register_fail(fail_data, url, baserquests):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"期望结果为：{fail_data['expect']}")
    # 发送请求
    r = Member.register(url, baserquests, fail_data['casedata']).json()
    # 检查结果
    assert r['status'] == fail_data['expect']['status']
    assert r['code'] == fail_data['expect']['code']
    assert r['msg'] == fail_data['expect']['msg']


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_pass.yaml"))
def pass_data(request):
    return request.param


# 注册成功
def test_register_pass(pass_data, url, baserquests, db):
    print(f"测试数据为：{pass_data['casedata']}")
    print(f"期望结果为：{pass_data['expect']}")
    phone = pass_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(url, baserquests, pass_data['casedata']).json()
    assert r['status'] == pass_data['expect']['status']
    assert r['code'] == pass_data['expect']['code']
    assert r['msg'] == pass_data['expect']['msg']
    # 2.检查实际有没有注册成功（1、查数据库;2、获取用户列表；3、用注册的用户登录）
    r = Member.getList(url, baserquests)
    assert phone in r.text
    # 清理环境，根据手机号删除用户
    DbOp.deleteUser(db, phone)


@pytest.fixture(params=DataRead.readyaml('ZongHe/data_case/register_repeat.yaml'))
def repeat_data(request):
    return request.param


# 重复注册
def test_register_repeat(repeat_data, url, baserquests, db):
    print(f"测试数据为：{repeat_data['casedata']}")
    print(f"期望结果为：{repeat_data['expect']}")
    phone = repeat_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(db, phone)
    # 发送注册请求
    r = Member.register(url, baserquests, repeat_data['casedata']).json()
    assert r['status'] == pass_data['expect']['status']
    assert r['code'] == pass_data['expect']['code']
    assert r['msg'] == pass_data['expect']['msg']

    # 检查实际有没有注册成功（1、查数据库;2、获取用户列表；3、用注册的用户登录）
    r = Member.getList(url, baserquests)
    assert phone in r.text
    # 再次发送注册请求
    r = Member.register(url, baserquests, repeat_data['casedata']).json()
    assert r['status'] == repeat_data['expect']['status']
    assert r['code'] == repeat_data['expect']['code']
    # 清理环境
    DbOp.deleteUser(db, phone)
