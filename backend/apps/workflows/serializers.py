from rest_framework import serializers
from .models import WorkflowTemplate, WorkflowStep, WorkflowInstance, WorkflowAction
class WorkflowStepSerializer(serializers.ModelSerializer):
    class Meta: model=WorkflowStep; fields="__all__"
class WorkflowTemplateSerializer(serializers.ModelSerializer):
    steps=WorkflowStepSerializer(many=True, read_only=True)
    class Meta: model=WorkflowTemplate; fields="__all__"
class WorkflowActionSerializer(serializers.ModelSerializer):
    class Meta: model=WorkflowAction; fields="__all__"
class WorkflowInstanceSerializer(serializers.ModelSerializer):
    actions=WorkflowActionSerializer(many=True, read_only=True)
    class Meta: model=WorkflowInstance; fields="__all__"
