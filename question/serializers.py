from rest_framework import serializers

from question.models import Choice, Fill, Judge, Program, ChoiceMu


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
#mu

class ChoiceMuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceMu
        fields = '__all__'

class FillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fill
        fields = '__all__'


class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
