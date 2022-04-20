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
import xadmin
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import TokenRefreshView
from user.views import MyObtainTokenPairView

from exam.views import GradeListViewSet, ExamListViewSet, PracticeListViewSet
from question.views import ChoiceListViewSet, FillListViewSet, JudgeListViewSet, ProgramListViewSet, CheckProgramApi, \
    ChoiceMuListViewSet
from record.views import ChoiceRecordListViewSet, FillRecordListViewSet, JudgeRecordListViewSet, \
    ProgramRecordListViewSet, ChoiceMuRecordListViewSet
from user.views import RegisterViewSet, StudentViewSet, UpdatePwdApi, ClazzListViewSet

from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

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
router.register(r'clazzs', ClazzListViewSet)
router.register(r'students', StudentViewSet)
router.register(r'practices', PracticeListViewSet)
router.register(r'records/choices', ChoiceRecordListViewSet)
router.register(r'records/choicesmu', ChoiceMuRecordListViewSet)
router.register(r'records/fills', FillRecordListViewSet)
router.register(r'records/judges', JudgeRecordListViewSet)
router.register(r'records/programs', ProgramRecordListViewSet)

openapi_info = openapi.Info(
        title="模板数据管理服务",
        default_version='v1',
        description="模板数据管理服务",
        # terms_of_service="https://www.tweet.org",
        contact=openapi.Contact(email="xxx@xxx.com"),
        # license=openapi.License(name="Awesome IP"),
    )

schema_view = get_schema_view(
    openapi_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', xadmin.site.urls),
    # path('docs/', include_docs_urls('Python在线考试系统')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api-auth/', include('rest_framework.urls')),
    path('jwt-auth/', obtain_jwt_token),
    path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('check-program/', CheckProgramApi.as_view()),
    path('update-pwd/', UpdatePwdApi.as_view()),
    re_path('^', include(router.urls))
]
