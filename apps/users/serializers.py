from rest_framework import serializers
from .models import UserDepartment

class UserDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDepartment
        fields = ('department_id', 'name', 'desc', 'add_time')
