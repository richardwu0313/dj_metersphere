from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters

from fvr_metersphere.serializers.fvr_test_plan_test_case import FvrTestplanTestcaseSerializer
from fvr_metersphere.utils.fvr_test_plan_test_case_util import FvrTestplanTestcaseUtil
from fvr_metersphere.models.metersphere import TestPlanTestCase


class FvrTestplanTestcaseFilter(filters.FilterSet):
    testplan_id = filters.CharFilter(field_name="plan_id")

    class Meta:
        model = TestPlanTestCase
        fields = ["testplan_id", "id"]


class FvrTestplanTestcaseViewSet(ModelViewSet):
    queryset = TestPlanTestCase.objects.all()
    serializer_class = FvrTestplanTestcaseSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("testplan_id", "id")

    @action(detail=False, methods=["get"], url_path="assignment_summary")
    def assignment_summary(self, request):
        testplan_id = request.query_params.get("testplan_id", "")
        result = FvrTestplanTestcaseUtil.get_assignment_summary(testplan_id=testplan_id)
        return Response(result)

    @action(detail=False, methods=["get"], url_path="execution_summary")
    def execution_summary(self, request):
        testplan_id = request.query_params.get("testplan_id", "")
        result = FvrTestplanTestcaseUtil.get_execution_summary(testplan_id=testplan_id)
        return Response(result)

    @action(detail=False, methods=["get"], url_path="execution_detail_summary")
    def execution_detail_summary(self, request):
        testplan_id = request.query_params.get("testplan_id", "")
        result = FvrTestplanTestcaseUtil.get_execution_detail_summary(testplan_id=testplan_id)
        return Response(result)

    @action(detail=False, methods=["get"], url_path="daily_execution_summary")
    def daily_execution_summary(self, request):
        testplan_id = request.query_params.get("testplan_id", "")
        result = FvrTestplanTestcaseUtil.get_daily_execution_summary(testplan_id=testplan_id)
        return Response(result)

    @action(detail=False, methods=["get"], url_path="daily_execution_detail_summary")
    def daily_execution_detail_summary(self, request):
        testplan_id = request.query_params.get("testplan_id", "")
        result = FvrTestplanTestcaseUtil.get_daily_execution_detail_summary(testplan_id=testplan_id)
        return Response(result)
