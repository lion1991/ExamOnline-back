from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from question.models import Program
from record.models import ChoiceRecord, FillRecord, JudgeRecord, ProgramRecord, ChoiceMuRecord
from record.serializers import ChoiceRecordSerializer, FillRecordSerializer, JudgeRecordSerializer, \
    ProgramRecordSerializer, ChoiceMuRecordSerializer


class ChoiceRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """单选题练习记录"""
    authentication_classes = []
    permission_classes = []
    # 数据集
    queryset = ChoiceRecord.objects.all()
    # 序列化
    serializer_class = ChoiceRecordSerializer

    def get_queryset(self):
        # 模拟练习ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = ChoiceRecord.objects.filter(practice_id=practice_id)
        return self.queryset

class ChoiceMuRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """多选题练习记录"""
    authentication_classes = []
    permission_classes = []
    # 数据集
    queryset = ChoiceMuRecord.objects.all()
    # 序列化
    serializer_class = ChoiceMuRecordSerializer

    def get_queryset(self):
        # 模拟练习ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = ChoiceMuRecord.objects.filter(practice_id=practice_id)
        return self.queryset


class FillRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """填空题练习记录"""
    authentication_classes = []
    permission_classes = []
    # 数据集
    queryset = FillRecord.objects.all()
    # 序列化
    serializer_class = FillRecordSerializer

    def get_queryset(self):
        # 模拟练习ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = FillRecord.objects.filter(practice_id=practice_id)
        return self.queryset


class JudgeRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """判断题练习记录"""
    authentication_classes = []
    permission_classes = []
    # 数据集
    queryset = JudgeRecord.objects.all()
    # 序列化
    serializer_class = JudgeRecordSerializer

    def get_queryset(self):
        # 模拟练习ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = JudgeRecord.objects.filter(practice_id=practice_id)
        return self.queryset


class ProgramRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """编程题练习记录"""
    # 数据集
    queryset = ProgramRecord.objects.all()
    # 序列化
    serializer_class = ProgramRecordSerializer

    def get_queryset(self):
        # 模拟练习ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = ProgramRecord.objects.filter(practice_id=practice_id)
        return self.queryset
