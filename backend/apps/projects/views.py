from rest_framework.decorators import action
from rest_framework.response import Response
from common.mixins import SecureModelViewSet
from .models import Project, ProjectRisk, ProjectIssue, ProjectChangeRequest
from .serializers import ProjectSerializer, ProjectRiskSerializer, ProjectIssueSerializer, ProjectChangeRequestSerializer
from .services import project_dashboard_payload
class ProjectViewSet(SecureModelViewSet):
    queryset=Project.objects.select_related("owning_department","status","phase","priority","sponsor","owner","manager").prefetch_related("budgets","risks","issues","change_requests")
    serializer_class=ProjectSerializer
    search_fields=["project_code","project_name_ar","description"]
    @action(detail=True, methods=["get"])
    def dashboard(self, request, pk=None):
        return Response(project_dashboard_payload(self.get_object()))
class ProjectRiskViewSet(SecureModelViewSet): queryset=ProjectRisk.objects.all(); serializer_class=ProjectRiskSerializer
class ProjectIssueViewSet(SecureModelViewSet): queryset=ProjectIssue.objects.all(); serializer_class=ProjectIssueSerializer
class ProjectChangeRequestViewSet(SecureModelViewSet): queryset=ProjectChangeRequest.objects.all(); serializer_class=ProjectChangeRequestSerializer
