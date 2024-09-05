from django.db.models import Q
from django.db.models import Count

from fvr_metersphere.models.metersphere import TestPlan


class FvrTestPlanUtil:

    @staticmethod
    def get_test_plans():
        return TestPlan.objects.all()

    @staticmethod
    def get_test_plans_by_workspace_id(workspace_id: str):
        if workspace_id is not None:
            return TestPlan.objects.filter(workspace_id=workspace_id)
        else:
            return TestPlan.objects.all()

    @staticmethod
    def get_test_plan_by_id(id: str):
        return TestPlan.objects.filter(id=id).first()

    @staticmethod
    def get_short_test_plans_by_workspace_id(workspace_id: str, project_id: str):
        q = Q()
        q.connector = "AND"
        if workspace_id:
            q.children.append(("workspace_id", workspace_id))
        if project_id:
            q.children.append(("project_id", project_id))
        return TestPlan.objects.filter(q).order_by("name").values_list("name", "id")
