from dao.basedao import BaseDao
import time

class BlogClassDao(BaseDao):

    def findClassByClassName(self, params=[]):
        sql = "select * from t_blogclass where classname=%s"  # %s是占位符
        self.execute(sql, params)
        resultSet = self.fetch()
        return resultSet
        pass

    def createClass(self, params=[]):
        sql = "insert into t_blogclass (classname) " \
              "values(%s)"
        result = self.execute(sql, params)
        self.commit()
        return result
        pass

    def findPageClassList(self, params={}):
        sql = "select * from t_blogclass where 1=1 "  # %s是占位符
        searchParams = []
        if params.get('className'):
            sql += ' and className like %s'
            searchParams.append('%' +params.get('className') + "%")
            pass

        sql += " limit " + str(params.get('startRow')) + ', ' + str(params.get('pageSize'))

        print(sql)
        self.execute(sql, searchParams)   #
        resultSet = self.fetch()
        return resultSet
        pass

    def findAllClassList(self, params={}):
        sql = "select * from t_blogclass where 1=1 "  # %s是占位符
        searchParams = []
        if params.get('className'):
            sql += ' and className like %s'
            searchParams.append('%' + params.get('className') + "%")
            pass

        self.execute(sql, searchParams)  #
        resultSet = self.fetch()
        return resultSet
        pass

    def findClassCounts(self, params):
        sql = "select count(*) as counts from t_blogclass where 1=1 "  # %s是占位符
        searchParams = []
        if params.get('className'):
            sql += ' and className like %s'
            searchParams.append('%' + params.get('className') + "%")
            pass

        print(sql)
        self.execute(sql, searchParams)  #
        resultSet = self.fetch()
        return resultSet[0]['counts']
        pass

    def removeClass(self, params):
        sql = "delete from t_blogclass where classid=%s "  # %s是占位符
        result = self.execute(sql, params)  #
        self.commit()
        return result
        pass

    def findClassByClassId(self, params):
        sql = "select * from t_blogclass where classid=%s"  # %s是占位符
        self.execute(sql, params)
        resultSet = self.fetch()
        return resultSet[0]
        pass

    def updateClass(self, params):
        sql = "update t_blogclass set className=%s where classid=%s"  # %s是占位符
        result = self.execute(sql, params)
        self.commit()
        return result
        pass
    pass
