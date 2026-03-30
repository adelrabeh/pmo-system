from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectRiskViewSet, ProjectIssueViewSet, ProjectChangeRequestViewSet
router=DefaultRouter()
router.register(r"", ProjectViewSet, basename="projects")
router.register(r"risks", ProjectRiskViewSet, basename="project-risks")
router.register(r"issues", ProjectIssueViewSet, basename="project-issues")
router.register(r"change-requests", ProjectChangeRequestViewSet, basename="project-change-requests")
urlpatterns=router.urls
