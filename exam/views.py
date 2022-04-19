from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from exam.filter import ExamFilter
from exam.models import Exam, Grade, Practice
from exam.serializers import ExamSerializer, GradeSerializer, PracticeSerializer
# Create your views here.
from user.models import Student


class CommonPagination(PageNumberPagination):
    """考试列表自定义分页"""
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 10


class ExamListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    """考试列表页"""
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Exam.objects.all().order_by('id')
    # 序列化
    serializer_class = ExamSerializer
    # 分页
    pagination_class = CommonPagination
    # 开启过滤
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置filter的类为我们自定义的类
    filter_class = ExamFilter
    # 搜索,=name表示精确搜索，也可以使用各种正则表达式
    search_fields = ('name', 'major')
    # 排序
    ordering_fields = ('id', 'exam_date')

    # 重写queryset
    def get_queryset(self):
        # 学生ID
        student_id = self.request.query_params.get("student_id")
        student = Student.objects.get(id=student_id)

        if student:
            self.queryset = Exam.objects.filter(clazzs__student=student)
        return self.queryset


class GradeListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    """成绩列表"""
    # authentication_classes = []
    # permission_classes = []
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Grade.objects.all().order_by('-create_time')
    # 序列化
    serializer_class = GradeSerializer
    # 分页
    pagination_class = CommonPagination

    # 重写queryset
    def get_queryset(self):
        # 学生ID
        student_id = self.request.query_params.get("student_id")
        if student_id:
            self.queryset = Grade.objects.filter(student_id=student_id)
        return self.queryset
    # 重写返回
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        result_data = response.data
        return Response(
            {
                "code": 200,
                "message": "查询成功",
                "response": result_data
            }
        )


class PracticeListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """练习列表"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = []
    # permission_classes = []
    # 数据集
    queryset = Practice.objects.all()
    # 序列化
    serializer_class = PracticeSerializer
    # 分页
    pagination_class = CommonPagination

    def get_queryset(self):
        # 学生ID
        student_id = self.request.query_params.get('student_id')
        if student_id:
            self.queryset = Practice.objects.filter(student_id=student_id)
        return (self.queryset)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        result_data = response.data
        return Response(
            {
                "code": 200,
                "message": "查询成功",
                "response": result_data
            }
        )