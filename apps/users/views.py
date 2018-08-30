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

    @detail_route()
    def changeName(self,request,*arfs,**kwargs):
        get = request.GET
        user_department= self.get_object()
        user_department.name = get.get('name')
        user_department.save()
        return Response(user_department.name)

    @list_route()
    def filterUserDepartment(self,request):
        user_departments = UserDepartment.objects.filter(self,request)
        serializer = UserDepartmentSerializer(user_departments,many=True)

        return Response(serializer.data)