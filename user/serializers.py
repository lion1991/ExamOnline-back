from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import Student, Department
    # , MenuInfo, MetaInfo, RolesInfo, StaffMenu, MenuChildren, MetaChildrenInfo


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class RolesInfoSerializer(serializers.Serializer):
    # roles = serializers.StringRelatedField(many=True, read_only=False)
    sys = serializers.CharField (max_length=32)
    # class Meta:
    #     model = RolesInfo
    #     # fields = '__all__'
    #     fields = ('name')

class UserRolesInfoSerializer(serializers.Serializer):
    # roles = serializers.StringRelatedField(many=True, read_only=False)
    roles = serializers.CharField (max_length=32)

# class MetaChildrenInfoSerializer(serializers.ModelSerializer):
#     # roles = serializers.StringRelatedField(many=True, read_only=False)
#     # roles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     # roles = serializers.ReadOnlyField(source="roles.name")
#     # roles = RolesInfoSerializer(many=True)
#     roles = serializers.StringRelatedField(many=True, read_only=False)
#     class Meta:
#         model = MetaChildrenInfo
#         # fields = '__all__'
#         fields = ('title', 'icon', 'roles')

# class MetaInfoSerializer(serializers.ModelSerializer):
#     # roles = serializers.StringRelatedField(many=True, read_only=False)
#     # roles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     # roles = serializers.ReadOnlyField(source="roles.name")
#     # roles = RolesInfoSerializer(many=True)
#     roles = serializers.StringRelatedField(many=True, read_only=False)
#
#     class Meta:
#         model = MetaInfo
#         # fields = '__all__'
#         fields = ('title', 'icon', 'roles')


# class MenuChildrenSerializer(serializers.ModelSerializer):
#     meta = MetaChildrenInfoSerializer()
#     class Meta:
#         model = MenuChildren
#         fields = ('meta', 'path', 'component', 'alwaysShow', 'name')
#         # fields = '__all__'
#
# class MenuInfoSerializer(serializers.Serializer):
#     meta = MetaInfoSerializer()
#     path = serializers.CharField(max_length=32)
#     component = serializers.CharField(max_length=32)
#     alwaysShow = serializers.BooleanField()
#     name = serializers.CharField(max_length=32)
#     # menuchildren_set1 = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
#     children = MenuChildrenSerializer(many=True)
#     #
#     # class Meta:
#     #     model = MenuInfo
#     #     fields = ('meta', 'path', 'component', 'alwaysShow', 'name', 'children', 'menuinfo_set')

# class StaffMenuSerializer(serializers.Serializer):
#     menu = MenuInfoSerializer()
#     # children = MenuChildrenSerializer()
#     # class Meta:
#     #     model = StaffMenu
#     #     # fields = '__all__'
#     #     fields = ('menu',)

class StudentSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 只读
    # user = UserDetailSerializer()
    # clazz = ClazzSerializer(read_only=True)
    # menu = MenuInfoSerializer()
    # 用于创建的只写字段
    roles = serializers.StringRelatedField(many=True, read_only=False)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source='department', write_only=True)

    class Meta:
        model = Student
        fields = '__all__'
        # fields = ('roles','department_id',)



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
