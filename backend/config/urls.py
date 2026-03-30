from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "PMO Backend Running 🚀"})

def test_api(request):
    return JsonResponse({"status": "API Working ✅"})

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/test/", test_api),
]
