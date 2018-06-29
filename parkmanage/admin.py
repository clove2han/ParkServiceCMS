#_*_coding:utf-8_*_

from django.contrib import admin
from .models import Employee,Parkinfo
# Register your models here.
class ParkinfoInline(admin.StackedInline):
    model = Parkinfo

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id','employee_name','position','state','create_time')
    inlines = [ParkinfoInline, ]
#先导入Employee类，通过admain.site.register注册。
admin.site.register(Employee,EmployeeAdmin)

class ParkinfoAdmin(admin.ModelAdmin):
    #list_display = ('park_id','park_name','country','province','city','district','area','address','director','construction_time','actieve_time','remark')
    list_display = ('park_id','park_name','country','province','city','district','address','park_type','property','Property_contact','Property_tele','space_number','carriage_way','director','construction_time','using_time','watch_man','train_man','remark')
    search_fields = ('park_name',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(ParkinfoAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct

    def save_model(self, request, obj, form, change):
        if change:  # 更改的时候
            obj_original = self.model.objects.get(pk=obj.pk)
        else:  # 新增的时候
            obj_original = None
        obj.user = request.user
        obj.save()

admin.site.register(Parkinfo, ParkinfoAdmin)