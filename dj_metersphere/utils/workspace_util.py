from dj_metersphere.models.metersphere import Workspace


class WorkspaceUtil:

    @staticmethod
    def get_workspaces():
        return Workspace.objects.all()

    @staticmethod
    def get_short_workspaces():
        return Workspace.objects.values("name", "id")