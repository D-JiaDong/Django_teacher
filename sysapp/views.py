from django.shortcuts import render
from dao.userdao import UserDao
import os

# Create your views here.
def getUserList(request):
    # 获取查询条件
    userName = request.POST.get('userName', '')
    userPhone = request.POST.get('userPhone', '')
    userState = request.POST.get('userState', '')
    userId = request.POST.get('userId', '')
    opr = request.POST.get('opr', '')
    pageSize = request.POST.get('pageSize', 0)
    currentPage = request.POST.get('currentPage', 0)

    if pageSize == 0 or pageSize == "":
        pageSize = 10
        pass
    if currentPage == 0 or currentPage == "":
        currentPage = 1
        pass

    userDao = UserDao()

    params = {'userName': userName,
              'userPhone': userPhone,
              'userState': userState,
              'pageSize': int(pageSize),
              'currentPage': int(currentPage) }

    if opr == 'delUser':

        result = userDao.removeUser([userId])
        params['result'] = result
        pass

    # 查询用户的个人信息
    if opr == 'update':
        uUser = userDao.findUserByUserId([userId])
        return render(request, 'admin/sysmgr/updateuser.html', {'params': params, 'uUser': uUser})
        pass

    # 提交修改用户的个人信息
    if opr == 'submitUpdate':
        userIntro = request.POST.get('userIntro', '')
        userPicPath = ""
        # 文件上传
        if request.POST:
            fileObj = request.FILES.get('userPic', None)
            # 将文件保存到本地
            if fileObj:
                userPicPath = '/static/upload/' + fileObj.name
                filePath = os.path.join(os.getcwd(), 'static/upload/' + fileObj.name)
                with open(filePath, 'wb+') as fp:
                    for chunk in fileObj.chunks():
                        fp.write(chunk)
                        pass
                    pass
                pass
            pass
        result = userDao.updateUser([userPhone, userPicPath, userIntro, userId])
        pass

    counts = userDao.findUserCounts(params)
    totalPage = counts // int(pageSize) if counts % int(pageSize) == 0 else counts // int(pageSize) + 1
    params['counts'] = counts
    params['totalPage'] = totalPage
    # 计算两个值：startRow
    startRow = (int(currentPage) - 1) * int(pageSize)
    params['startRow'] = startRow
    userList = userDao.findPageUserList(params)
    userDao.close()
    return render(request, 'admin/sysmgr/userinfo.html', {'userList': userList, 'params': params})
    pass