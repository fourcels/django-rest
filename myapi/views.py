from django.shortcuts import render
from .serializers import HeroSerializer, QuestionSerializer
from .models import Hero, Question
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    """
    create:
    创建项目
    retrieve:
    获取项目详情数据
    update:
    完整更新项目
    partial_update:
    部分更新项目
    destroy:
    删除项目
    list:
    获取项目列表数据
    """
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    """
    create:
    创建项目
    retrieve:
    获取项目详情数据
    update:
    完整更新项目
    partial_update:
    部分更新项目
    destroy:
    删除项目
    list:
    获取项目列表数据
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
