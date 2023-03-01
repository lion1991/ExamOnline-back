from rest_framework import serializers

from exam.models import Practice
from exam.serializers import PracticeSerializer
from question.models import Choice, Fill, Judge, Program, ChoiceMu
from question.serializers import ChoiceSerializer, FillSerializer, JudgeSerializer, ProgramSerializer, \
    ChoiceMuSerializer
from record.models import ChoiceRecord, FillRecord, ProgramRecord, JudgeRecord, ChoiceMuRecord
from hsoftskill.models import Files, LimitFile, RandomFileId, CaptainFiles, ExamFiles, JudgeFiles, PersonalGradeFiles


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'
        # exclude = ('create_time', 'is_delete')

class FilePersonSerializer(serializers.ModelSerializer):
    uploader = serializers.ReadOnlyField(source="uploader.name")
    class Meta:
        model = Files
        fields = ('uploader',)

class PersonalGradeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalGradeFiles
        fields = '__all__'

class CaptainFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptainFiles
        fields = '__all__'

class LimitFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LimitFile
        fields = '__all__'
        # exclude = ('create_time', 'is_delete')

class RandomFileIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomFileId
        fields = '__all__'
        # exclude = ('create_time', 'is_delete')

class ExamFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamFiles
        fields = '__all__'
        # exclude = ('create_time', 'is_delete')

class JudgeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudgeFiles
        fields = '__all__'
        # exclude = ('create_time', 'is_delete')