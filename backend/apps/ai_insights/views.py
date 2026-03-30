from rest_framework.decorators import action
from rest_framework.response import Response
from common.mixins import SecureModelViewSet
from apps.projects.models import Project
from .models import AIProjectInsight
from .serializers import AIProjectInsightSerializer
from .services import generate_mock_insight
class AIProjectInsightViewSet(SecureModelViewSet):
    queryset=AIProjectInsight.objects.select_related("project").all(); serializer_class=AIProjectInsightSerializer
    @action(detail=False, methods=["post"], url_path="generate/(?P<project_id>[^/.]+)")
    def generate_for_project(self, request, project_id=None):
        project=Project.objects.get(pk=project_id)
        insight=generate_mock_insight(project)
        return Response(self.get_serializer(insight).data)
