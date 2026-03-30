from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def json_response(data):
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

def home(request):
    return json_response({"message": "PMO Backend Running 🚀"})

def test_api(request):
    return json_response({"status": "API Working ✅"})

def projects_list(request):
    return json_response({
        "results": [
            {
                "project_code": "42452491",
                "project_name_ar": "تجديد أنظمة التخزين"
            }
        ]
    })

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/test/", test_api),
    path("api/projects/", projects_list),
]
