from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication

from exam.views import CommonPagination
from question.models import Program
from record.models import ChoiceRecord, FillRecord, JudgeRecord, ProgramRecord, ChoiceMuRecord
from record.serializers import ChoiceRecordSerializer, FillRecordSerializer, JudgeRecordSerializer, \
    ProgramRecordSerializer, ChoiceMuRecordSerializer
from hsoftskill import serializers
from hsoftskill.models import Files


class FileView(generics.CreateAPIView):
    """
    上传文件
    """
    authentication_classes = []
    permission_classes = []
    queryset = Files.objects.filter()
    serializer_class = serializers.FileSerializer

    def create(self, request, *args, **kwargs):
        # print(request.data)
        if request.data.get('period') == "":
            return Response(data={'code':401,'msg':"参数不全"})
        #过滤文件名是否符合规范
        # namelist = ['张三']
        # filename = request.data.get('name').split('.')[0]
        # if filename in namelist:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data={'data':serializer.data,'code': 200}, status=status.HTTP_201_CREATED, headers=headers)
        # else:
        #     print(filename)
        #     return Response(data={'code': 402, 'msg': "文件命名不正确"})
class UploadListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    """上传列表"""
    # authentication_classes = []
    # permission_classes = []
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Files.objects.all().order_by('-upload_time')
    # 序列化
    serializer_class = serializers.FileSerializer
    # 分页
    pagination_class = CommonPagination

    # 重写queryset
    def get_queryset(self):
        # 学生ID
        student_id = self.request.query_params.get("student_id")
        if student_id:
            self.queryset = Files.objects.filter(uploader_id=student_id)
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
