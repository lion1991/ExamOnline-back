
from rest_framework import viewsets
from tyadmin_api.custom import XadminViewSet
from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from user.models import Department, Teacher, Student, UserRolesInfo
from exam.models import Paper, Exam, Grade, Practice
from question.models import Choice, ChoiceMu, Fill, Judge, Program
from record.models import ChoiceRecord, ChoiceMuRecord, FillRecord, JudgeRecord, ProgramRecord
from hsoftskill.models import LimitFile, RandomFileId, Files, PersonalGradeFiles, CaptainFiles, ExamFiles, JudgeFiles, Score3, LinuxScore3, NetworkScore3, OfficeScore3, Score4, LinuxScore4, NetworkScore4, OfficeScore4, Score5, LinuxScore5, NetworkScore5, OfficeScore5, Score6, LinuxScore6, NetworkScore6, Score7, LinuxScore7, NetworkScore7, Score8, LinuxScore8, NetworkScore8, Score9, LinuxScore9, NetworkScore9, Score10, LinuxScore10

from tyadmin_api.auto_serializers import PermissionListSerializer, GroupListSerializer, UserListSerializer, ContentTypeListSerializer, DepartmentListSerializer, TeacherListSerializer, StudentListSerializer, UserRolesInfoListSerializer, PaperListSerializer, ExamListSerializer, GradeListSerializer, PracticeListSerializer, ChoiceListSerializer, ChoiceMuListSerializer, FillListSerializer, JudgeListSerializer, ProgramListSerializer, ChoiceRecordListSerializer, ChoiceMuRecordListSerializer, FillRecordListSerializer, JudgeRecordListSerializer, ProgramRecordListSerializer, LimitFileListSerializer, RandomFileIdListSerializer, FilesListSerializer, PersonalGradeFilesListSerializer, CaptainFilesListSerializer, ExamFilesListSerializer, JudgeFilesListSerializer, Score3ListSerializer, LinuxScore3ListSerializer, NetworkScore3ListSerializer, OfficeScore3ListSerializer, Score4ListSerializer, LinuxScore4ListSerializer, NetworkScore4ListSerializer, OfficeScore4ListSerializer, Score5ListSerializer, LinuxScore5ListSerializer, NetworkScore5ListSerializer, OfficeScore5ListSerializer, Score6ListSerializer, LinuxScore6ListSerializer, NetworkScore6ListSerializer, Score7ListSerializer, LinuxScore7ListSerializer, NetworkScore7ListSerializer, Score8ListSerializer, LinuxScore8ListSerializer, NetworkScore8ListSerializer, Score9ListSerializer, LinuxScore9ListSerializer, NetworkScore9ListSerializer, Score10ListSerializer, LinuxScore10ListSerializer
from tyadmin_api.auto_serializers import PermissionCreateUpdateSerializer, GroupCreateUpdateSerializer, UserCreateUpdateSerializer, ContentTypeCreateUpdateSerializer, DepartmentCreateUpdateSerializer, TeacherCreateUpdateSerializer, StudentCreateUpdateSerializer, UserRolesInfoCreateUpdateSerializer, PaperCreateUpdateSerializer, ExamCreateUpdateSerializer, GradeCreateUpdateSerializer, PracticeCreateUpdateSerializer, ChoiceCreateUpdateSerializer, ChoiceMuCreateUpdateSerializer, FillCreateUpdateSerializer, JudgeCreateUpdateSerializer, ProgramCreateUpdateSerializer, ChoiceRecordCreateUpdateSerializer, ChoiceMuRecordCreateUpdateSerializer, FillRecordCreateUpdateSerializer, JudgeRecordCreateUpdateSerializer, ProgramRecordCreateUpdateSerializer, LimitFileCreateUpdateSerializer, RandomFileIdCreateUpdateSerializer, FilesCreateUpdateSerializer, PersonalGradeFilesCreateUpdateSerializer, CaptainFilesCreateUpdateSerializer, ExamFilesCreateUpdateSerializer, JudgeFilesCreateUpdateSerializer, Score3CreateUpdateSerializer, LinuxScore3CreateUpdateSerializer, NetworkScore3CreateUpdateSerializer, OfficeScore3CreateUpdateSerializer, Score4CreateUpdateSerializer, LinuxScore4CreateUpdateSerializer, NetworkScore4CreateUpdateSerializer, OfficeScore4CreateUpdateSerializer, Score5CreateUpdateSerializer, LinuxScore5CreateUpdateSerializer, NetworkScore5CreateUpdateSerializer, OfficeScore5CreateUpdateSerializer, Score6CreateUpdateSerializer, LinuxScore6CreateUpdateSerializer, NetworkScore6CreateUpdateSerializer, Score7CreateUpdateSerializer, LinuxScore7CreateUpdateSerializer, NetworkScore7CreateUpdateSerializer, Score8CreateUpdateSerializer, LinuxScore8CreateUpdateSerializer, NetworkScore8CreateUpdateSerializer, Score9CreateUpdateSerializer, LinuxScore9CreateUpdateSerializer, NetworkScore9CreateUpdateSerializer, Score10CreateUpdateSerializer, LinuxScore10CreateUpdateSerializer
from tyadmin_api.auto_filters import PermissionFilter, GroupFilter, UserFilter, ContentTypeFilter, DepartmentFilter, TeacherFilter, StudentFilter, UserRolesInfoFilter, PaperFilter, ExamFilter, GradeFilter, PracticeFilter, ChoiceFilter, ChoiceMuFilter, FillFilter, JudgeFilter, ProgramFilter, ChoiceRecordFilter, ChoiceMuRecordFilter, FillRecordFilter, JudgeRecordFilter, ProgramRecordFilter, LimitFileFilter, RandomFileIdFilter, FilesFilter, PersonalGradeFilesFilter, CaptainFilesFilter, ExamFilesFilter, JudgeFilesFilter, Score3Filter, LinuxScore3Filter, NetworkScore3Filter, OfficeScore3Filter, Score4Filter, LinuxScore4Filter, NetworkScore4Filter, OfficeScore4Filter, Score5Filter, LinuxScore5Filter, NetworkScore5Filter, OfficeScore5Filter, Score6Filter, LinuxScore6Filter, NetworkScore6Filter, Score7Filter, LinuxScore7Filter, NetworkScore7Filter, Score8Filter, LinuxScore8Filter, NetworkScore8Filter, Score9Filter, LinuxScore9Filter, NetworkScore9Filter, Score10Filter, LinuxScore10Filter

    
class PermissionViewSet(XadminViewSet):
    serializer_class = PermissionListSerializer
    queryset = Permission.objects.all().order_by('-pk')
    filter_class = PermissionFilter
    search_fields = ["name","codename"]

    def get_serializer_class(self):
        if self.action == "list":
            return PermissionListSerializer
        else:
            return PermissionCreateUpdateSerializer

    
