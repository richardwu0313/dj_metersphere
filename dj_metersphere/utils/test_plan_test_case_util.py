from django.db.models import Count
import itertools
from datetime import datetime
from datetime import timedelta
from django.db.models import Q

from fvr_metersphere.models.metersphere import TestPlanTestCase


class FvrTestplanTestcaseUtil:

    @staticmethod
    def get_assignment_summary(testplan_id: str):
        result = (TestPlanTestCase.objects.
                  filter(plan_id=testplan_id).
                  values("executor").
                  annotate(count=Count("id")))
        result = list(result)
        total = 0
        for item in result:
            total += item["count"]
        result_new = {}
        for item in result:
            result_new[item["executor"]] = {
                    "count": item["count"],
                    "percent": round(item["count"] / total * 100, 2),
                }
        return result_new

    @staticmethod
    def get_execution_summary(testplan_id: str):
        result = (TestPlanTestCase.objects.
                  filter(plan_id=testplan_id).
                  values("status").
                  annotate(count=Count("id")))
        result = list(result)
        total = 0
        for item in result:
            total += item["count"]
        result_new = {}
        for item in result:
            result_new[item["status"]] = {
                    "count": item["count"],
                    "percent": round(item["count"] / total * 100, 2),
                }
        return result_new

    @staticmethod
    def get_execution_detail_summary(testplan_id: str):
        statuses = ["Prepare", "Pass", "Failure", "Blocking", "Skip"]
        executors = TestPlanTestCase.objects.filter(plan_id=testplan_id).values_list("executor", flat=True).distinct()
        results = {}
        for per in executors:
            result = TestPlanTestCase.objects.filter(executor=per, plan_id=testplan_id).\
                values("status").annotate(count=Count("id"))
            result_dict = {}
            for item in result:
                result_dict[item["status"]] = item["count"]
            result_dict_new = {}
            for s in statuses:
                if s not in result_dict:
                    result_dict_new[s] = 0
                else:
                    result_dict_new[s] = result_dict[s]
            results[per] = result_dict_new
        return results

    @staticmethod
    def get_daily_execution_summary(testplan_id: str, executor: str = ""):
        from fvr_metersphere.utils.fvr_test_plan_util import FvrTestPlanUtil
        tp_obj = FvrTestPlanUtil.get_test_plan_by_id(testplan_id)
        tp_start_date = datetime.utcfromtimestamp(tp_obj.actual_start_time / 1000).date()
        if tp_obj.actual_end_time:
            tp_end_date = datetime.utcfromtimestamp(tp_obj.actual_end_time / 1000).date()
        else:
            tp_end_date = datetime.today().date()
        q = Q()
        q.connector = "AND"
        q.children.append(("plan_id", testplan_id))
        if executor:
            q.children.append(("executor", executor))
        q.children.append(("status__in", ["Pass", "Failure", "Blocking", "Skip"]))
        testcases = TestPlanTestCase.objects.\
            filter(q).order_by("update_time").values("update_time")
        grouped_tcs = itertools.groupby(testcases, lambda record: datetime.utcfromtimestamp(record["update_time"] / 1000).strftime("%Y-%m-%d"))
        grouped_tcs = {str(day): len(list(tcs_this_day)) for day, tcs_this_day in grouped_tcs}
        day = tp_start_date
        delta = timedelta(days=1)
        while day <= tp_end_date:
            if str(day) not in grouped_tcs:
                grouped_tcs[str(day)] = 0
            day += delta
        grouped_tcs = sorted(grouped_tcs.items(), key=lambda x: x[0])
        result = {}
        for item in grouped_tcs:
            result[item[0]] = item[1]
        return result

    @staticmethod
    def get_daily_execution_detail_summary(testplan_id: str):
        executors = TestPlanTestCase.objects.filter(plan_id=testplan_id).values_list("executor", flat=True).distinct()
        results = {}
        for per in executors:
            result = FvrTestplanTestcaseUtil.get_daily_execution_summary(testplan_id, per)
            results[per] = result
        return results
