from django.shortcuts import render, HttpResponse
import json
from dao.blogclassdao import BlogClassDao
from dbmodels.models import TBlog, TBlogclass, TUser
# Create your views here.

def goBlogClass(request):
    return render(request, 'admin/blog/blogclass.html')
    pass

def getBlogClass(request):
    dictObj = json.loads(request.body.decode('utf-8'))  # {'classid':1, 'className': 'Python', 'opr':'del'}

    # 获取查询条件
    className = dictObj.get('className', '')
    classState = dictObj.get('classState', '')
    classId = dictObj.get('classId', '')
    opr = dictObj.get('opr', '')
    pageSize = dictObj.get('pageSize', 0)
    currentPage = dictObj.get('currentPage', 0)

    if pageSize == 0 or pageSize == "":
        pageSize = 10
        pass
    if currentPage == 0 or currentPage == "":
        currentPage = 1
        pass

    classDao = BlogClassDao()

    params = {'className': className,
              'classState': classState,
              'pageSize': int(pageSize),
              'currentPage': int(currentPage)}

    if opr == 'delClass':
        result = classDao.removeClass([classId])
        params['result'] = result
        pass

    # 查询用户的个人信息
    if opr == 'update':
        uClass = classDao.findClassByClassId([classId])
        return HttpResponse(json.dumps({'params': params, 'uClass': uClass}), content_type='application/json')
        pass

    # 提交修改用户的个人信息
    if opr == 'submitUpdate':
        uName = dictObj.get('uName', '')
        result = classDao.updateClass([uName, classId])
        pass

    if opr == 'add':
        aName = dictObj.get('aName', '')
        result = classDao.createClass([aName])
        pass

    counts = classDao.findClassCounts(params)
    totalPage = counts // int(pageSize) if counts % int(pageSize) == 0 else counts // int(pageSize) + 1
    params['counts'] = counts
    params['totalPage'] = totalPage
    currentPage = int(currentPage) if int(currentPage) < totalPage else totalPage
    currentPage = 1 if currentPage <= 0 else currentPage
    params['currentPage'] = currentPage
    # 计算两个值：startRow
    startRow = (int(currentPage) - 1) * int(pageSize)
    params['startRow'] = startRow
    classList = classDao.findPageClassList(params)
    classDao.close()

    return HttpResponse(json.dumps({'data': classList, 'params': params}), content_type='application/json')
    pass

# 博客管理
def goBlogList(request):
    return render(request, 'admin/blog/blog.html')
    pass

# AJAX异步技术实现CRUD
def blogList(request):
    dictObj = json.loads(request.body.decode('utf-8')) # {'classid':1, 'className': 'Python', 'opr':'del'}

    # 获取查询条件
    blogTitle = dictObj.get('blogTitle', '')
    blogState = dictObj.get('blogState', '')
    blogContent = dictObj.get('blogContent', '')
    blogTips = dictObj.get('blogTips', '')
    blogClassId = dictObj.get('blogClassId', '')
    blogId = dictObj.get('blogId', '')
    opr = dictObj.get('opr', '')
    pageSize = dictObj.get('pageSize', 0)
    currentPage = dictObj.get('currentPage', 0)

    if pageSize == 0 or pageSize == "":
        pageSize = 10
        pass
    if currentPage == 0 or currentPage == "":
        currentPage = 1
        pass

    tBlog = TBlog()

    blogClassDao = BlogClassDao()
    blogClassList = blogClassDao.findAllClassList()

    params = {'blogTitle': blogTitle,
              'blogState': blogState,
              'pageSize': int(pageSize),
              'currentPage': int(currentPage),
              'blogClassList': blogClassList}

    if opr == 'goAdd':
        return HttpResponse(json.dumps({'params': params}), content_type='application/json')
        pass

    # ORM实现删除功能
    if opr == 'delClass':
        tBlog.blogid = blogId    # 将id赋值为tBlog模型对象
        result = tBlog.delete()  #  delete from t_blog where blogid=blogId
        params['result'] = result
        pass

    # 查询博客信息 ORM映射框架区分大小写
    if opr == 'update':
        uBlog = TBlog.objects.filter(blogid=blogId).values('blogid', 'blogtitle', 'blogcontent', 'blogtips', 'classid')
        # select blogid, blogtitle, blogcontent, blogtips from t_blog where blogid=1
        # [{blogid:1, blogtitle:xxxxx}]
        return HttpResponse(json.dumps({'params': params, 'uBlog': uBlog[0]}), content_type='application/json')
        pass

    # 提交修改博客信息
    if opr == 'submitUpdate':
        tBlogclass = TBlogclass()
        tBlogclass.classid = int(blogClassId)

        # 摘要信息
        blogsummary = blogContent[0:300].replace('<p>', '')
        blogsummary = blogsummary.replace('</p>', '')

        result = TBlog.objects.filter(blogid=blogId).update(blogtitle=blogTitle,
                                                            blogcontent=blogContent,
                                                            blogtips=blogTips,
                                                            blogsummary=blogsummary,
                                                            classid=tBlogclass,
                                                            blogstate=blogState)
        if result:
            return HttpResponse(json.dumps({'result': 1}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'result': 0}), content_type='application/json')
            pass

        pass

    if opr == 'publish' or opr == 'cancel':
        result = TBlog.objects.filter(blogid=blogId).update(blogstate=blogState)
        pass

    if opr == 'add':
        # 是类别信息
        tBlogclass = TBlogclass()
        tBlogclass.classid = int(blogClassId)

        # 摘要信息
        blogsummary = blogContent[0:300].replace('<p>', '')
        blogsummary = blogsummary.replace('</p>', '')

        # 用户信息
        tUser = TUser()
        sessionUser = request.session['user']
        tUser.userid = sessionUser['userId']

        # ORM框架的外键列必须传对象
        result = TBlog.objects.create(blogtitle=blogTitle,
                                      blogcontent = blogContent,
                                      blogtips = blogTips,
                                      blogsummary = blogsummary,
                                      classid = tBlogclass,
                                      userid =tUser,
                                      blogstate=blogState)
        if result:
            return HttpResponse(json.dumps({'result': 1}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'result': 0}), content_type='application/json')
            pass
        pass

    querySet = TBlog.objects
    if blogTitle:
        querySet = querySet.filter(blogtitle__contains=blogTitle) # where blogtitle like %dddd%
        pass
    if blogState:
        querySet = querySet.filter(blogstate=blogState)           # where blogtitle like %dddd%  and blogstate=1
        pass

    # 计算两个值：startRow
    startRow = (int(currentPage) - 1) * int(pageSize)
    endRow = int(currentPage)* int(pageSize)
    params['startRow'] = startRow

    # 多表联查
    blogList = list(querySet.values('blogid',
                                    'blogtitle',
                                    'blogsummary',
                                    'blogtips',
                                    'userid__username',
                                    'classid__classname',
                                    'blogstate')[startRow: endRow])
    counts = querySet.count()
    totalPage = counts // int(pageSize) if counts % int(pageSize) == 0 else counts // int(pageSize) + 1
    params['counts'] = counts
    params['totalPage'] = totalPage
    currentPage = int(currentPage) if int(currentPage)<totalPage else totalPage
    currentPage = 1 if currentPage <= 0 else currentPage
    params['currentPage'] = currentPage

    return HttpResponse(json.dumps({'data': blogList, 'params': params}), content_type='application/json')
    pass

