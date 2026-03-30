from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "PMO Backend Running 🚀"})

def test_api(request):
    return JsonResponse({"status": "API Working ✅"})

def projects_list(request):
    return JsonResponse({
        "results": [
            {
                "id": 1,
                "project_code": "42452491",
                "project_name_ar": "تجديد أنظمة التخزين الرئيسية في دارة الملك عبدالعزيز",
                "status_name": "على المسار",
                "phase_name": "البدء",
                "completion_percentage": 48
            }
        ]
    })

def project_detail(request, project_id):
    return JsonResponse({
        "id": project_id,
        "project_code": "42452491",
        "project_name_ar": "تجديد أنظمة التخزين الرئيسية في دارة الملك عبدالعزيز",
        "status_name": "على المسار",
        "phase_name": "البدء",
        "completion_percentage": 48,
        "risks": [
            {"id": 1, "title": "تأخر المورد", "severity_name": "عالٍ"},
            {"id": 2, "title": "نقص التوثيق", "severity_name": "متوسط"}
        ]
    })

def project_dashboard(request, project_id):
    return JsonResponse({
        "project_id": project_id,
        "project_code": "42452491",
        "project_name_ar": "تجديد أنظمة التخزين الرئيسية في دارة الملك عبدالعزيز",
        "completion_percentage": 48,
        "risk_count": 2,
        "issue_count": 1,
        "change_request_count": 0
    })

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/test/", test_api),
    path("api/projects/", projects_list),
    path("api/projects/<int:project_id>/", project_detail),
    path("api/projects/<int:project_id>/dashboard/", project_dashboard),
]
