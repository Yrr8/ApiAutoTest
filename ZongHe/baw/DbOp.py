"""
数据库操作
"""
from ZongHe.caw import MysqlOp


def deleteUser(db, phone):
    """
    根据手机号删除用户
    :param db: 一个字典，存储数据库信息
    :param phone: 手机号
    :return:
    """
    conn = MysqlOp.connect(db)
    MysqlOp.execute(conn, f'delete from Member where MobilePhone = {phone};')
    MysqlOp.disconnect(conn)


def selectAmount(db, phone):
    pass
