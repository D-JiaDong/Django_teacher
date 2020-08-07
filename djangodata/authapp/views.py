from django.shortcuts import render, redirect, HttpResponse
import os
from dao.userdao import UserDao
import hashlib

# Create your views here.
# 作为整个网站的入口
def index(request):
    return render(request, 'index.html')

# 跳转登录页面
def goLogin(request):
    return render(request, 'admin/login.html')

# 跳转注册页面
def goNewUser(request):
    return render(request, 'newuser.html')

def goIndex(request):
    return render(request, 'admin/index.html')
    pass

# 用户注册
def regNewUser(request):
    # 普通的表单项
    userName = request.POST.get('userName', '')
    userPwd = request.POST.get('userPwd', '')
    userPhone = request.POST.get('userPhone', '')
    userIntro = request.POST.get('userIntro', '')
    userPicPath = ""  # 保存路径

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
    # 对用户的密码加密存储
    userPwd = hashlib.md5(userPwd.encode(encoding='utf-8')).hexdigest()

    userDao = UserDao()
    # 将用户的个人信息写入数据库
    result = userDao.createUser([userName, userPwd, userPhone, userPicPath, userIntro])
    userDao.commit()
    userDao.close()
    # 如果写入成功，跳转到登录页
    if result > 0:
        return render(request, 'login.html', {'success': 1})
        pass
    else:
        return render(request, 'newuser.html', {'success': 0})
        pass
    pass

import json

def checkUserName(request):
    dictObj = json.loads(request.body.decode('utf-8'))  # {'userName': 'zhangsan'}
    userName = dictObj['userName']
    userDao = UserDao()
    result = userDao.findUserByUserName([userName])
    userDao.close()
    rDict = {}
    if result:
        rDict['result'] = 1
        pass
    else:
        rDict['result'] = 0
    # {'result':1}
    return HttpResponse(json.dumps(rDict), content_type='application/json')
    pass

def login(request):

    userName = request.POST.get('userName', '')
    userPwd = request.POST.get('userPwd', '')
    rememberMe = request.POST.get('rememberMe', '')

    userPwd = hashlib.md5(userPwd.encode(encoding='utf-8')).hexdigest()
    userDao = UserDao()

    result = userDao.loginParams([userName, userPwd])
    if result:
        user = {}
        user['userName'] = userName
        user['userId']   = result[0]['userid']
        user['userPic']  = result[0]['userpic']
        request.session['user'] = user
        return render(request, 'admin/index.html')
        pass
    else:
        return redirect('/login/')
        pass

    pass