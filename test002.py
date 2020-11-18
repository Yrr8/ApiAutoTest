"""
测试前置和后置
类和方法级别
"""

class Test002:

    def setup_class(self):
        print("测试前置：类里的方法前执行调用")

    def teardown_class(self):
        print("测试后置：类里的方法后执行调用")

    def setup_method(self):# 使用setup一样效果
        print("每个方法前执行")

    def teardown_method(self):# 使用teardown一样效果
        print("每个方法后执行")

    def test_001(self):
        print("用例1")

    def test_002(self):
        print("用例2")
