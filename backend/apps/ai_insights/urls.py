from rest_framework.routers import DefaultRouter
from .views import AIProjectInsightViewSet
router=DefaultRouter(); router.register(r"insights", AIProjectInsightViewSet, basename="ai-insights")
urlpatterns=router.urls
