# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import UserDepartment,UserPosition
# Create your views here.

from rest_framework import viewsets
from serializers import UserDepartmentSerializer
from rest_framework.decorators import detail_route,list_route
from rest_framework.response import Response


class UserDepartmentViewSet(viewsets.ModelViewSet):
    queryset = UserDepartment.objects.all()
    serializer_class = UserDepartmentSerializer

    ##############################################################
    # 添加部门信息
    ##############################################################
    @detail_route()
    def add_department(self, request, *args, **kwargs):
        result = request.GET
        # user_department = self.get_object()
        user_department = ''
        user_department.department_id = result.get('department_id')
        user_department.name = result.get('name')
        user_department.desc = result.get('desc')

        user_department.save()
        return Response({"result": 1, "msg": "添加成功"})


    ##############################################################
    #修改部门信息
    ##############################################################
    @detail_route()
    def changeName(self,request,*arfs,**kwargs):
        get = request.GET
        user_department= self.get_object()
        user_department.name = get.get('name')
        user_department.desc = get.get('desc')
        user_department.save()
        return Response({"result":1,"msg":"修改成功"})


    @list_route()
    def filterUserDepartment(self,request):
        user_departments = UserDepartment.objects.filter(self,request)
        serializer = UserDepartmentSerializer(user_departments,many=True)

        return Response(serializer.data)