from rest_framework import serializers
from .models import Project, ProjectBudget, ProjectRisk, ProjectIssue, ProjectChangeRequest
class ProjectBudgetSerializer(serializers.ModelSerializer):
    class Meta: model=ProjectBudget; fields="__all__"
class ProjectRiskSerializer(serializers.ModelSerializer):
    severity_name=serializers.CharField(source="severity.name_ar", read_only=True)
    class Meta: model=ProjectRisk; fields="__all__"
class ProjectIssueSerializer(serializers.ModelSerializer):
    severity_name=serializers.CharField(source="severity.name_ar", read_only=True)
    class Meta: model=ProjectIssue; fields="__all__"
class ProjectChangeRequestSerializer(serializers.ModelSerializer):
    class Meta: model=ProjectChangeRequest; fields="__all__"
class ProjectSerializer(serializers.ModelSerializer):
    status_name=serializers.CharField(source="status.name_ar", read_only=True)
    phase_name=serializers.CharField(source="phase.name_ar", read_only=True)
    risks=ProjectRiskSerializer(many=True, read_only=True)
    issues=ProjectIssueSerializer(many=True, read_only=True)
    change_requests=ProjectChangeRequestSerializer(many=True, read_only=True)
    budgets=ProjectBudgetSerializer(many=True, read_only=True)
    class Meta: model=Project; fields="__all__"
