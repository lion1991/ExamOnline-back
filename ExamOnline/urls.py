"""ExamOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# import xadmin
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import TokenRefreshView

from ExamOnline import settings
from hsoftskill import views
from hsoftskill.views import UploadListViewSet, LimitPeriodListViewSet, ResetPasswordView

from user.views import MyObtainTokenPairView, QueryUserView
    #, QueryMenuDetail

from exam.views import GradeListViewSet, ExamListViewSet, PracticeListViewSet
from question.views import ChoiceListViewSet, FillListViewSet, JudgeListViewSet, ProgramListViewSet, CheckProgramApi, \
    ChoiceMuListViewSet
from record.views import ChoiceRecordListViewSet, FillRecordListViewSet, JudgeRecordListViewSet, \
    ProgramRecordListViewSet, ChoiceMuRecordListViewSet
from user.views import RegisterViewSet, StudentViewSet, UpdatePwdApi, DepartmentListViewSet
from tyadmin_api.views import AdminIndexView

router = DefaultRouter()

# 配置exams的url
router.register(r'exams', ExamListViewSet)
router.register(r'grades', GradeListViewSet)
router.register(r'choices', ChoiceListViewSet)
router.register(r'choicesmu', ChoiceMuListViewSet)
router.register(r'fills', FillListViewSet)
router.register(r'judges', JudgeListViewSet)
router.register(r'programs', ProgramListViewSet)
router.register(r'register', RegisterViewSet)
router.register(r'department', DepartmentListViewSet)
router.register(r'students', StudentViewSet)
router.register(r'practices', PracticeListViewSet)
router.register(r'records/choices', ChoiceRecordListViewSet)
router.register(r'records/choicesmu', ChoiceMuRecordListViewSet)
router.register(r'records/fills', FillRecordListViewSet)
router.register(r'records/judges', JudgeRecordListViewSet)
router.register(r'records/programs', ProgramRecordListViewSet)
router.register(r'showfile', UploadListViewSet)
router.register(r'showlimitperiod', LimitPeriodListViewSet)
#router.register(r'filesdownload', views.FileDownload) #组员考核文件下载
router.register(r'captainfilesdownload', views.CaptainFileDownload)
router.register(r'examfilesdownload', views.ExamFileDownload)
router.register(r'judgefiledownload', views.JudgeFileDownload)  # 评分下载
router.register(r'personalgradefiledownload', views.PersonalGradeFileDownload)  # 评分下载

# router.register(r'filepersion', views.FilePersion.as_view())

schema_view = get_schema_view(
    openapi.Info(
        title="Tweet API",
        default_version='v1',
        description="Welcome to the world of Tweet",
        terms_of_service="https://www.tweet.org",
        contact=openapi.Contact(email="demo@tweet.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path('admin/', xadmin.site.urls),
    path('api/xadmin/v1/', include('tyadmin_api.urls')),
    re_path('^xadmin/.*', AdminIndexView.as_view()),
    # re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),

    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'), #重置密码
    path('docs/', include_docs_urls('Python在线考试系统')),
    # path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  #<-- 这里
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  #<-- 这里
    path('api-auth/', include('rest_framework.urls')),
    path('jwt-auth/', obtain_jwt_token),
    path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('check-program/', CheckProgramApi.as_view()),
    path('update-pwd/', UpdatePwdApi.as_view()),
    path(r'examfile/', views.ExamFileView.as_view()),                       #考核题上传
    path(r'file/', views.FileView.as_view()),                               #组员上传
    path(r'captainfile/', views.CaptainExamFileView.as_view()),             #组长上传
    path(r'judgefile/', views.JudgeFileView.as_view()),                     #评分上传
    path(r'personalgradefile/', views.PersonalGradeFileView.as_view()),     #个人成绩上传
    path(r'filepersion/', views.FilePersion.as_view()),                     #生成随机组员
    path(r'mergefile/', views.MergeFile.as_view()),                     #合并各组评分文件
    path(r'captainpersion/', views.CaptainPersion.as_view()),               #获取随机评分人员
    path(r'captainuploadlist/', views.CaptainUploadList.as_view()),         #生成组长上传答题文件下载链接返回
    path(r'captainjudgeuploadlist/', views.CaptainJudgeUploadList.as_view()),         #生成组长上传评分文件下载链接返回
    path(r'personalgradeuploadlist/', views.PersonalGradeUploadList.as_view()),         #生成个人成绩文件下载链接返回
    path(r'examuploadlist/', views.ExamUploadList.as_view()),               #生成考题文件下载链接返回
    path(r'uploadedemployee/', views.UploadedEmployee.as_view()),               #查询已上传人员
    path('filesdownload/<str:filename>/<int:period>', views.FileDownload.as_view({'get': 'download_zip'}), name='download_zip'),
    # re_path(r'^queryuser/(?P<pk>\d+)$', QueryUserView.as_view()),               #考核题下载
    # re_path(r'^querymenu/(?P<pk>\d+)$', QueryMenuDetail.as_view()),               #考核题下载
    path(r'insertdatabase/', views.InsertDatabase.as_view()),               #插入成绩到数据库
    path(r'getallperiod/', views.GetAllPeriod.as_view()),               # 获取考核期数
    path(r'getscore/', views.GetScore.as_view()),               # 获取人员成绩信息

    re_path('^', include(router.urls)),

    # re_path('load_excel/', views.load_excel, name='load_excel') # 预览成绩

]
