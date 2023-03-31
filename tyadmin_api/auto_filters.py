from django_filters import rest_framework as filters
from tyadmin_api.custom import DateFromToRangeFilter
from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from user.models import Department, Teacher, Student, UserRolesInfo
from exam.models import Paper, Exam, Grade, Practice
from question.models import Choice, ChoiceMu, Fill, Judge, Program
from record.models import ChoiceRecord, ChoiceMuRecord, FillRecord, JudgeRecord, ProgramRecord
from hsoftskill.models import LimitFile, RandomFileId, Files, PersonalGradeFiles, CaptainFiles, ExamFiles, JudgeFiles, Score3, LinuxScore3, NetworkScore3, OfficeScore3, Score4, LinuxScore4, NetworkScore4, OfficeScore4, Score5, LinuxScore5, NetworkScore5, OfficeScore5, Score6, LinuxScore6, NetworkScore6, Score7, LinuxScore7, NetworkScore7, Score8, LinuxScore8, NetworkScore8, Score9, LinuxScore9, NetworkScore9, Score10, LinuxScore10

class PermissionFilter(filters.FilterSet):
    content_type_text = filters.CharFilter(field_name="content_type")

    class Meta:
        model = Permission
        exclude = []

class GroupFilter(filters.FilterSet):

    class Meta:
        model = Group
        exclude = []

class UserFilter(filters.FilterSet):
    last_login = DateFromToRangeFilter(field_name="last_login")
    date_joined = DateFromToRangeFilter(field_name="date_joined")

    class Meta:
        model = User
        exclude = []

class ContentTypeFilter(filters.FilterSet):

    class Meta:
        model = ContentType
        exclude = []

class DepartmentFilter(filters.FilterSet):

    class Meta:
        model = Department
        exclude = []

class TeacherFilter(filters.FilterSet):
    user_text = filters.CharFilter(field_name="user")

    class Meta:
        model = Teacher
        exclude = []

class StudentFilter(filters.FilterSet):
    user_text = filters.CharFilter(field_name="user")
    department_text = filters.CharFilter(field_name="department")

    class Meta:
        model = Student
        exclude = []

class UserRolesInfoFilter(filters.FilterSet):
    roles_student_text = filters.CharFilter(field_name="roles_student")

    class Meta:
        model = UserRolesInfo
        exclude = []

class PaperFilter(filters.FilterSet):

    class Meta:
        model = Paper
        exclude = []

class ExamFilter(filters.FilterSet):
    paper_text = filters.CharFilter(field_name="paper")

    class Meta:
        model = Exam
        exclude = []

class GradeFilter(filters.FilterSet):
    exam_text = filters.CharFilter(field_name="exam")
    student_text = filters.CharFilter(field_name="student")
    create_time = DateFromToRangeFilter(field_name="create_time")
    update_time = DateFromToRangeFilter(field_name="update_time")

    class Meta:
        model = Grade
        exclude = []

class PracticeFilter(filters.FilterSet):
    student_text = filters.CharFilter(field_name="student")
    create_time = DateFromToRangeFilter(field_name="create_time")

    class Meta:
        model = Practice
        exclude = []

class ChoiceFilter(filters.FilterSet):

    class Meta:
        model = Choice
        exclude = []

class ChoiceMuFilter(filters.FilterSet):

    class Meta:
        model = ChoiceMu
        exclude = []

class FillFilter(filters.FilterSet):

    class Meta:
        model = Fill
        exclude = []

class JudgeFilter(filters.FilterSet):

    class Meta:
        model = Judge
        exclude = []

class ProgramFilter(filters.FilterSet):

    class Meta:
        model = Program
        exclude = []

class ChoiceRecordFilter(filters.FilterSet):
    practice_text = filters.CharFilter(field_name="practice")
    student_text = filters.CharFilter(field_name="student")
    choice_text = filters.CharFilter(field_name="choice")

    class Meta:
        model = ChoiceRecord
        exclude = []

class ChoiceMuRecordFilter(filters.FilterSet):
    practice_text = filters.CharFilter(field_name="practice")
    student_text = filters.CharFilter(field_name="student")
    choicemu_text = filters.CharFilter(field_name="choicemu")

    class Meta:
        model = ChoiceMuRecord
        exclude = []

class FillRecordFilter(filters.FilterSet):
    practice_text = filters.CharFilter(field_name="practice")
    student_text = filters.CharFilter(field_name="student")
    fill_text = filters.CharFilter(field_name="fill")

    class Meta:
        model = FillRecord
        exclude = []

class JudgeRecordFilter(filters.FilterSet):
    practice_text = filters.CharFilter(field_name="practice")
    student_text = filters.CharFilter(field_name="student")
    judge_text = filters.CharFilter(field_name="judge")

    class Meta:
        model = JudgeRecord
        exclude = []