class GroupViewSet(XadminViewSet):
    serializer_class = GroupListSerializer
    queryset = Group.objects.all().order_by('-pk')
    filter_class = GroupFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return GroupListSerializer
        else:
            return GroupCreateUpdateSerializer

    
class UserViewSet(XadminViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all().order_by('-pk')
    filter_class = UserFilter
    search_fields = ["password","username","first_name","last_name","email"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        else:
            return UserCreateUpdateSerializer

    
class ContentTypeViewSet(XadminViewSet):
    serializer_class = ContentTypeListSerializer
    queryset = ContentType.objects.all().order_by('-pk')
    filter_class = ContentTypeFilter
    search_fields = ["app_label","model"]

    def get_serializer_class(self):
        if self.action == "list":
            return ContentTypeListSerializer
        else:
            return ContentTypeCreateUpdateSerializer

    
class DepartmentViewSet(XadminViewSet):
    serializer_class = DepartmentListSerializer
    queryset = Department.objects.all().order_by('-pk')
    filter_class = DepartmentFilter
    search_fields = ["department"]

    def get_serializer_class(self):
        if self.action == "list":
            return DepartmentListSerializer
        else:
            return DepartmentCreateUpdateSerializer

    
class TeacherViewSet(XadminViewSet):
    serializer_class = TeacherListSerializer
    queryset = Teacher.objects.all().order_by('-pk')
    filter_class = TeacherFilter
    search_fields = ["name","gender","title","institute"]

    def get_serializer_class(self):
        if self.action == "list":
            return TeacherListSerializer
        else:
            return TeacherCreateUpdateSerializer

    
class StudentViewSet(XadminViewSet):
    serializer_class = StudentListSerializer
    queryset = Student.objects.all().order_by('-pk')
    filter_class = StudentFilter
    search_fields = ["name","gender","avatar","introduction"]

    def get_serializer_class(self):
        if self.action == "list":
            return StudentListSerializer
        else:
            return StudentCreateUpdateSerializer

    
class UserRolesInfoViewSet(XadminViewSet):
    serializer_class = UserRolesInfoListSerializer
    queryset = UserRolesInfo.objects.all().order_by('-pk')
    filter_class = UserRolesInfoFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserRolesInfoListSerializer
        else:
            return UserRolesInfoCreateUpdateSerializer

    
class PaperViewSet(XadminViewSet):
    serializer_class = PaperListSerializer
    queryset = Paper.objects.all().order_by('-pk')
    filter_class = PaperFilter
    search_fields = ["name","level"]

    def get_serializer_class(self):
        if self.action == "list":
            return PaperListSerializer
        else:
            return PaperCreateUpdateSerializer

    
class ExamViewSet(XadminViewSet):
    serializer_class = ExamListSerializer
    queryset = Exam.objects.all().order_by('-pk')
    filter_class = ExamFilter
    search_fields = ["name","major"]

    def get_serializer_class(self):
        if self.action == "list":
            return ExamListSerializer
        else:
            return ExamCreateUpdateSerializer

    
class GradeViewSet(XadminViewSet):
    serializer_class = GradeListSerializer
    queryset = Grade.objects.all().order_by('-pk')
    filter_class = GradeFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return GradeListSerializer
        else:
            return GradeCreateUpdateSerializer

    
class PracticeViewSet(XadminViewSet):
    serializer_class = PracticeListSerializer
    queryset = Practice.objects.all().order_by('-pk')
    filter_class = PracticeFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return PracticeListSerializer
        else:
            return PracticeCreateUpdateSerializer

    
class ChoiceViewSet(XadminViewSet):
    serializer_class = ChoiceListSerializer
    queryset = Choice.objects.all().order_by('-pk')
    filter_class = ChoiceFilter
    search_fields = ["answer_A","answer_B","answer_C","answer_D","right_answer","level"]

    def get_serializer_class(self):
        if self.action == "list":
            return ChoiceListSerializer
        else:
            return ChoiceCreateUpdateSerializer

    
class ChoiceMuViewSet(XadminViewSet):
    serializer_class = ChoiceMuListSerializer
    queryset = ChoiceMu.objects.all().order_by('-pk')
    filter_class = ChoiceMuFilter
    search_fields = ["answer_A","answer_B","answer_C","answer_D","right_answer","level"]

    def get_serializer_class(self):
        if self.action == "list":
            return ChoiceMuListSerializer
        else:
            return ChoiceMuCreateUpdateSerializer

    
class FillViewSet(XadminViewSet):
    serializer_class = FillListSerializer
    queryset = Fill.objects.all().order_by('-pk')
    filter_class = FillFilter
    search_fields = ["right_answer","level"]

    def get_serializer_class(self):
        if self.action == "list":
            return FillListSerializer
        else:
            return FillCreateUpdateSerializer

    
class JudgeViewSet(XadminViewSet):
    serializer_class = JudgeListSerializer
    queryset = Judge.objects.all().order_by('-pk')
    filter_class = JudgeFilter
    search_fields = ["right_answer","level"]

    def get_serializer_class(self):
        if self.action == "list":
            return JudgeListSerializer
        else:
            return JudgeCreateUpdateSerializer

    
class ProgramViewSet(XadminViewSet):
    serializer_class = ProgramListSerializer
    queryset = Program.objects.all().order_by('-pk')
    filter_class = ProgramFilter
    search_fields = ["level"]

    def get_serializer_class(self):
        if self.action == "list":
            return ProgramListSerializer
        else:
            return ProgramCreateUpdateSerializer

    
class ChoiceRecordViewSet(XadminViewSet):
    serializer_class = ChoiceRecordListSerializer
    queryset = ChoiceRecord.objects.all().order_by('-pk')
    filter_class = ChoiceRecordFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ChoiceRecordListSerializer
        else:
            return ChoiceRecordCreateUpdateSerializer

    
class ChoiceMuRecordViewSet(XadminViewSet):
    serializer_class = ChoiceMuRecordListSerializer
    queryset = ChoiceMuRecord.objects.all().order_by('-pk')
    filter_class = ChoiceMuRecordFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ChoiceMuRecordListSerializer
        else:
            return ChoiceMuRecordCreateUpdateSerializer

    
class FillRecordViewSet(XadminViewSet):
    serializer_class = FillRecordListSerializer
    queryset = FillRecord.objects.all().order_by('-pk')
    filter_class = FillRecordFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return FillRecordListSerializer
        else:
            return FillRecordCreateUpdateSerializer

    
class JudgeRecordViewSet(XadminViewSet):
    serializer_class = JudgeRecordListSerializer
    queryset = JudgeRecord.objects.all().order_by('-pk')
    filter_class = JudgeRecordFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return JudgeRecordListSerializer
        else:
            return JudgeRecordCreateUpdateSerializer

    
class ProgramRecordViewSet(XadminViewSet):
    serializer_class = ProgramRecordListSerializer
    queryset = ProgramRecord.objects.all().order_by('-pk')
    filter_class = ProgramRecordFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ProgramRecordListSerializer
        else:
            return ProgramRecordCreateUpdateSerializer

    
class LimitFileViewSet(XadminViewSet):
    serializer_class = LimitFileListSerializer
    queryset = LimitFile.objects.all().order_by('-pk')
    filter_class = LimitFileFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return LimitFileListSerializer
        else:
            return LimitFileCreateUpdateSerializer

    
class RandomFileIdViewSet(XadminViewSet):
    serializer_class = RandomFileIdListSerializer
    queryset = RandomFileId.objects.all().order_by('-pk')
    filter_class = RandomFileIdFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return RandomFileIdListSerializer
        else:
            return RandomFileIdCreateUpdateSerializer

    
class FilesViewSet(XadminViewSet):
    serializer_class = FilesListSerializer
    queryset = Files.objects.all().order_by('-pk')
    filter_class = FilesFilter
    search_fields = ["name","downloadfile","finger"]

    def get_serializer_class(self):
        if self.action == "list":
            return FilesListSerializer
        else:
            return FilesCreateUpdateSerializer

    
class PersonalGradeFilesViewSet(XadminViewSet):
    serializer_class = PersonalGradeFilesListSerializer
    queryset = PersonalGradeFiles.objects.all().order_by('-pk')
    filter_class = PersonalGradeFilesFilter
    search_fields = ["name","downloadfile"]

    def get_serializer_class(self):
        if self.action == "list":
            return PersonalGradeFilesListSerializer
        else:
            return PersonalGradeFilesCreateUpdateSerializer

    
class CaptainFilesViewSet(XadminViewSet):
    serializer_class = CaptainFilesListSerializer
    queryset = CaptainFiles.objects.all().order_by('-pk')
    filter_class = CaptainFilesFilter
    search_fields = ["name","downloadfile","finger"]

    def get_serializer_class(self):
        if self.action == "list":
            return CaptainFilesListSerializer
        else:
            return CaptainFilesCreateUpdateSerializer

    
class ExamFilesViewSet(XadminViewSet):
    serializer_class = ExamFilesListSerializer
    queryset = ExamFiles.objects.all().order_by('-pk')
    filter_class = ExamFilesFilter
    search_fields = ["name","downloadfile","exam_questions_type"]

    def get_serializer_class(self):
        if self.action == "list":
            return ExamFilesListSerializer
        else:
            return ExamFilesCreateUpdateSerializer

    
class JudgeFilesViewSet(XadminViewSet):
    serializer_class = JudgeFilesListSerializer
    queryset = JudgeFiles.objects.all().order_by('-pk')
    filter_class = JudgeFilesFilter
    search_fields = ["name","downloadfile"]

    def get_serializer_class(self):
        if self.action == "list":
            return JudgeFilesListSerializer
        else:
            return JudgeFilesCreateUpdateSerializer

    
class Score3ViewSet(XadminViewSet):
    serializer_class = Score3ListSerializer
    queryset = Score3.objects.all().order_by('-pk')
    filter_class = Score3Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return Score3ListSerializer
        else:
            return Score3CreateUpdateSerializer

    
class LinuxScore3ViewSet(XadminViewSet):
    serializer_class = LinuxScore3ListSerializer
    queryset = LinuxScore3.objects.all().order_by('-pk')
    filter_class = LinuxScore3Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return LinuxScore3ListSerializer
        else:
            return LinuxScore3CreateUpdateSerializer

    
class NetworkScore3ViewSet(XadminViewSet):
    serializer_class = NetworkScore3ListSerializer
    queryset = NetworkScore3.objects.all().order_by('-pk')
    filter_class = NetworkScore3Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return NetworkScore3ListSerializer
        else:
            return NetworkScore3CreateUpdateSerializer

    
class OfficeScore3ViewSet(XadminViewSet):
    serializer_class = OfficeScore3ListSerializer
    queryset = OfficeScore3.objects.all().order_by('-pk')
    filter_class = OfficeScore3Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return OfficeScore3ListSerializer
        else:
            return OfficeScore3CreateUpdateSerializer

    
class Score4ViewSet(XadminViewSet):
    serializer_class = Score4ListSerializer
    queryset = Score4.objects.all().order_by('-pk')
    filter_class = Score4Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return Score4ListSerializer
        else:
            return Score4CreateUpdateSerializer

    
class LinuxScore4ViewSet(XadminViewSet):
    serializer_class = LinuxScore4ListSerializer
    queryset = LinuxScore4.objects.all().order_by('-pk')
    filter_class = LinuxScore4Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return LinuxScore4ListSerializer
        else:
            return LinuxScore4CreateUpdateSerializer

    
class NetworkScore4ViewSet(XadminViewSet):
    serializer_class = NetworkScore4ListSerializer
    queryset = NetworkScore4.objects.all().order_by('-pk')
    filter_class = NetworkScore4Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return NetworkScore4ListSerializer
        else:
            return NetworkScore4CreateUpdateSerializer

    
class OfficeScore4ViewSet(XadminViewSet):
    serializer_class = OfficeScore4ListSerializer
    queryset = OfficeScore4.objects.all().order_by('-pk')
    filter_class = OfficeScore4Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return OfficeScore4ListSerializer
        else:
            return OfficeScore4CreateUpdateSerializer

    
class Score5ViewSet(XadminViewSet):
    serializer_class = Score5ListSerializer
    queryset = Score5.objects.all().order_by('-pk')
    filter_class = Score5Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return Score5ListSerializer
        else:
            return Score5CreateUpdateSerializer

    
class LinuxScore5ViewSet(XadminViewSet):
    serializer_class = LinuxScore5ListSerializer
    queryset = LinuxScore5.objects.all().order_by('-pk')
    filter_class = LinuxScore5Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return LinuxScore5ListSerializer
        else:
            return LinuxScore5CreateUpdateSerializer

    
class NetworkScore5ViewSet(XadminViewSet):
    serializer_class = NetworkScore5ListSerializer
    queryset = NetworkScore5.objects.all().order_by('-pk')
    filter_class = NetworkScore5Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return NetworkScore5ListSerializer
        else:
            return NetworkScore5CreateUpdateSerializer

    
class OfficeScore5ViewSet(XadminViewSet):
    serializer_class = OfficeScore5ListSerializer
    queryset = OfficeScore5.objects.all().order_by('-pk')
    filter_class = OfficeScore5Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return OfficeScore5ListSerializer
        else:
            return OfficeScore5CreateUpdateSerializer

    
class Score6ViewSet(XadminViewSet):
    serializer_class = Score6ListSerializer
    queryset = Score6.objects.all().order_by('-pk')
    filter_class = Score6Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return Score6ListSerializer
        else:
            return Score6CreateUpdateSerializer

    
class LinuxScore6ViewSet(XadminViewSet):
    serializer_class = LinuxScore6ListSerializer
    queryset = LinuxScore6.objects.all().order_by('-pk')
    filter_class = LinuxScore6Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return LinuxScore6ListSerializer
        else:
            return LinuxScore6CreateUpdateSerializer

    
class NetworkScore6ViewSet(XadminViewSet):
    serializer_class = NetworkScore6ListSerializer
    queryset = NetworkScore6.objects.all().order_by('-pk')
    filter_class = NetworkScore6Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return NetworkScore6ListSerializer
        else:
            return NetworkScore6CreateUpdateSerializer

    
class Score7ViewSet(XadminViewSet):
    serializer_class = Score7ListSerializer
    queryset = Score7.objects.all().order_by('-pk')
    filter_class = Score7Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return Score7ListSerializer
        else:
            return Score7CreateUpdateSerializer

    
class LinuxScore7ViewSet(XadminViewSet):
    serializer_class = LinuxScore7ListSerializer
    queryset = LinuxScore7.objects.all().order_by('-pk')
    filter_class = LinuxScore7Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return LinuxScore7ListSerializer
        else:
            return LinuxScore7CreateUpdateSerializer

    
class NetworkScore7ViewSet(XadminViewSet):
    serializer_class = NetworkScore7ListSerializer
    queryset = NetworkScore7.objects.all().order_by('-pk')
    filter_class = NetworkScore7Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return NetworkScore7ListSerializer
        else:
            return NetworkScore7CreateUpdateSerializer

    
class Score8ViewSet(XadminViewSet):
    serializer_class = Score8ListSerializer
    queryset = Score8.objects.all().order_by('-pk')
    filter_class = Score8Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return Score8ListSerializer
        else:
            return Score8CreateUpdateSerializer

    
class LinuxScore8ViewSet(XadminViewSet):
    serializer_class = LinuxScore8ListSerializer
    queryset = LinuxScore8.objects.all().order_by('-pk')
    filter_class = LinuxScore8Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return LinuxScore8ListSerializer
        else:
            return LinuxScore8CreateUpdateSerializer

    
class NetworkScore8ViewSet(XadminViewSet):
    serializer_class = NetworkScore8ListSerializer
    queryset = NetworkScore8.objects.all().order_by('-pk')
    filter_class = NetworkScore8Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return NetworkScore8ListSerializer
        else:
            return NetworkScore8CreateUpdateSerializer

    
class Score9ViewSet(XadminViewSet):
    serializer_class = Score9ListSerializer
    queryset = Score9.objects.all().order_by('-pk')
    filter_class = Score9Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return Score9ListSerializer
        else:
            return Score9CreateUpdateSerializer

    
class LinuxScore9ViewSet(XadminViewSet):
    serializer_class = LinuxScore9ListSerializer
    queryset = LinuxScore9.objects.all().order_by('-pk')
    filter_class = LinuxScore9Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return LinuxScore9ListSerializer
        else:
            return LinuxScore9CreateUpdateSerializer

    
class NetworkScore9ViewSet(XadminViewSet):
    serializer_class = NetworkScore9ListSerializer
    queryset = NetworkScore9.objects.all().order_by('-pk')
    filter_class = NetworkScore9Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return NetworkScore9ListSerializer
        else:
            return NetworkScore9CreateUpdateSerializer

    
class Score10ViewSet(XadminViewSet):
    serializer_class = Score10ListSerializer
    queryset = Score10.objects.all().order_by('-pk')
    filter_class = Score10Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return Score10ListSerializer
        else:
            return Score10CreateUpdateSerializer

    
class LinuxScore10ViewSet(XadminViewSet):
    serializer_class = LinuxScore10ListSerializer
    queryset = LinuxScore10.objects.all().order_by('-pk')
    filter_class = LinuxScore10Filter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return LinuxScore10ListSerializer
        else:
            return LinuxScore10CreateUpdateSerializer
