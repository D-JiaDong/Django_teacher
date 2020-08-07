# 封装数据库访问的底层结构
import pymysql # 引入库
import json
import os

class BaseDao():
    def __init__(self, configfile='mysql.json'):
        self.config = json.load(open(os.path.dirname(__file__) + os.sep + configfile)) # dict
        self.connection = None
        self.cursor = None
        pass

    def getConnection(self):
        '''
        通用的创建数据库并返回数据库连接的方法
        :return:数据库连接
        '''
        if self.connection != None:
            return self.connection
            pass
        try:
            self.connection = pymysql.connect(** self.config)
            self.connection.autocommit(0)
        except Exception as e:
            print("数据库连接失败，请检查配置参数")
            pass
        print("数据库连接成功！")
        return self.connection
        pass

    def execute(self, sql, params =None): # SQL注入问题，参数化的方法
        '''
        封装执行语句的方法
        :param sql: 语句
        :param params: 参数列表
        :return:
        '''
        result = 0
        try:
            self.cursor = self.getConnection().cursor(cursor=pymysql.cursors.DictCursor)
            if params:  # == if params != None: if None: == False
                result = self.cursor.execute(sql, params)
                pass
            else:
                result = self.cursor.execute(sql)
        except Exception as e:
            print(e)
            pass
        return result
        pass

    # 封装读取数据集的功能
    def fetch(self):
        if self.cursor:
            return self.cursor.fetchall()
            pass
        pass

    # 处理事务管理
    def commit(self):
        if self.connection:
            self.connection.commit()
        pass

    def rollback(self):
        if self.connection:
            self.connection.rollback()
        pass

    def close(self):
        if self.connection:
            self.connection.close()
            pass
        pass
    pass


