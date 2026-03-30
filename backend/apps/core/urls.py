from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter()
router.register(r"departments", DepartmentViewSet, basename="departments")
router.register(r"project-statuses", ProjectStatusViewSet, basename="project-statuses")
router.register(r"project-phases", ProjectPhaseViewSet, basename="project-phases")
router.register(r"project-priorities", ProjectPriorityViewSet, basename="project-priorities")
router.register(r"severity-levels", SeverityLevelViewSet, basename="severity-levels")
router.register(r"probability-levels", ProbabilityLevelViewSet, basename="probability-levels")
router.register(r"impact-levels", ImpactLevelViewSet, basename="impact-levels")
router.register(r"change-decision-statuses", ChangeDecisionStatusViewSet, basename="change-decision-statuses")
urlpatterns=router.urls
