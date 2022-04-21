from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import Student, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 只读
    # user = UserDetailSerializer()
    # clazz = ClazzSerializer(read_only=True)

    # 用于创建的只写字段
    clazz_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source='department', write_only=True)

    class Meta:
        model = Student
        fields = '__all__'

    #创建simplejwt的自定义序列化


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['refreshtoken'] = data['refresh']
        data['access'] = str(refresh.access_token)
        data['token'] = data['access']

        # Add extra responses here
        userinfo = UserDetailSerializer(self.user).data
        studentinfo = Student.objects.get(user=self.user)  #查询student表
        student = StudentSerializer(studentinfo).data  #序列化student表
        data['user'] = userinfo
        data['student'] = student
        data['code'] = 200
        # data['username'] = self.user.username
        # data['useid'] = self.user.id
        # data['groups'] = self.user.groups.values_list('name', flat=True)
        return data
