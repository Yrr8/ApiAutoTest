"""
脚本层的公共方法
"""
import pytest

from ZongHe.baw import DbOp
from ZongHe.caw import DataRead, Member
from ZongHe.caw.BaseRequests import BaseRequests


# 从环境文件里面读取url
@pytest.fixture(scope='session')
def url():
    return DataRead.readini("ZongHe/data_env/env.ini", "url")


# 从环境文件里面读取db
@pytest.fixture(scope='session')
def db():
    # 从ini文件中读取出来是字符串，将字符串转成字典，使用eval函数
    return eval(DataRead.readini("ZongHe/data_env/env.ini", "db"))


# 创建BaseRequests的一个实例
@pytest.fixture(scope='session')
def baserquests():
    return BaseRequests()



