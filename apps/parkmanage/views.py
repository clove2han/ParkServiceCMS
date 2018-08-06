#_*_coding:utf-8_*_

from django.shortcuts import render_to_response,render,redirect
from django.views.decorators.csrf import csrf_exempt
from models import Parkinfo,Employee,Book
from django.template import RequestContext
from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from pagination import Pagination

import json

@csrf_exempt
def index(request):
    staffinfo = Employee.objects.filter(position__in=['线下运维',])
    # park_num = Parkinfo.objects.count()
    # PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return render_to_response('parkmanage/index.html', {'staffs': staffinfo})

def employeeinfo(request):
    employee_list = Employee.objects.order_by('employee_id')


    return render_to_response('parkmanage/employeeinfo.html',{'employee_list':employee_list})

def login(request):
    # 包含用户提交的所有信息
    # 获取用户提交方法
    error_msg = ""
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username is not None and password is not None:
            user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)

            return redirect('parkmanage/index.html')
        else:
            return render(request,'parkmanage/login.html', {'error_msg': '用户名或密码错误!'})

    return render(request,'parkmanage/login.html', {'error_msg': error_msg})

def parkinfo(request):
    # 获取parkinfo数据表中的所有记录
    park_lists = Parkinfo.objects.order_by('park_id')

    current_page = request.GET.get('p')

    count = Parkinfo.objects.all().count()

    page_obj =Pagination(current_page,count,page_url="parkmanage/parkinfo.html")

    data_list = park_lists[page_obj.start_page_item():page_obj.end_page_item()]

    return render_to_response('parkmanage/parkinfo.html',{'parklists':data_list,'page_obj':page_obj})


def test(request):
    parkinfo = Parkinfo.objects.order_by('park_id')


    return render_to_response('parkmanage/test.html',{'parklists':parkinfo})


@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name = request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception,e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", books))

        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception,e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)