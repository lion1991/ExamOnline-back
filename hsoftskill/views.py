import random

from django.http import FileResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from exam.views import CommonPagination
from hsoftskill.filevars import fileuserid, qj_userid, ljj_userid, wcl_userid, ybw_userid, wy_userid, \
    captainName, downloadlink, lc_userid
from question.models import Program
from record.models import ChoiceRecord, FillRecord, JudgeRecord, ProgramRecord, ChoiceMuRecord
from record.serializers import ChoiceRecordSerializer, FillRecordSerializer, JudgeRecordSerializer, \
    ProgramRecordSerializer, ChoiceMuRecordSerializer
from hsoftskill import serializers, robot, mergeexcel
from hsoftskill.models import Files, LimitFile, RandomFileId, CaptainFiles, ExamFiles, JudgeFiles, PersonalGradeFiles
#from tyadmin_api.auto_serializers import FilesListSerializer
#from tyadmin_api.auto_views import FilesViewSet
#from tyadmin_api.custom import XadminViewSet
#合并文件模块导入
# import os
# import xlrd2
# import xlsxwriter
# import glob
# from openpyxl import load_workbook
# from openpyxl.styles import Alignment
# from openpyxl.styles import Side, Border
# from openpyxl.styles import Font


class ExamFileView(generics.CreateAPIView):
    """
    上传考核题文件
    """
    authentication_classes = []
    permission_classes = []
    queryset = ExamFiles.objects.filter()
    serializer_class = serializers.ExamFileSerializer

    def create(self, request, *args, **kwargs):

        uploader = request.data.get('uploader')
        period = request.data.get('period')
        query = ExamFiles.objects.filter(period=period).values('uploader')[::1]
        uploadedid = []
        for index in query:
            uploadedid.append(index.get('uploader'))
        if int(uploader) in uploadedid:
            return Response(data={'msg': '处理失败，已经上传过', 'code': 405}, status=200)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        content = "考核题已经发布，请到网站下载。"
        is_send_all = False
        robot.send_ding_message(content,is_send_all)
        return Response(data={'data': serializer.data, 'code': 200}, status=status.HTTP_201_CREATED, headers=headers)


class FileView(generics.CreateAPIView):
    """
    上传组员考核文件
    """
    authentication_classes = []
    permission_classes = []
    queryset = Files.objects.filter()
    serializer_class = serializers.FileSerializer

    def create(self, request, *args, **kwargs):
        # print(request.data)
        # if request.data.get('period') == "":
        #     return Response(data={'code':401,'msg':"参数不全"})
        # 过滤文件名是否符合规范
        # namelist = ['张三']
        # filename = request.data.get('name').split('.')[0]
        # if filename in namelist:
        uploader = request.data.get('uploader')
        period = request.data.get('period')
        query = Files.objects.filter(period=period).values('uploader')[::1]
        uploadedid = []
        for index in query:
            uploadedid.append(index.get('uploader'))
        if int(uploader) in uploadedid:
            return Response(data={'msg': '处理失败，已经上传过', 'code': 405}, status=200)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data={'data': serializer.data, 'code': 200}, status=status.HTTP_201_CREATED, headers=headers)
        # else:
        #     print(filename)
        #     return Response(data={'code': 402, 'msg': "文件命名不正确"})

class CaptainExamFileView(generics.CreateAPIView):
    """
    上传组长考核文件
    """
    authentication_classes = []
    permission_classes = []
    queryset = CaptainFiles.objects.filter()
    serializer_class = serializers.CaptainFileSerializer

    def create(self, request, *args, **kwargs):

        uploader = request.data.get('uploader')
        period = request.data.get('period')
        query = CaptainFiles.objects.filter(period=period).values('uploader')[::1]
        uploadedid = []
        for index in query:
            uploadedid.append(index.get('uploader'))
        if int(uploader) in uploadedid:
            return Response(data={'msg': '处理失败，已经上传过', 'code': 405}, status=200)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data={'data': serializer.data, 'code': 200}, status=status.HTTP_201_CREATED, headers=headers)

