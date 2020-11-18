"""
测试前置和后置
模块级（每个模块执行一次）和函数级（每个函数执行一次）通常一起使用。
1、测试前置、后置名字不能写错，pytest是通过名字来识别前置和后置的
2、不够灵活，比如test_001期望执行前置，但是test_002不期望执行前置，只能分开成两个文件
"""
def setup_module():
    print("测试前置：登录系统")

def teardown_module():
    print("测试后置：退出登录系统")

def setup_function():# 使用setup一样的效果
    print("测试前置：每个函数执行一次")

def teardown_function():# 使用teardown一样的效果
    print("测试后置：每个函数执行一次")

def test_001():
    print("测试充值功能的用例1")

def test_002():
    print("测试充值功能的用例2")

def test_003():
    print("测试充值功能的用例3")


