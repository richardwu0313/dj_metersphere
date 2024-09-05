from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from dj_metersphere.serializers.workspace import WorkspaceSerializer
from dj_metersphere.utils.workspace_util import WorkspaceUtil


class WorkspaceViewSet(ModelViewSet):
    # workspace
    queryset = WorkspaceUtil.get_workspaces()
    serializer_class = WorkspaceSerializer

    @action(detail=False, methods=["get"], url_path="short")
    def short_workspaces(self, request):
        result = WorkspaceUtil.get_short_workspaces()
        return Response(result)
