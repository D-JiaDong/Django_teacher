from dao.basedao import BaseDao
import time

class UserDao(BaseDao):

    # 参数化
    def loginParams(self, params=[]):
        sql = "select * from t_user where username=%s and userpwd=%s" # %s是占位符
        self.execute(sql, params)
        resultSet = self.fetch()
        return resultSet
        pass

    def findUserByUserName(self, params=[]):
        sql = "select * from t_user where username=%s"  # %s是占位符
        self.execute(sql, params)
        resultSet = self.fetch()
        return resultSet
        pass

    def createUser(self, params=[]):
        sql = "insert into t_user (username, userpwd, userphone, userpic, userintro) " \
              "values(%s, %s, %s, %s,%s)"
        result = self.execute(sql, params)
        return result
        pass

    def updateUserMoney(self, params):
        sql = "update t_user set usermoney=usermoney+%s where userid=%s"
        result = self.execute(sql, params)
        return result
        pass

    def findPageUserList(self, params={}):
        sql = "select * from t_user where 1=1 "  # %s是占位符
        searchParams = []
        if params.get('userName'):
            sql += ' and userName like %s'
            searchParams.append('%' +params.get('userName') + "%")
            pass
        if params.get('userPhone'):
            sql += ' and userPhone like %s'
            searchParams.append('%'+ params.get('userPhone') + '%')
            pass
        if params.get('userState'):
            sql += ' and userState=%s'
            searchParams.append(params.get('userState'))
            pass

        sql += " limit " + str(params.get('startRow')) + ', ' + str(params.get('pageSize'))

        print(sql)
        self.execute(sql, searchParams)   #
        resultSet = self.fetch()
        return resultSet
        pass

    def findUserCounts(self, params):
        sql = "select count(*) as counts from t_user where 1=1 "  # %s是占位符
        searchParams = []
        if params.get('userName'):
            sql += ' and userName like %s'
            searchParams.append('%' + params.get('userName') + "%")
            pass
        if params.get('userPhone'):
            sql += ' and userPhone like %s'
            searchParams.append('%' + params.get('userPhone') + '%')
            pass
        if params.get('userState'):
            sql += ' and userState=%s'
            searchParams.append(params.get('userState'))
            pass
        print(sql)
        self.execute(sql, searchParams)  #
        resultSet = self.fetch()
        return resultSet[0]['counts']
        pass

    def removeUser(self, params):
        sql = "delete from t_user where userid=%s "  # %s是占位符
        result = self.execute(sql, params)  #
        self.commit()
        return result
        pass

    def findUserByUserId(self, params):
        sql = "select * from t_user where userid=%s"  # %s是占位符
        self.execute(sql, params)
        resultSet = self.fetch()
        return resultSet[0]
        pass

    def updateUser(self, params):
        sql = "update t_user set userphone=%s, userpic=%s, userintro=%s where userid=%s"  # %s是占位符
        result = self.execute(sql, params)
        self.commit()
        return result
        pass
    pass
