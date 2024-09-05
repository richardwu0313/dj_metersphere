from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters import rest_framework as filters

from fvr_metersphere.models.metersphere import TestCase


class FvrTestCaseFilter(filters.FilterSet):
    class Meta:
        model = TestCase
        fields = ["project_id", "id"]


class FvrTestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FvrTestCaseFilter

    def get_serializer_context(self):
        from fvr_metersphere.models.metersphere import Project
        context = super().get_serializer_context()
        prjs = Project.objects.values("id", "name")
        prj_dict = {}
        for prj in prjs:
            prj_dict[prj["id"]] = prj["name"]
        context.update({"projects": prj_dict})
        return context

    @action(detail=False, methods=["get"], url_path="sw/number")
    def case_number_by_sw_projects(self, request, *args, **kwargs):
        from fvr_metersphere.utils.fvr_test_case_util import FvrTestCaseUtil
        from fvr_metersphere.serializers.fvr_test_case import FvrTestCaseSerializer
        result = FvrTestCaseUtil.get_sw_project_test_case_num()
        serializer = FvrTestCaseSerializer(result, many=True, context=self.get_serializer_context())
        serializer.data.sort(key=lambda x: x["project_name"])
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="sw/time")
    def case_time_by_sw_projects(self, request, *args, **kwargs):
        from fvr_metersphere.utils.fvr_test_case_util import FvrTestCaseUtil
        result = FvrTestCaseUtil.get_sw_project_test_case_time()
        return Response(result)

    @action(detail=False, methods=["get"], url_path="sw/priority/number")
    def case_priority_by_sw_projects(self, request, *args, **kwargs):
        from fvr_metersphere.utils.fvr_test_case_util import FvrTestCaseUtil
        project_id = request.query_params.get("project_id")
        result = FvrTestCaseUtil.get_test_case_priority_dict(project_id)
        return Response(result)

    @action(detail=False, methods=["get"], url_path="sw/priority/time")
    def case_priority_time_by_sw_projects(self, request, *args, **kwargs):
        from fvr_metersphere.utils.fvr_test_case_util import FvrTestCaseUtil
        project_id = request.query_params.get("project_id")
        result = FvrTestCaseUtil.get_test_case_priority_time_dict(project_id)
        return Response(result)

    @action(detail=False, methods=["get"], url_path="automation/status/active")
    def automation_status_active(self, request, *args, **kwargs):
        project_id = request.query_params.get("project_id")
        from fvr_metersphere.utils.fvr_test_case_util import FvrTestCaseUtil
        result = FvrTestCaseUtil.get_automation_status_active(project_id)
        return Response(result)

    @action(detail=False, methods=["get"], url_path="automation/status/detail/active")
    def automation_status_detail_active(self, request, *args, **kwargs):
        project_id = request.query_params.get("project_id")
        from fvr_metersphere.utils.fvr_test_case_util import FvrTestCaseUtil
        result = FvrTestCaseUtil.get_automation_status_detail_active(project_id)
        return Response(result)

    @action(detail=False, methods=["get"], url_path="automation/status/trend")
    def automation_status_trend(self, request, *args, **kwargs):
        pass

    @action(detail=False, methods=["get"], url_path="tree")
    def case_tree(self, request, *args, **kwargs):
        from fvr_metersphere.utils.fvr_test_case_util import FvrTestCaseUtil
        project_id = request.query_params.get("project_id")
        result = FvrTestCaseUtil.get_tree_view_by_project_id(project_id)
        return Response(result)



