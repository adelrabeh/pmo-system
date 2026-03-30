from rest_framework.decorators import action
from rest_framework.response import Response
from common.mixins import SecureModelViewSet
from .models import WorkflowTemplate, WorkflowStep, WorkflowInstance, WorkflowAction
from .serializers import WorkflowTemplateSerializer, WorkflowStepSerializer, WorkflowInstanceSerializer, WorkflowActionSerializer
from .services import approve_workflow_step
class WorkflowTemplateViewSet(SecureModelViewSet): queryset=WorkflowTemplate.objects.prefetch_related("steps").all(); serializer_class=WorkflowTemplateSerializer
class WorkflowStepViewSet(SecureModelViewSet): queryset=WorkflowStep.objects.all(); serializer_class=WorkflowStepSerializer
class WorkflowInstanceViewSet(SecureModelViewSet):
    queryset=WorkflowInstance.objects.prefetch_related("actions").all(); serializer_class=WorkflowInstanceSerializer
    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):
        updated=approve_workflow_step(self.get_object(), request.user, request.data.get("comments", ""))
        return Response(WorkflowInstanceSerializer(updated).data)
class WorkflowActionViewSet(SecureModelViewSet): queryset=WorkflowAction.objects.all(); serializer_class=WorkflowActionSerializer
