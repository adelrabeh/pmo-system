from common.mixins import SecureModelViewSet
from .models import Department, ProjectStatus, ProjectPhase, ProjectPriority, SeverityLevel, ProbabilityLevel, ImpactLevel, ChangeDecisionStatus
from .serializers import DepartmentSerializer, ProjectStatusSerializer, ProjectPhaseSerializer, ProjectPrioritySerializer, SeverityLevelSerializer, ProbabilityLevelSerializer, ImpactLevelSerializer, ChangeDecisionStatusSerializer
class DepartmentViewSet(SecureModelViewSet): queryset=Department.objects.all(); serializer_class=DepartmentSerializer
class ProjectStatusViewSet(SecureModelViewSet): queryset=ProjectStatus.objects.all(); serializer_class=ProjectStatusSerializer
class ProjectPhaseViewSet(SecureModelViewSet): queryset=ProjectPhase.objects.all(); serializer_class=ProjectPhaseSerializer
class ProjectPriorityViewSet(SecureModelViewSet): queryset=ProjectPriority.objects.all(); serializer_class=ProjectPrioritySerializer
class SeverityLevelViewSet(SecureModelViewSet): queryset=SeverityLevel.objects.all(); serializer_class=SeverityLevelSerializer
class ProbabilityLevelViewSet(SecureModelViewSet): queryset=ProbabilityLevel.objects.all(); serializer_class=ProbabilityLevelSerializer
class ImpactLevelViewSet(SecureModelViewSet): queryset=ImpactLevel.objects.all(); serializer_class=ImpactLevelSerializer
class ChangeDecisionStatusViewSet(SecureModelViewSet): queryset=ChangeDecisionStatus.objects.all(); serializer_class=ChangeDecisionStatusSerializer
