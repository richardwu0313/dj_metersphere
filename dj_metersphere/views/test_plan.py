from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from rest_framework.response import Response

from fvr_metersphere.serializers.fvr_test_plan import FvrTestPlanSerializer
from fvr_metersphere.utils.fvr_test_plan_util import FvrTestPlanUtil
from fvr_metersphere.models.metersphere import TestPlan


class FvrTestPlanFilters(filters.FilterSet):
    class Meta:
        model = TestPlan
        fields = ["workspace_id", "project_id", "id"]


class FvrTestPlanViewSet(viewsets.ModelViewSet):
    # workspace -> project -> test plan
    queryset = FvrTestPlanUtil.get_test_plans()
    serializer_class = FvrTestPlanSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("workspace_id", "project_id", "id")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        workspace_id = self.request.query_params.get("workspace_id", "")
        project_id = self.request.query_params.get("project_id", "")
        from fvr_metersphere.models.metersphere import Project
        from django.db.models import Q
        q = Q()
        q.connector = "AND"
        if workspace_id:
            q.children.append(("workspace_id", workspace_id))
        if project_id:
            q.children.append(("project_id", project_id))
        values = Project.objects.filter(q).values("id", "name")
        values_new = {}
        for item in values:
            values_new[item["id"]] = item["name"]
        context.update({
            "pid_pname_mapping": values_new
        })
        return context

    @action(detail=False, methods=["get"], url_path="short")
    def short_test_plans(self, request):
        workspace_id = request.query_params.get("workspace_id", "")
        project_id = request.query_params.get("project_id", "")
        tps = FvrTestPlanUtil.get_short_test_plans_by_workspace_id(workspace_id, project_id)
        return Response(tps)



