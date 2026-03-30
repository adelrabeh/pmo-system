from rest_framework.routers import DefaultRouter
from .views import WorkflowTemplateViewSet, WorkflowStepViewSet, WorkflowInstanceViewSet, WorkflowActionViewSet
router=DefaultRouter()
router.register(r"templates", WorkflowTemplateViewSet, basename="workflow-templates")
router.register(r"steps", WorkflowStepViewSet, basename="workflow-steps")
router.register(r"instances", WorkflowInstanceViewSet, basename="workflow-instances")
router.register(r"actions", WorkflowActionViewSet, basename="workflow-actions")
urlpatterns=router.urls
