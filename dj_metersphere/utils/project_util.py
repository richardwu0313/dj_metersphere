from typing import Dict

from dj_metersphere.models.metersphere import Project


class ProjectUtil:

    @staticmethod
    def get_projects(workspace_id: str):
        if workspace_id:
            return Project.objects.filter(workspace_id=workspace_id)
        return Project.objects.all()

    @staticmethod
    def get_project_name_by_id(project_id: str):
        prj_obj = Project.objects.get(id=project_id)
        return prj_obj.name

    @staticmethod
    def get_short_projects(workspace_id: str):
        return ProjectUtil.get_projects(workspace_id).values("name", "id")

    @staticmethod
    def get_short_projects_dict(workspace_id: str) -> Dict[str, str]:
        short_projects = ProjectUtil.get_short_projects(workspace_id)
        result = {}
        for item in short_projects:
            result[item["id"]] = item["name"]
        return result


