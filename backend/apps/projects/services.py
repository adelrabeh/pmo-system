from .models import Project

def project_dashboard_payload(project: Project) -> dict:
    return {
        "project_id": project.id,
        "project_code": project.project_code,
        "project_name_ar": project.project_name_ar,
        "status": project.status.name_ar,
        "phase": project.phase.name_ar,
        "completion_percentage": float(project.completion_percentage),
        "risk_count": project.risks.count(),
        "issue_count": project.issues.count(),
        "change_request_count": project.change_requests.count(),
        "budget_count": project.budgets.count(),
    }
