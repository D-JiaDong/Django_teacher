# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TBlog(models.Model):
    blogid = models.AutoField(primary_key=True)
    blogtitle = models.CharField(max_length=45, blank=True, null=True)
    blogcontent = models.TextField(blank=True, null=True)
    blogtips = models.CharField(max_length=45, blank=True, null=True)
    blogdate = models.DateTimeField(blank=True, null=True)
    userid = models.ForeignKey('TUser', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    classid = models.ForeignKey('TBlogclass', models.DO_NOTHING, db_column='classid', blank=True, null=True)
    blogstate = models.IntegerField(blank=True, null=True)
    blogsummary = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_blog'


class TBlogclass(models.Model):
    classid = models.AutoField(primary_key=True)
    classname = models.CharField(unique=True, max_length=45, blank=True, null=True)
    classstate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_blogclass'


class TUser(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=45, blank=True, null=True)
    userpwd = models.CharField(max_length=512, blank=True, null=True)
    userphone = models.CharField(unique=True, max_length=45, blank=True, null=True)
    userpic = models.CharField(max_length=255, blank=True, null=True)
    userintro = models.CharField(max_length=512, blank=True, null=True)
    userstate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'