class JudgeFileView(generics.CreateAPIView):
    """
    上传评分文件
    """
    authentication_classes = []
    permission_classes = []
    queryset = JudgeFiles.objects.filter()
    serializer_class = serializers.JudgeFileSerializer

    def create(self, request, *args, **kwargs):

        uploader = request.data.get('uploader')
        period = request.data.get('period')
        query = JudgeFiles.objects.filter(period=period).values('uploader')[::1]
        uploadedid = []
        for index in query:
            uploadedid.append(index.get('uploader'))
        if int(uploader) in uploadedid:
            return Response(data={'msg': '处理失败，已经上传过', 'code': 405}, status=200)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data={'data': serializer.data, 'code': 200}, status=status.HTTP_201_CREATED, headers=headers)

class PersonalGradeFileView(generics.CreateAPIView):
    """
    上传个人成绩文件
    """
    authentication_classes = []
    permission_classes = []
    queryset = PersonalGradeFiles.objects.filter()
    serializer_class = serializers.PersonalGradeFileSerializer

    def create(self, request, *args, **kwargs):

        uploader = request.data.get('uploader')
        period = request.data.get('period')
        query = PersonalGradeFiles.objects.filter(period=period).values('uploader')[::1]
        uploadedid = []
        for index in query:
            uploadedid.append(index.get('uploader'))
        if int(uploader) in uploadedid:
            return Response(data={'msg': '处理失败，已经上传过', 'code': 405}, status=200)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data={'data': serializer.data, 'code': 200}, status=status.HTTP_201_CREATED, headers=headers)

