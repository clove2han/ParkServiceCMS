# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers

from models import UserDepartment,UserPosition
# Create your views here.

@require_http_methods(["GET"])
def add_department(request):
    response = {}
    try:
        department = UserDepartment(department_name = request.GET.get('departments_name'))
        department.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception,e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_department(request):
    response = {}
    try:
        department = UserDepartment.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", department))

        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception,e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)