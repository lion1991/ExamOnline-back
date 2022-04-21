from rest_framework import serializers

from exam.models import Practice
from exam.serializers import PracticeSerializer
from question.models import Choice, Fill, Judge, Program, ChoiceMu
from question.serializers import ChoiceSerializer, FillSerializer, JudgeSerializer, ProgramSerializer, \
    ChoiceMuSerializer
from record.models import ChoiceRecord, FillRecord, ProgramRecord, JudgeRecord, ChoiceMuRecord
from hsoftskill.models import Files

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'
        # exclude = ('create_time', 'is_delete')
