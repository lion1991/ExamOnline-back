from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from rest_framework import viewsets, mixins, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend

from user.genericsview import ReListView
from user.models import Student, Department, Department
    #, MenuInfo, StaffMenu
from user.serializers import StudentSerializer, UserDetailSerializer, DepartmentSerializer, MyTokenObtainPairSerializer, \
    DepartmentSerializer\
    #, MenuInfoSerializer, StaffMenuSerializer


# Create your views here.
# class CustomBackend(ModelBackend):
#     """
#     自定义用户验证
#     """
#
#     def authenticate(self, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(Q(username=username) | Q(mobile=username))
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None
#
#
# def jwt_response_payload_handler(token, user=None, request=None):
#     """
#     设置jwt登录之后返回token和user信息
#     """
#     student = Student.objects.get(user=user)
#     return {
#         'token': token,
#         'user': UserDetailSerializer(user, context={'request': request}).data,
#         'student': StudentSerializer(student, context={'request': request}).data
#     }

class MyObtainTokenPairView(TokenObtainPairView):
    # permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = []
    permission_classes = []
    """
    用户注册
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.data['username'])
        if user:
            return Response({'msg': '用户名已存在'}, status=status.HTTP_201_CREATED)
        user_detail = UserDetailSerializer(data=request.data)
        if user_detail.is_valid():
            user_detail.save()
        user = User.objects.get(username=request.data['username'])
        # 密码转成密文存储
        user.password = make_password(user.password)
        user.save()
        student = Student(user=user, name=request.data['name'])
        if student:
            student.save()
        return Response(user_detail.errors)


class UpdatePwdApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    """
    修改用户密码
    """

    def patch(self, request):
        # 获取参数
        old_pwd = request.data['oldpwd']
        new_pwd = request.data['newpwd']
        user_id = request.data['userid']
        # 获得请求用户
        user = User.objects.get(id=user_id)
        # 检查原始密码是否正确
        if user.check_password(old_pwd):
            user.set_password(new_pwd)
            user.save()
        else:
            return Response(data={'msg': 'fail'}, status=status.HTTP_200_OK)
        # 返回数据
        return Response(data={'msg': 'success'}, status=status.HTTP_200_OK)


class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    """
    用户信息
    """
    # 查询集
    queryset = Student.objects.all().order_by('id')
    # 序列化
    serializer_class = StudentSerializer

class DepartmentListViewSet(viewsets.ModelViewSet):
    """
    部门信息
    """
    # 查询集
    queryset = Department.objects.all().order_by('id')
    # 序列化
    serializer_class = DepartmentSerializer


class QueryUserView(GenericAPIView):
    # authentication_classes = [JWTAuthentication]
    authentication_classes = []
    # permission_classes = [IsAuthenticated]
    permission_classes = []
    """
    用户权限信息
    """
    filter_backends = [DjangoFilterBackend]
    queryset = Student.objects.all()  # 你要序列化的数据
    serializer_class = StudentSerializer  # 你要使用的序列化类

    def get(self, request, *args, **kwargs):
        info = self.get_object()  # 获取单条
        ser = self.get_serializer(instance=info)
        print(info)
        return Response({'data':ser.data, 'code':200, 'msg': '用户获取成功'}, status=200)

# class QueryMenuList(ReListView):
#     authentication_classes = []
#     permission_classes = []
#     queryset = GetMenu.objects.all()
#     serializer_class = GetMenuSerializer

# class QueryMenuDetail(APIView):
#     """
#     Retrieve, update or delete an article instance.
#     """
#
#     authentication_classes = []
#     permission_classes = []
#     def get_object(self, pk):
#         try:
#             return Student.objects.filter(pk=pk)
#         except StaffMenu.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         #需要借助查询多对多关系表StaffMenu的staffid字段，返回对应的Menu_id
#         #然后序列化MenuInfo的数据
#         menu = self.get_object(pk)
#         menu = self.get_object(pk)
#         a = StaffMenu.objects.filter(staff=pk).all()
#         print(a)
#         # b = a.staffmenu_set.all()
#         # b = a.staffmenu.objects()
#         # print(b)
#         # menu_obj = menu.staffmenu_set.all()
#         # print(menu_obj)
#         # menu = MenuInfo.objects.filter(b)
#         # print(menu)
#         serializer = StaffMenuSerializer(a, many=True)
#         # serializer = MenuInfoSerializer(menu, many=True)
#         print(serializer.data)
#         return Response({"msg": "菜单查询成功", "code": 200, "data": serializer.data})