def goWriteBlog(request):
    return render(request, 'admin/blog/writeblog.html')
    pass

def goUpdateBlog(request):
    blogId = request.GET.get('blogId', 0)
    params = {}
    params['blogId'] = blogId
    return render(request, 'admin/blog/updateblog.html', {'params': params})
    pass

import jieba
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def viewBlog(request):
    blogId = request.GET.get('blogId', 0)
    uBlog = TBlog.objects.filter(blogid=blogId).values('blogid', 'blogtitle', 'blogcontent', 'blogtips', 'classid', 'classid__classname')

    if uBlog:
        uBlog = uBlog[0]
    # 加入基于内容的推荐功能
    # 1.查找最近的100篇同类型的博客
    blogList = list(TBlog.objects.filter(classid=uBlog['classid']).values('blogid', 'blogtitle', 'blogcontent',  'blogsummary', 'blogtips', 'classid', 'classid__classname')[0:100])

    content = uBlog['blogcontent']
    content = content.replace('<p>', '')
    content = content.replace('</p>', '')

    contentList = []
    contentList.append(' '.join(jieba.cut(content))) # 我是中国人['我','是','中国人']  -> 我 是  中国人
    # 分词
    for ct in blogList:
        cc = ct['blogcontent']
        cc = cc.replace('<p>', '')
        cc = cc.replace('</p>', '')
        contentList.append(' '.join(jieba.cut(cc)))
        pass

    vectorizer = CountVectorizer()

    # 传入词库，用于统计词库和词数
    tf = vectorizer.fit_transform(contentList)

    # 得到词库。词汇表
    words = vectorizer.get_feature_names()
    print(words)

    # 查看词频统计
    print(tf.toarray())  #

    tfidfTransformer = TfidfTransformer()

    # 计算tf-idf
    tfidf = tfidfTransformer.fit_transform(tf)
    # 查看每句话的tf-idf值
    print(tfidf.toarray())

    from sklearn.metrics.pairwise import linear_kernel

    # 通过向量的余弦相似度，计算出第一个文本和所有其他文本之间的相似度（注意此处包含了自己）
    cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten()
    print(cosine_similarities)

    similarList = []
    for i in range(1, len(cosine_similarities)):
        if cosine_similarities[i] > 0.3 and blogList[i - 1]['blogid'] != int(blogId):
            similarList.append(blogList[i - 1])
            pass
        pass
    # 作业：排序

    return render(request, 'user/viewblog.html', {'uBlog': uBlog, 'similarList': similarList})
    pass

import os
import uuid
# 文件上传功能
def uploadFile(request):
    # 后缀需要检查的
    file = request.FILES.get('upload')
    if file:
        fileName = str(uuid.uuid4()) +  file.name # 避免文件名称冲突
        try:
            with open(os.path.dirname(__file__) + os.sep + '..' + os.sep + 'static' + os.sep + 'upload'+ os.sep + fileName, "wb+") as fp:
                for chunk in file.chunks():
                    fp.write(chunk)
                    pass
        except Exception as e:
            return HttpResponse(json.dumps({'uploaded': 0, 'fileName': "", 'url': ""}), content_type="application/json")
            pass
        return  HttpResponse(json.dumps({'uploaded': 1, 'fileName':fileName, 'url': os.sep + 'static' + os.sep + 'upload'+ os.sep + fileName}), content_type="application/json")
    else:
        return  HttpResponse(json.dumps({'uploaded': 0, 'fileName': "", 'url': ""}), content_type="application/json")
    pass

