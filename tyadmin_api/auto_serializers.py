from rest_framework import serializers
from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from user.models import Department, Teacher, Student, UserRolesInfo
from exam.models import Paper, Exam, Grade, Practice
from question.models import Choice, ChoiceMu, Fill, Judge, Program
from record.models import ChoiceRecord, ChoiceMuRecord, FillRecord, JudgeRecord, ProgramRecord
from hsoftskill.models import LimitFile, RandomFileId, Files, PersonalGradeFiles, CaptainFiles, ExamFiles, JudgeFiles, Score3, LinuxScore3, NetworkScore3, OfficeScore3, Score4, LinuxScore4, NetworkScore4, OfficeScore4, Score5, LinuxScore5, NetworkScore5, OfficeScore5, Score6, LinuxScore6, NetworkScore6, Score7, LinuxScore7, NetworkScore7, Score8, LinuxScore8, NetworkScore8, Score9, LinuxScore9, NetworkScore9, Score10, LinuxScore10


class ContentTypeListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ContentType
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ContentTypeCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ContentType
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class DepartmentListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class DepartmentCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class PaperListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Paper
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class PaperCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Paper
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ChoiceListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ChoiceCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ChoiceMuListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ChoiceMu
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ChoiceMuCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ChoiceMu
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class FillListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Fill
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class FillCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Fill
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class JudgeListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Judge
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class JudgeCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Judge
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ProgramListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ProgramCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LimitFileListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LimitFile
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LimitFileCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LimitFile
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score3ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score3
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score3CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score3
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore3ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore3
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore3CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore3
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore3ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore3
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore3CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore3
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class OfficeScore3ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = OfficeScore3
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class OfficeScore3CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = OfficeScore3
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score4ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score4
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score4CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score4
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore4ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore4
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore4CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore4
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore4ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore4
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore4CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore4
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class OfficeScore4ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = OfficeScore4
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class OfficeScore4CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = OfficeScore4
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score5ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score5
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score5CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score5
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore5ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore5
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore5CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore5
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore5ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore5
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore5CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore5
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class OfficeScore5ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = OfficeScore5
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class OfficeScore5CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = OfficeScore5
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score6ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score6
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score6CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score6
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore6ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore6
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore6CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore6
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore6ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore6
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore6CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore6
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score7ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score7
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score7CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score7
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore7ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore7
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore7CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore7
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore7ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore7
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore7CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore7
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score8ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score8
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score8CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score8
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore8ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore8
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore8CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore8
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore8ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore8
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore8CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore8
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score9ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score9
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score9CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score9
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore9ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore9
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore9CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore9
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore9ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore9
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class NetworkScore9CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = NetworkScore9
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score10ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score10
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class Score10CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Score10
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore10ListSerializer(serializers.ModelSerializer):
    

    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore10
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class LinuxScore10CreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = LinuxScore10
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class PermissionListSerializer(serializers.ModelSerializer):
    

    class ContentTypeSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = ContentType
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    content_type = ContentTypeSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Permission
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class PermissionCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Permission
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class GroupListSerializer(serializers.ModelSerializer):
    

    class PermissionSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Permission
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    permissions = PermissionSerializer(many=True)
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class GroupCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class UserListSerializer(serializers.ModelSerializer):
    

    class GroupSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Group
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    groups = GroupSerializer(many=True)
    class PermissionSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Permission
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    user_permissions = PermissionSerializer(many=True)
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_password(self.validated_data['password'])
        instance.save()
        return instance        
        

class TeacherListSerializer(serializers.ModelSerializer):
    

    class UserSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = User
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    user = UserSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class TeacherCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class StudentListSerializer(serializers.ModelSerializer):
    

    class UserSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = User
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    user = UserSerializer()
    class DepartmentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Department
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    department = DepartmentSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class StudentCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class UserRolesInfoListSerializer(serializers.ModelSerializer):
    

    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    roles_student = StudentSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = UserRolesInfo
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class UserRolesInfoCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = UserRolesInfo
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ExamListSerializer(serializers.ModelSerializer):
    

    class PaperSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Paper
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    paper = PaperSerializer()
    class DepartmentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Department
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    department = DepartmentSerializer(many=True)
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ExamCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class GradeListSerializer(serializers.ModelSerializer):
    

    class ExamSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Exam
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    exam = ExamSerializer()
    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    student = StudentSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Grade
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class GradeCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Grade
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class PracticeListSerializer(serializers.ModelSerializer):
    

    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    student = StudentSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Practice
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class PracticeCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Practice
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ChoiceRecordListSerializer(serializers.ModelSerializer):
    

    class PracticeSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Practice
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    practice = PracticeSerializer()
    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    student = StudentSerializer()
    class ChoiceSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Choice
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    choice = ChoiceSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ChoiceRecord
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ChoiceRecordCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ChoiceRecord
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ChoiceMuRecordListSerializer(serializers.ModelSerializer):
    

    class PracticeSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Practice
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    practice = PracticeSerializer()
    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    student = StudentSerializer()
    class ChoiceMuSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = ChoiceMu
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    choicemu = ChoiceMuSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ChoiceMuRecord
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ChoiceMuRecordCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ChoiceMuRecord
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class FillRecordListSerializer(serializers.ModelSerializer):
    

    class PracticeSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Practice
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    practice = PracticeSerializer()
    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    student = StudentSerializer()
    class FillSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Fill
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    fill = FillSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = FillRecord
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class FillRecordCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = FillRecord
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class JudgeRecordListSerializer(serializers.ModelSerializer):
    

    class PracticeSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Practice
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    practice = PracticeSerializer()
    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    student = StudentSerializer()
    class JudgeSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Judge
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    judge = JudgeSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = JudgeRecord
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class JudgeRecordCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = JudgeRecord
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ProgramRecordListSerializer(serializers.ModelSerializer):
    

    class PracticeSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Practice
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    practice = PracticeSerializer()
    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    student = StudentSerializer()
    class ProgramSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Program
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    program = ProgramSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ProgramRecord
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ProgramRecordCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ProgramRecord
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class RandomFileIdListSerializer(serializers.ModelSerializer):
    

    class LimitFileSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = LimitFile
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    period = LimitFileSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = RandomFileId
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class RandomFileIdCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = RandomFileId
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class FilesListSerializer(serializers.ModelSerializer):
    

    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    uploader = StudentSerializer()
    class LimitFileSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = LimitFile
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    limit_period = LimitFileSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Files
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class FilesCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = Files
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class PersonalGradeFilesListSerializer(serializers.ModelSerializer):
    

    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    uploader = StudentSerializer()
    class LimitFileSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = LimitFile
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    limit_period = LimitFileSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = PersonalGradeFiles
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class PersonalGradeFilesCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = PersonalGradeFiles
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class CaptainFilesListSerializer(serializers.ModelSerializer):
    

    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    uploader = StudentSerializer()
    class LimitFileSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = LimitFile
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    limit_period = LimitFileSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = CaptainFiles
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class CaptainFilesCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = CaptainFiles
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ExamFilesListSerializer(serializers.ModelSerializer):
    

    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    uploader = StudentSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ExamFiles
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class ExamFilesCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = ExamFiles
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class JudgeFilesListSerializer(serializers.ModelSerializer):
    

    class StudentSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = Student
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    uploader = StudentSerializer()
    class LimitFileSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()
        class Meta:
            model = LimitFile
            fields = "__all__"
        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)
    limit_period = LimitFileSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = JudgeFiles
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class JudgeFilesCreateUpdateSerializer(serializers.ModelSerializer):
    
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = JudgeFiles
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)
