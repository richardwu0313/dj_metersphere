from typing import Dict
from typing import List

from django.db.models import Count
from django.db.models import Q

from dj_metersphere.models.metersphere import Project
from dj_metersphere.models.metersphere import TestCase
from dj_metersphere.models.metersphere import Workspace
from dj_metersphere.models.metersphere import TestCaseNode
from dj_metersphere.models.metersphere import CustomField
from dj_metersphere.models.metersphere import CustomFieldTestCase


class TestCaseUtil:

    @staticmethod
    def get_execution_time_dict(project_id: str) -> Dict:
        # get test case 执行时间( min) field id
        q = Q()
        q.connector = "AND"
        q.children.append(Q(project_id=project_id))
        q.children.append(Q(name="执行时间(min)"))
        q.children.append(Q(scene="TEST_CASE"))
        if CustomField.objects.filter(q).exists():
            field_id = CustomField.objects.filter(q).first().id
        else:
            # project do not have 执行时间( min)
            return {}
        field_id = CustomField.objects.filter(q).first().id
        qs = CustomFieldTestCase.objects.filter(field_id=field_id).values("resource_id", "value")
        result = {}
        for item in qs:
            if item["value"] != "":
                try:
                    try:
                        result[item["resource_id"]] = int(item["value"])
                    except:
                        result[item["resource_id"]] = int(item["value"][1:-1])
                except:
                    result[item["resource_id"]] = 0
            else:
                result[item["resource_id"]] = 0
        return result

    @staticmethod
    def get_test_case(project_id: str):
        q = Q()
        q.connector = "AND"
        q.children.append(Q(project_id=project_id))
        q.children.append(~Q(status="Trash"))
        q.children.append(~Q(node_path__icontains="未规划用例"))
        testcases = TestCase.objects.filter(q)
        return testcases

    @staticmethod
    def get_sw_project_test_case_num():
        q = Q()
        q.connector = "AND"
        q.children.append(~Q(status="Trash"))
        q.children.append(~Q(node_path__icontains="未规划用例"))
        workspace_id = Workspace.objects.filter(name="QA").first().id
        prj_ids = Project.objects.filter(workspace_id=workspace_id, name__startswith="v").values_list("id", flat=True)
        result = TestCase.objects.filter(project_id__in=prj_ids).filter(q).values("project_id").annotate(count=Count("id"))
        return result

    @staticmethod
    def get_sw_project_test_case_time():
        q = Q()
        q.connector = "AND"
        q.children.append(~Q(status="Trash"))
        q.children.append(~Q(node_path__icontains="未规划用例"))
        workspace_id = Workspace.objects.filter(name="QA").first().id
        prj_ids = Project.objects.filter(workspace_id=workspace_id, name__startswith="v").values_list("id", "name")
        prj_id_dict = {}
        for prj_id in prj_ids:
            prj_id_dict[prj_id[0]] = prj_id[1]
        result = {}
        for prj_id in prj_id_dict:
            result[prj_id_dict[prj_id]] = 0
            execution_time_dict = TestCaseUtil.get_execution_time_dict(prj_id)
            if execution_time_dict:
                tcs = TestCase.objects.filter(project_id=prj_id).filter(q)
                for tc in tcs:
                    result[prj_id_dict[prj_id]] += execution_time_dict.get(tc.ref_id, 0)
        return result

    @staticmethod
    def get_automation_status_active(project_id: str) -> Dict:
        assert project_id is not None, "project_id is None"
        tc_count = TestCaseUtil.get_test_case(project_id).count()
        tc_automatable_count = TestCaseUtil.get_test_case(project_id).filter(tags__icontains="automatable").count()
        tc_automated_count = TestCaseUtil.get_test_case(project_id).filter(tags__icontains="automated").count()
        result = {
            "total": tc_count,
            "automatable": tc_automatable_count,
            "automated": tc_automated_count,
        }

        return result

    @staticmethod
    def get_automation_status_detail_active(project_id: str) -> List:
        assert project_id is not None, "project_id is None"
        execution_time_dict = TestCaseUtil.get_execution_time_dict(project_id)
        tcn_q = Q()
        tcn_q.connector = "AND"
        tcn_q.children.append(Q(level=1))
        tcn_q.children.append(~Q(name__icontains="未规划用例"))
        tcn_q.children.append(Q(project_id=project_id))
        root_nodes = TestCaseNode.objects.filter(tcn_q).values_list("name", flat=True)
        tc_q = Q()
        tc_q.connector = "AND"
        tc_q.children.append(Q(project_id=project_id))
        tc_q.children.append(~Q(status="Trash"))
        result = []
        for root_node in sorted(root_nodes):
            qs = TestCase.objects.filter(tc_q).filter(node_path__startswith="/" + root_node)
            total = 0
            total_time = 0
            automatable_count = 0
            automatable_time = 0
            automated_count = 0
            automated_time = 0
            for item in qs:
                if "automatable" in item.tags.lower():
                    automatable_count += 1
                    automatable_time += execution_time_dict.get(item.ref_id, 0)
                if "automated" in item.tags.lower():
                    automated_count += 1
                    automated_time += execution_time_dict.get(item.ref_id, 0)
                total += 1
                total_time += execution_time_dict.get(item.ref_id, 0)
            result.append({
                "feature": root_node,
                "total": total,
                "total_time": total_time,
                "automatable": automatable_count,
                "automatable_percent": str(round(automatable_count * 1.0 / total * 100, 2)) + "%",
                "automatable_time": automatable_time,
                "automatable_time_percent": str(round(automatable_time * 1.0 / total_time * 100, 2)) + "%" if total_time!= 0 else "100%",
                "automated": automated_count,
                "automated_percent": str(round(automated_count * 1.0 / total * 100, 2)) + "%",
                "automated_time": automated_time,
                "automated_time_percent": str(round(automated_time * 1.0 / total_time * 100, 2)) + "%" if total_time!= 0 else "100%",
                "task_percent": str(round(automated_count * 1.0 / automatable_count * 100, 2)) + "%" if automatable_count != 0 else "100%",
                "task_time_percent": str(round(automated_time * 1.0 / automatable_time * 100, 2)) + "%" if automatable_time != 0 else "100%",
            })
        return result

    @staticmethod
    def get_tree_view_by_project_id(project_id: str):
        def get_children(node, q, level: int):
            children = []

            if TestCaseNode.objects.filter(q).filter(level=level + 1, parent_id=node.id).exists():
                for item in TestCaseNode.objects.filter(q).filter(level=level + 1, parent_id=node.id):
                    res = get_children(item, q, level+1)
                    if isinstance(res, dict):
                        children.append(res)
                    else:
                        children.append({
                            "name": item.name,
                            "children": res
                        })
            else:
                return {
                    "name": node.name,
                    "value": TestCase.objects.filter(q).filter(node_id=node.id).count()
                }

            return children
        from dj_metersphere.utils.project_util import ProjectUtil
        q = Q()
        q.connector = "AND"
        q.children.append(~Q(name__icontains="未规划用例"))
        q.children.append(Q(project_id=project_id))
        tree = {}
        level = 1
        project_name = ProjectUtil.get_project_name_by_id(project_id)
        tree["name"] = project_name
        tree["children"] = []
        for node in TestCaseNode.objects.filter(q).filter(level=level):
            tree["children"].append({
                "name": node.name,
                "children": get_children(node, q, level)
            })
        return tree

    @staticmethod
    def get_test_case_priority_dict(project_id: str) -> Dict:
        testcases = TestCaseUtil.get_test_case(project_id)
        result = testcases.values("priority").annotate(count=Count("id"))
        return result

    @staticmethod
    def get_test_case_priority_time_dict(project_id: str) -> Dict:
        testcases = TestCaseUtil.get_test_case(project_id)
        execution_time_dict = TestCaseUtil.get_execution_time_dict(project_id)
        result = {}
        for item in testcases:
            if item.priority not in result:
                result[item.priority] = execution_time_dict.get(item.ref_id, 0)
            else:
                result[item.priority] += execution_time_dict.get(item.ref_id, 0)
        return result

