from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from rest_framework import permissions

from dj_metersphere.views.workspace import WorkspaceViewSet
from dj_metersphere.views.test_plan import TestPlanViewSet
from dj_metersphere.views.project import ProjectViewSet
from dj_metersphere.views.test_plan_test_case import TestplanTestcaseViewSet
from dj_metersphere.views.test_case import TestCaseViewSet

router = DefaultRouter()
router.register("workspaces", WorkspaceViewSet, basename="workspaces")
router.register("testplans", TestPlanViewSet, basename="testplans")
router.register("projects", ProjectViewSet, basename="projects")
router.register("testplan_testcases", TestplanTestcaseViewSet, basename="testplan_testcases")
router.register("testcases", TestCaseViewSet, basename="testcases")
urlpatterns = router.urls

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version="v1",
      description="metersphere api based on django",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns.extend([
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

])