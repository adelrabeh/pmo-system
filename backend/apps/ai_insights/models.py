from django.db import models
from django.utils import timezone
from apps.projects.models import Project
class TimestampedModel(models.Model):
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: abstract=True
class AIProjectInsight(TimestampedModel):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name="ai_insights")
    delay_risk_score=models.DecimalField(max_digits=6, decimal_places=2, default=0)
    budget_overrun_risk_score=models.DecimalField(max_digits=6, decimal_places=2, default=0)
    scope_change_risk_score=models.DecimalField(max_digits=6, decimal_places=2, default=0)
    overall_ai_health_score=models.DecimalField(max_digits=6, decimal_places=2, default=0)
    summary_text=models.TextField(blank=True)
    recommended_actions=models.TextField(blank=True)
    model_version=models.CharField(max_length=100, blank=True)
