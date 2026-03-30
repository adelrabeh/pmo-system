from rest_framework import serializers
from .models import Department, ProjectStatus, ProjectPhase, ProjectPriority, SeverityLevel, ProbabilityLevel, ImpactLevel, ChangeDecisionStatus
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta: model = Department; fields=["id","name_ar"]
class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta: model = ProjectStatus; fields=["id","name_ar","color_hex","sort_order"]
class ProjectPhaseSerializer(serializers.ModelSerializer):
    class Meta: model = ProjectPhase; fields=["id","name_ar","sort_order"]
class ProjectPrioritySerializer(serializers.ModelSerializer):
    class Meta: model = ProjectPriority; fields=["id","name_ar","weight"]
class SeverityLevelSerializer(serializers.ModelSerializer):
    class Meta: model = SeverityLevel; fields=["id","name_ar","weight"]
class ProbabilityLevelSerializer(serializers.ModelSerializer):
    class Meta: model = ProbabilityLevel; fields=["id","name_ar","weight"]
class ImpactLevelSerializer(serializers.ModelSerializer):
    class Meta: model = ImpactLevel; fields=["id","name_ar","weight"]
class ChangeDecisionStatusSerializer(serializers.ModelSerializer):
    class Meta: model = ChangeDecisionStatus; fields=["id","name_ar"]
