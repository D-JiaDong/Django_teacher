from django.contrib import admin

# Register your models here.
from dbmodels.models import TBlog
from dbmodels.models import TBlogclass
from dbmodels.models import TUser

admin.site.register(TBlog)
admin.site.register(TBlogclass)
admin.site.register(TUser)