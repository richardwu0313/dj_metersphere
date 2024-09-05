from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from fvr_metersphere.serializers.fvr_workspace import FvrWorkspaceSerializer
from fvr_metersphere.utils.fvr_workspace_util import FvrWorkspaceUtil


class FvrWorkspaceViewSet(ModelViewSet):
    # workspace
    queryset = FvrWorkspaceUtil.get_workspaces()
    serializer_class = FvrWorkspaceSerializer

    @action(detail=False, methods=["get"], url_path="short")
    def short_workspaces(self, request):
        result = FvrWorkspaceUtil.get_short_workspaces()
        return Response(result)
