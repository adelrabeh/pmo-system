from apps.projects.models import Project
from .models import AIProjectInsight

def generate_mock_insight(project: Project):
    risk_count = project.risks.count(); issue_count = project.issues.count()
    delay_score=min(100, (risk_count*15)+(issue_count*10))
    overall=round((delay_score+20+25)/3,2)
    return AIProjectInsight.objects.create(project=project, delay_risk_score=delay_score, budget_overrun_risk_score=20, scope_change_risk_score=25, overall_ai_health_score=overall, summary_text=f"المشروع يحتوي على {risk_count} مخاطر و {issue_count} تحديات.", recommended_actions="مراجعة المعالم المتأخرة.", model_version="mock-v1")