class ProgramRecordFilter(filters.FilterSet):
    practice_text = filters.CharFilter(field_name="practice")
    student_text = filters.CharFilter(field_name="student")
    program_text = filters.CharFilter(field_name="program")

    class Meta:
        model = ProgramRecord
        exclude = []

class LimitFileFilter(filters.FilterSet):

    class Meta:
        model = LimitFile
        exclude = []

class RandomFileIdFilter(filters.FilterSet):
    period_text = filters.CharFilter(field_name="period")

    class Meta:
        model = RandomFileId
        exclude = []

class FilesFilter(filters.FilterSet):
    uploader_text = filters.CharFilter(field_name="uploader")
    limit_period_text = filters.CharFilter(field_name="limit_period")
    upload_time = DateFromToRangeFilter(field_name="upload_time")

    class Meta:
        model = Files
        exclude = ["file"]

class PersonalGradeFilesFilter(filters.FilterSet):
    uploader_text = filters.CharFilter(field_name="uploader")
    limit_period_text = filters.CharFilter(field_name="limit_period")
    upload_time = DateFromToRangeFilter(field_name="upload_time")

    class Meta:
        model = PersonalGradeFiles
        exclude = ["file"]

class CaptainFilesFilter(filters.FilterSet):
    uploader_text = filters.CharFilter(field_name="uploader")
    limit_period_text = filters.CharFilter(field_name="limit_period")
    upload_time = DateFromToRangeFilter(field_name="upload_time")

    class Meta:
        model = CaptainFiles
        exclude = ["file"]

class ExamFilesFilter(filters.FilterSet):
    uploader_text = filters.CharFilter(field_name="uploader")
    upload_time = DateFromToRangeFilter(field_name="upload_time")

    class Meta:
        model = ExamFiles
        exclude = ["file"]

class JudgeFilesFilter(filters.FilterSet):
    uploader_text = filters.CharFilter(field_name="uploader")
    limit_period_text = filters.CharFilter(field_name="limit_period")
    upload_time = DateFromToRangeFilter(field_name="upload_time")

    class Meta:
        model = JudgeFiles
        exclude = ["file"]

class Score3Filter(filters.FilterSet):

    class Meta:
        model = Score3
        exclude = []

class LinuxScore3Filter(filters.FilterSet):

    class Meta:
        model = LinuxScore3
        exclude = []

class NetworkScore3Filter(filters.FilterSet):

    class Meta:
        model = NetworkScore3
        exclude = []

class OfficeScore3Filter(filters.FilterSet):

    class Meta:
        model = OfficeScore3
        exclude = []

class Score4Filter(filters.FilterSet):

    class Meta:
        model = Score4
        exclude = []

class LinuxScore4Filter(filters.FilterSet):

    class Meta:
        model = LinuxScore4
        exclude = []

class NetworkScore4Filter(filters.FilterSet):

    class Meta:
        model = NetworkScore4
        exclude = []

class OfficeScore4Filter(filters.FilterSet):

    class Meta:
        model = OfficeScore4
        exclude = []

class Score5Filter(filters.FilterSet):

    class Meta:
        model = Score5
        exclude = []

class LinuxScore5Filter(filters.FilterSet):

    class Meta:
        model = LinuxScore5
        exclude = []

class NetworkScore5Filter(filters.FilterSet):

    class Meta:
        model = NetworkScore5
        exclude = []

class OfficeScore5Filter(filters.FilterSet):

    class Meta:
        model = OfficeScore5
        exclude = []

class Score6Filter(filters.FilterSet):

    class Meta:
        model = Score6
        exclude = []

class LinuxScore6Filter(filters.FilterSet):

    class Meta:
        model = LinuxScore6
        exclude = []

class NetworkScore6Filter(filters.FilterSet):

    class Meta:
        model = NetworkScore6
        exclude = []

class Score7Filter(filters.FilterSet):

    class Meta:
        model = Score7
        exclude = []

class LinuxScore7Filter(filters.FilterSet):

    class Meta:
        model = LinuxScore7
        exclude = []

class NetworkScore7Filter(filters.FilterSet):

    class Meta:
        model = NetworkScore7
        exclude = []

class Score8Filter(filters.FilterSet):

    class Meta:
        model = Score8
        exclude = []

class LinuxScore8Filter(filters.FilterSet):

    class Meta:
        model = LinuxScore8
        exclude = []

class NetworkScore8Filter(filters.FilterSet):

    class Meta:
        model = NetworkScore8
        exclude = []

class Score9Filter(filters.FilterSet):

    class Meta:
        model = Score9
        exclude = []

class LinuxScore9Filter(filters.FilterSet):

    class Meta:
        model = LinuxScore9
        exclude = []

class NetworkScore9Filter(filters.FilterSet):

    class Meta:
        model = NetworkScore9
        exclude = []

class Score10Filter(filters.FilterSet):

    class Meta:
        model = Score10
        exclude = []

class LinuxScore10Filter(filters.FilterSet):

    class Meta:
        model = LinuxScore10
        exclude = []