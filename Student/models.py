# -*-coding:utf-8-*-
from django.db import models


# Create your models here.
class Student(models.Model):
    '''
    The model of student.
    '''
    name = models.CharField(max_length=10)                  # 学生姓名
    age = models.PositiveIntegerField(verbose_name=0)       # 学生年龄
    gender = models.BooleanField()                          # 学生性别
    introduction = models.TextField()                       # 学生简介
    major = models.CharField(max_length=10)                 # 学生专业
    grade = models.CharField(max_length=5)                  # 学生年级
    GPA = models.FloatField(verbose_name=0)                 # 学生成绩