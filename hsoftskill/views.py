from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, generics

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