class ExamFileDownload(ModelViewSet):
    """
    考核题下载
    """
    authentication_classes = []
    permission_classes = []
    queryset = ExamFiles.objects.filter()
    serializer_class = serializers.ExamFileSerializer

    # 文件下载响应
    @action(methods=['get', 'post'], detail=True)
    def download(self, request, pk=None, *args, **kwargs):
        file_obj = self.get_object()
        print(file_obj)
        filename = str(file_obj)
        response = FileResponse(open(file_obj.file.path, 'rb'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename.encode('utf-8').decode('ISO-8859-1'))
        return response


class FileDownload(ModelViewSet):
    """
    获取组员考核文件下载
    """
    authentication_classes = []
    permission_classes = []
    queryset = Files.objects.filter()
    serializer_class = serializers.FileSerializer

    # 文件下载响应
    @action(methods=['get', 'post'], detail=True)
    def download(self, request, pk=None, *args, **kwargs):
        file_obj = self.get_object()
        print(file_obj)
        filename = str(file_obj)
        response = FileResponse(open(file_obj.file.path, 'rb'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename.encode('utf-8').decode('ISO-8859-1'))
        return response

class CaptainFileDownload(ModelViewSet):
    """
    获取组长考核文件下载
    """
    authentication_classes = []
    permission_classes = []
    queryset = CaptainFiles.objects.filter()
    serializer_class = serializers.CaptainFileSerializer

    # 文件下载响应
    @action(methods=['get', 'post'], detail=True)
    def download(self, request, pk=None, *args, **kwargs):
        file_obj = self.get_object()
        print(file_obj)
        filename = str(file_obj)
        response = FileResponse(open(file_obj.file.path, 'rb'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename.encode('utf-8').decode('ISO-8859-1'))
#         return response

class JudgeFileDownload(ModelViewSet):
    """
    评分文件下载
    """
    authentication_classes = []
    permission_classes = []
    queryset = JudgeFiles.objects.filter()
    serializer_class = serializers.JudgeFileSerializer

    # 文件下载响应
    @action(methods=['get', 'post'], detail=True)
    def download(self, request, pk=None, *args, **kwargs):
        file_obj = self.get_object()
        print(file_obj)
        filename = str(file_obj)
        response = FileResponse(open(file_obj.file.path, 'rb'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename.encode('utf-8').decode('ISO-8859-1'))
        return response

class PersonalGradeFileDownload(ModelViewSet):
    """
    个人成绩文件下载
    """
    authentication_classes = []
    permission_classes = []
    queryset = PersonalGradeFiles.objects.filter()
    serializer_class = serializers.PersonalGradeFileSerializer

    # 文件下载响应
    @action(methods=['get', 'post'], detail=True)
    def download(self, request, pk=None, *args, **kwargs):
        file_obj = self.get_object()
        print(file_obj)
        filename = str(file_obj)
        response = FileResponse(open(file_obj.file.path, 'rb'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename.encode('utf-8').decode('ISO-8859-1'))
        return response

class UploadListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    """showfile 查询上传列表"""
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


class LimitPeriodListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    """showlimitperiod，查询上传限制"""
    # authentication_classes = []
    # permission_classes = []
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = LimitFile.objects.all()
    # 序列化
    serializer_class = serializers.LimitFileSerializer

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


class FilePersion(APIView):
    # 返回查询的文件上传信息
    """
    生成各组长判分的组员，管理员每期结束后手动调用一次
    """
    authentication_classes = []
    permission_classes = []

    # 你要序列化的数据
    # serializer_class = serializers.FileSerializer  # 你要使用的序列化类
    # queryset = Files.objects.all().order_by('-pk')
    def get(self, request):
        req = request.GET
        period = (req['period'])
        qs = Files.objects.filter(period=period).values('id')  # GenericAPIView提供的等同于self.queryset
        ser = serializers.FileSerializer(instance=qs, many=True)  # GenericAPIView提供的等同于self.serializer_class
        # print(Files.objects.filter(period=1))
        # 定义各组随机列表
        qj_userid.clear()
        ljj_userid.clear()
        wcl_userid.clear()
        lc_userid.clear()
        ybw_userid.clear()
        wy_userid.clear()
        fileuserid.clear()

        for value in qs:
            fileuserid.append(value['id'])

        random.shuffle(fileuserid)

        while True:
            if fileuserid:
                qj_userid.append(downloadlink + "/filesdownload/" + str(fileuserid.pop()) + "/download")
            if fileuserid:
                ljj_userid.append(downloadlink + "/filesdownload/" + str(fileuserid.pop()) + "/download")
            if fileuserid:
                wcl_userid.append(downloadlink + "/filesdownload/" + str(fileuserid.pop()) + "/download")
            if fileuserid:
                lc_userid.append(downloadlink + "/filesdownload/" + str(fileuserid.pop()) + "/download")
            if fileuserid:
                ybw_userid.append(downloadlink + "/filesdownload/" + str(fileuserid.pop()) + "/download")
            if fileuserid:
                wy_userid.append(downloadlink + "/filesdownload/" + str(fileuserid.pop()) + "/download")
            else:
                break
        try:
            RandomFileId.objects.create(team_one=qj_userid, team_two=ljj_userid, team_three=wcl_userid,
                                        team_four=lc_userid,
                                        team_five=ybw_userid, team_six=wy_userid, period_id=period)


            print(f"开始{qj_userid}")
            print(ljj_userid)
            print(wcl_userid)
            print(lc_userid)
            print(ybw_userid)
            print(f"结束{wy_userid}")
            return Response(data={'msg': '处理成功', 'code': 200}, status=200)
        except Exception as e:
            print(e)
            return Response(data={'msg': '处理失败，请检查period', 'code': 400}, status=400)

class MergeFile(APIView):
    """
    合并各组长已上传的评分文件
    """
    authentication_classes = []
    permission_classes = []


    queryset = JudgeFiles.objects.filter()
    serializer_class = serializers.JudgeFileSerializer

    # def create(self, request, *args, **kwargs):
    #
    #     uploader = request.data.get('uploader')
    #     period = request.data.get('period')
    #     query = JudgeFiles.objects.filter(period=period).values('uploader')[::1]
    #     uploadedid = []
    #     for index in query:
    #         uploadedid.append(index.get('uploader'))
    #     if int(uploader) in uploadedid:
    #         return Response(data={'msg': '处理失败，已经上传过', 'code': 405}, status=200)
    #
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(data={'data': serializer.data, 'code': 200}, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request):
        req = request.data
        period = (req['period'])
        name = '评分汇总.xlsx'
        filepath = "upload/judge/exam" + str(period) + "/"
        file = "upload/judge/exam" + str(period) + "/" + name
        try:
            query = JudgeFiles.objects.filter(period=period).values('uploader')[::1]
            uploadedid = []
            uploader = 1
            for index in query:
                uploadedid.append(index.get('uploader'))
            if uploader in uploadedid:
                return Response(data={'msg': '处理失败，文件已合并', 'code': 405})
            else:
                obj = mergeexcel.MakeExcel()
                obj.startwork(filepath)
                jfobj = JudgeFiles(name=name, period=period, file=file, limit_period_id=1,uploader_id=1)
                jfobj.save()
                return Response(data={'msg': '处理成功', 'code': 200}, status=200)
        except Exception as e:
            print(e)
            return Response(data={'msg': '处理失败，请检查period', 'code': 400}, status=400)

class CaptainPersion(APIView):
    #为请求的组长下发随机好的组员
    """
    根据组长id下发全部判分组员信息，每期执行一次
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        req = request.GET
        period = (req['period'])
        captain_name = (req['username'])
        qs = RandomFileId.objects.filter(period_id=period).first()  # GenericAPIView提供的等同于self.queryset
        ser = serializers.RandomFileIdSerializer(instance=qs, many=False)
        # print(qs)
        if captain_name in  captainName and qs != None:
            return Response(data={'people':ser.data,'msg': '处理成功', 'code': 200}, status=200)
        elif qs == None:
            return Response(data={'msg': '本期暂未生成提交文件', 'code': 404}, status=200)
        else:
            return Response(data={'msg': '你没有权限，请求失败', 'code': 401}, status=200)

class CaptainUploadList(APIView):
    """
    生成组长上传答题文件下载链接返回
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        req = request.GET
        period = (req['period'])
        print(period)
        if not period:
            return Response(data={'msg': '处理失败，没有period参数', 'code': 401}, status=200)

        # captain_name = (req['username'])
        qs = CaptainFiles.objects.filter(period=period).values('id')
        for value in qs:   #从组长上传表查询对应期数的id，开始循环。
            id = value['id']
            address = f"{downloadlink}/captainfilesdownload/{id}/download" #赋值当前id的下载链接
            p = CaptainFiles.objects.get(id=id)
            # print(p.downloadfile)
            if not p.downloadfile:   #如果当前downloadfile字段无值，将链接传入并保存到数据库中
                p.downloadfile = address
                p.save()
        query = CaptainFiles.objects.filter(period=period).all()
        ser = serializers.CaptainFileSerializer(instance=query, many=True)
        return Response(data={'data': ser.data, 'msg': '处理成功', 'code': 200}, status=200)

class CaptainJudgeUploadList(APIView):
    """
    生成组长上传评分文件下载链接返回
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        req = request.GET
        period = (req['period'])
        print(period)
        if not period:
            return Response(data={'msg': '处理失败，没有period参数', 'code': 401}, status=200)

        # captain_name = (req['username'])
        qs = JudgeFiles.objects.filter(period=period).values('id')
        for value in qs:
            id = value['id']
            address = f"{downloadlink}/judgefiledownload/{id}/download"
            p = JudgeFiles.objects.get(id=id)
            # print(p.downloadfile)
            if not p.downloadfile:
                p.downloadfile = address
                p.save()
        query = JudgeFiles.objects.filter(period=period).all()
        ser = serializers.JudgeFileSerializer(instance=query, many=True)
        return Response(data={'data': ser.data, 'msg': '处理成功', 'code': 200}, status=200)

class PersonalGradeUploadList(APIView):
    """
    生成个人成绩文件下载链接返回
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        req = request.GET
        period = (req['period'])
        # uploader = (req['uploader'])
        # print(period)
        if not period:
            return Response(data={'msg': '处理失败，没有period参数', 'code': 401}, status=200)
        # if not uploader:
            # return Response(data={'msg': '处理失败，没有uploader参数', 'code': 401}, status=200)

        # captain_name = (req['username'])
        try:
            qs = PersonalGradeFiles.objects.filter(period=period).values('id')
            print(qs)
            for value in qs:
                id = value['id']
                address = f"{downloadlink}/personalgradefiledownload/{id}/download"
                p = PersonalGradeFiles.objects.get(id=id)
                # print(p.uploader)
                # print(address)
                # print(p)
                # print('------')
                file_obj = Files.objects.get(period=period, uploader=p.uploader)
                if not file_obj.downloadfile:
                    file_obj.downloadfile = address
                    file_obj.save()
            query = Files.objects.filter(period=period).all()
            ser = serializers.FileSerializer(instance=query, many=True)
            return Response(data={'data': ser.data, 'msg': '处理成功', 'code': 200}, status=200)
        except:
            return Response(data={'msg': '未找到当期评分', 'code': 404}, status=200)

class ExamUploadList(APIView):
    """
    生成考题文件下载链接返回
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        req = request.GET
        period = (req['period'])
        if not period:
            return Response(data={'msg': '处理失败，没有period参数', 'code': 401}, status=200)

        # captain_name = (req['username'])
        qs = ExamFiles.objects.filter(period=period).values('id')
        for value in qs:
            id = value['id']
            address = f"{downloadlink}/examfilesdownload/{id}/download"
            p = ExamFiles.objects.get(id=id)
            # print(p.downloadfile)
            if not p.downloadfile:
                p.downloadfile = address
                p.save()
        query = ExamFiles.objects.filter(period=period).all()
        ser = serializers.ExamFileSerializer(instance=query, many=True)
        # print(ser.data)
        if query == None:
            return Response(data={'msg': '处理失败，未发现考核题文件', 'code': 404}, status=200)
        return Response(data={'data':ser.data, 'msg': '处理成功', 'code': 200}, status=200)

class UploadedEmployee(APIView):
    """
    查询本期已上传答题人员
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        req = request.GET
        period = (req['period'])
        query = Files.objects.filter(period=period).all()
        ser = serializers.FilePersonSerializer(instance=query, many=True)
        return Response(data={'data':ser.data, 'msg': '处理成功', 'code': 200}, status=200)


#转换excel为html
# from Personnel.models import Contract
# import pandas
# from django.shortcuts import render
# def load_excel(request):
#     if request.method == 'GET':
#         # 获取前台传过来的id值，判断文件的类型是不是excel。
#         id = request.GET.get('id')
#         contract_type = Contract.objects.filter(contract_id=id).first().contract_type
#         if contract_type == 'excel':
#             # 从数据库中获取文件的存的path，
#             path_obj = Contract.objects.filter(contract_id=id).first().contract_content
#             contract_name = Contract.objects.filter(contract_id=id).first().contract_name
#             # 重命名并指定路径{ 将文件写入template文件夹中，因为我们的Django项目静态页面都是存放在这个文件夹下面}
#             new_file_name = "template/" + contract_name.split('.')[0] + '.html'
#             html_path = new_file_name.split('/')[1]
#
#             # 通过pandas.ExcelFie函数，将excel文件转成html
#             xd = pandas.ExcelFile(path_obj)
#             df = xd.parse()
#             html = df.to_html(header=True, index=True)
#             # 将转换后的html写入，一定要加编码方式utf-8，要不页面中打开会乱码
#             with open(new_file_name, 'w', encoding='utf-8') as file:
#                 file.writelines('<meta charset="UTF-8">\n')
#                 file.write(html)
#     return render(request, html_path, locals())
