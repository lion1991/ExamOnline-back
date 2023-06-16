
from rest_framework import viewsets
from tyadmin_api.custom import XadminViewSet
from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from user.models import Department, Teacher, Student, UserRolesInfo
from exam.models import Paper, Exam, Grade, Practice
from question.models import Choice, ChoiceMu, Fill, Judge, Program
from record.models import ChoiceRecord, ChoiceMuRecord, FillRecord, JudgeRecord, ProgramRecord
from hsoftskill.models import LimitFile, RandomFileId, Files, PersonalGradeFiles, CaptainFiles, ExamFiles, JudgeFiles, Subject, Score

from tyadmin_api.auto_serializers import PermissionListSerializer, GroupListSerializer, UserListSerializer, ContentTypeListSerializer, DepartmentListSerializer, TeacherListSerializer, StudentListSerializer, UserRolesInfoListSerializer, PaperListSerializer, ExamListSerializer, GradeListSerializer, PracticeListSerializer, ChoiceListSerializer, ChoiceMuListSerializer, FillListSerializer, JudgeListSerializer, ProgramListSerializer, ChoiceRecordListSerializer, ChoiceMuRecordListSerializer, FillRecordListSerializer, JudgeRecordListSerializer, ProgramRecordListSerializer, LimitFileListSerializer, RandomFileIdListSerializer, FilesListSerializer, PersonalGradeFilesListSerializer, CaptainFilesListSerializer, ExamFilesListSerializer, JudgeFilesListSerializer, SubjectListSerializer, ScoreListSerializer
from tyadmin_api.auto_serializers import PermissionCreateUpdateSerializer, GroupCreateUpdateSerializer, UserCreateUpdateSerializer, ContentTypeCreateUpdateSerializer, DepartmentCreateUpdateSerializer, TeacherCreateUpdateSerializer, StudentCreateUpdateSerializer, UserRolesInfoCreateUpdateSerializer, PaperCreateUpdateSerializer, ExamCreateUpdateSerializer, GradeCreateUpdateSerializer, PracticeCreateUpdateSerializer, ChoiceCreateUpdateSerializer, ChoiceMuCreateUpdateSerializer, FillCreateUpdateSerializer, JudgeCreateUpdateSerializer, ProgramCreateUpdateSerializer, ChoiceRecordCreateUpdateSerializer, ChoiceMuRecordCreateUpdateSerializer, FillRecordCreateUpdateSerializer, JudgeRecordCreateUpdateSerializer, ProgramRecordCreateUpdateSerializer, LimitFileCreateUpdateSerializer, RandomFileIdCreateUpdateSerializer, FilesCreateUpdateSerializer, PersonalGradeFilesCreateUpdateSerializer, CaptainFilesCreateUpdateSerializer, ExamFilesCreateUpdateSerializer, JudgeFilesCreateUpdateSerializer, SubjectCreateUpdateSerializer, ScoreCreateUpdateSerializer
from tyadmin_api.auto_filters import PermissionFilter, GroupFilter, UserFilter, ContentTypeFilter, DepartmentFilter, TeacherFilter, StudentFilter, UserRolesInfoFilter, PaperFilter, ExamFilter, GradeFilter, PracticeFilter, ChoiceFilter, ChoiceMuFilter, FillFilter, JudgeFilter, ProgramFilter, ChoiceRecordFilter, ChoiceMuRecordFilter, FillRecordFilter, JudgeRecordFilter, ProgramRecordFilter, LimitFileFilter, RandomFileIdFilter, FilesFilter, PersonalGradeFilesFilter, CaptainFilesFilter, ExamFilesFilter, JudgeFilesFilter, SubjectFilter, ScoreFilter

    
class PermissionViewSet(XadminViewSet):
    serializer_class = PermissionListSerializer
    queryset = Permission.objects.all().order_by('-pk')
    filterset_class = PermissionFilter
    search_fields = ["name","codename"]

    def get_serializer_class(self):
        if self.action == "list":
            return PermissionListSerializer
        else:
            return PermissionCreateUpdateSerializer

    
class GroupViewSet(XadminViewSet):
    serializer_class = GroupListSerializer
    queryset = Group.objects.all().order_by('-pk')
    filterset_class = GroupFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return GroupListSerializer
        else:
            return GroupCreateUpdateSerializer

    
