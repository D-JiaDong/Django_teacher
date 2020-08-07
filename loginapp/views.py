from django.shortcuts import render
from dao.userdao import UserDao

# Create your views here.
# 基于数据的登录
def userLogin(request):
    userName = request.POST.get('userName', '')
    userPwd = request.POST.get('userPwd', '')

    userDao = UserDao()
    result = userDao.loginParams([userName, userPwd])

    if result:
        user = {}
        user['userName'] = userName
        request.session['user'] = user
        return render(request, 'main1.html')
        pass
    else:
        return render(request, 'index.html')
        pass
    pass