class UserViewSet(XadminViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all().order_by('-pk')
    filterset_class = UserFilter
    search_fields = ["password","username","first_name","last_name","email"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        else:
            return UserCreateUpdateSerializer

    
class ContentTypeViewSet(XadminViewSet):
    serializer_class = ContentTypeListSerializer
    queryset = ContentType.objects.all().order_by('-pk')
    filterset_class = ContentTypeFilter
    search_fields = ["app_label","model"]

    def get_serializer_class(self):
        if self.action == "list":
            return ContentTypeListSerializer
        else:
            return ContentTypeCreateUpdateSerializer

    
class DepartmentViewSet(XadminViewSet):
    serializer_class = DepartmentListSerializer
    queryset = Department.objects.all().order_by('-pk')
    filterset_class = DepartmentFilter
    search_fields = ["department"]

    def get_serializer_class(self):
        if self.action == "list":
            return DepartmentListSerializer
        else:
            return DepartmentCreateUpdateSerializer

    
class TeacherViewSet(XadminViewSet):
    serializer_class = TeacherListSerializer
    queryset = Teacher.objects.all().order_by('-pk')
    filterset_class = TeacherFilter
    search_fields = ["name","gender","title","institute"]

    def get_serializer_class(self):
        if self.action == "list":
            return TeacherListSerializer
        else:
            return TeacherCreateUpdateSerializer

    
class StudentViewSet(XadminViewSet):
    serializer_class = StudentListSerializer
    queryset = Student.objects.all().order_by('-pk')
    filterset_class = StudentFilter
    search_fields = ["name","gender","avatar","introduction"]

    def get_serializer_class(self):
        if self.action == "list":
            return StudentListSerializer
        else:
            return StudentCreateUpdateSerializer

    
class UserRolesInfoViewSet(XadminViewSet):
    serializer_class = UserRolesInfoListSerializer
    queryset = UserRolesInfo.objects.all().order_by('-pk')
    filterset_class = UserRolesInfoFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserRolesInfoListSerializer
        else:
            return UserRolesInfoCreateUpdateSerializer

    
class PaperViewSet(XadminViewSet):
    serializer_class = PaperListSerializer
    queryset = Paper.objects.all().order_by('-pk')
    filterset_class = PaperFilter
    search_fields = ["name","level"]

    def get_serializer_class(self):
        if self.action == "list":
            return PaperListSerializer
        else:
            return PaperCreateUpdateSerializer

    
class ExamViewSet(XadminViewSet):
    serializer_class = ExamListSerializer
    queryset = Exam.objects.all().order_by('-pk')
    filterset_class = ExamFilter
    search_fields = ["name","major"]

    def get_serializer_class(self):
        if self.action == "list":
            return ExamListSerializer
        else:
            return ExamCreateUpdateSerializer

    
class GradeViewSet(XadminViewSet):
    serializer_class = GradeListSerializer
    queryset = Grade.objects.all().order_by('-pk')
    filterset_class = GradeFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return GradeListSerializer
        else:
            return GradeCreateUpdateSerializer

    
class PracticeViewSet(XadminViewSet):
    serializer_class = PracticeListSerializer
    queryset = Practice.objects.all().order_by('-pk')
    filterset_class = PracticeFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return PracticeListSerializer
        else:
            return PracticeCreateUpdateSerializer

    
class ChoiceViewSet(XadminViewSet):
    serializer_class = ChoiceListSerializer
    queryset = Choice.objects.all().order_by('-pk')
    filterset_class = ChoiceFilter
    search_fields = ["answer_A","answer_B","answer_C","answer_D","right_answer","level"]

    def get_serializer_class(self):
        if self.action == "list":
            return ChoiceListSerializer
        else:
            return ChoiceCreateUpdateSerializer

    
class ChoiceMuViewSet(XadminViewSet):
    serializer_class = ChoiceMuListSerializer
    queryset = ChoiceMu.objects.all().order_by('-pk')
    filterset_class = ChoiceMuFilter
    search_fields = ["answer_A","answer_B","answer_C","answer_D","right_answer","level"]

    def get_serializer_class(self):
        if self.action == "list":
            return ChoiceMuListSerializer
        else:
            return ChoiceMuCreateUpdateSerializer

    
class FillViewSet(XadminViewSet):
    serializer_class = FillListSerializer
    queryset = Fill.objects.all().order_by('-pk')
    filterset_class = FillFilter
    search_fields = ["right_answer","level"]

    def get_serializer_class(self):
        if self.action == "list":
            return FillListSerializer
        else:
            return FillCreateUpdateSerializer

    
class JudgeViewSet(XadminViewSet):
    serializer_class = JudgeListSerializer
    queryset = Judge.objects.all().order_by('-pk')
    filterset_class = JudgeFilter
    search_fields = ["right_answer","level"]

    def get_serializer_class(self):
        if self.action == "list":
            return JudgeListSerializer
        else:
            return JudgeCreateUpdateSerializer

    
class ProgramViewSet(XadminViewSet):
    serializer_class = ProgramListSerializer
    queryset = Program.objects.all().order_by('-pk')
    filterset_class = ProgramFilter
    search_fields = ["level"]

    def get_serializer_class(self):
        if self.action == "list":
            return ProgramListSerializer
        else:
            return ProgramCreateUpdateSerializer

    
class ChoiceRecordViewSet(XadminViewSet):
    serializer_class = ChoiceRecordListSerializer
    queryset = ChoiceRecord.objects.all().order_by('-pk')
    filterset_class = ChoiceRecordFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ChoiceRecordListSerializer
        else:
            return ChoiceRecordCreateUpdateSerializer

    
class ChoiceMuRecordViewSet(XadminViewSet):
    serializer_class = ChoiceMuRecordListSerializer
    queryset = ChoiceMuRecord.objects.all().order_by('-pk')
    filterset_class = ChoiceMuRecordFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ChoiceMuRecordListSerializer
        else:
            return ChoiceMuRecordCreateUpdateSerializer

    
class FillRecordViewSet(XadminViewSet):
    serializer_class = FillRecordListSerializer
    queryset = FillRecord.objects.all().order_by('-pk')
    filterset_class = FillRecordFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return FillRecordListSerializer
        else:
            return FillRecordCreateUpdateSerializer

    
class JudgeRecordViewSet(XadminViewSet):
    serializer_class = JudgeRecordListSerializer
    queryset = JudgeRecord.objects.all().order_by('-pk')
    filterset_class = JudgeRecordFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return JudgeRecordListSerializer
        else:
            return JudgeRecordCreateUpdateSerializer

    
class ProgramRecordViewSet(XadminViewSet):
    serializer_class = ProgramRecordListSerializer
    queryset = ProgramRecord.objects.all().order_by('-pk')
    filterset_class = ProgramRecordFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ProgramRecordListSerializer
        else:
            return ProgramRecordCreateUpdateSerializer

    
class LimitFileViewSet(XadminViewSet):
    serializer_class = LimitFileListSerializer
    queryset = LimitFile.objects.all().order_by('-pk')
    filterset_class = LimitFileFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return LimitFileListSerializer
        else:
            return LimitFileCreateUpdateSerializer

    
class RandomFileIdViewSet(XadminViewSet):
    serializer_class = RandomFileIdListSerializer
    queryset = RandomFileId.objects.all().order_by('-pk')
    filterset_class = RandomFileIdFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return RandomFileIdListSerializer
        else:
            return RandomFileIdCreateUpdateSerializer

    
class FilesViewSet(XadminViewSet):
    serializer_class = FilesListSerializer
    queryset = Files.objects.all().order_by('-pk')
    filterset_class = FilesFilter
    search_fields = ["name","downloadfile","finger"]

    def get_serializer_class(self):
        if self.action == "list":
            return FilesListSerializer
        else:
            return FilesCreateUpdateSerializer

    
class PersonalGradeFilesViewSet(XadminViewSet):
    serializer_class = PersonalGradeFilesListSerializer
    queryset = PersonalGradeFiles.objects.all().order_by('-pk')
    filterset_class = PersonalGradeFilesFilter
    search_fields = ["name","downloadfile"]

    def get_serializer_class(self):
        if self.action == "list":
            return PersonalGradeFilesListSerializer
        else:
            return PersonalGradeFilesCreateUpdateSerializer

    
class CaptainFilesViewSet(XadminViewSet):
    serializer_class = CaptainFilesListSerializer
    queryset = CaptainFiles.objects.all().order_by('-pk')
    filterset_class = CaptainFilesFilter
    search_fields = ["name","downloadfile","finger"]

    def get_serializer_class(self):
        if self.action == "list":
            return CaptainFilesListSerializer
        else:
            return CaptainFilesCreateUpdateSerializer

    
class ExamFilesViewSet(XadminViewSet):
    serializer_class = ExamFilesListSerializer
    queryset = ExamFiles.objects.all().order_by('-pk')
    filterset_class = ExamFilesFilter
    search_fields = ["name","downloadfile","exam_questions_type"]

    def get_serializer_class(self):
        if self.action == "list":
            return ExamFilesListSerializer
        else:
            return ExamFilesCreateUpdateSerializer

    
class JudgeFilesViewSet(XadminViewSet):
    serializer_class = JudgeFilesListSerializer
    queryset = JudgeFiles.objects.all().order_by('-pk')
    filterset_class = JudgeFilesFilter
    search_fields = ["name","downloadfile"]

    def get_serializer_class(self):
        if self.action == "list":
            return JudgeFilesListSerializer
        else:
            return JudgeFilesCreateUpdateSerializer

    
class SubjectViewSet(XadminViewSet):
    serializer_class = SubjectListSerializer
    queryset = Subject.objects.all().order_by('-pk')
    filterset_class = SubjectFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return SubjectListSerializer
        else:
            return SubjectCreateUpdateSerializer

    
class ScoreViewSet(XadminViewSet):
    serializer_class = ScoreListSerializer
    queryset = Score.objects.all().order_by('-pk')
    filterset_class = ScoreFilter
    search_fields = ["group"]

    def get_serializer_class(self):
        if self.action == "list":
            return ScoreListSerializer
        else:
            return ScoreCreateUpdateSerializer
