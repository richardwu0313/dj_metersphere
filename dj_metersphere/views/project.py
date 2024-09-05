from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from django_filters import rest_framework as filters

from fvr_metersphere.serializers.fvr_project import FvrProjectSerializer
from fvr_metersphere.models.metersphere import Project
from fvr_metersphere.utils.fvr_project_util import FvrProjectUtil


class FvrProjectFilters(filters.FilterSet):
    class Meta:
        model = Project
        fields = ["workspace_id", "id"]


class FvrProjectViewSet(ModelViewSet):
    # workspace -> project
    queryset = Project.objects.all()
    serializer_class = FvrProjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("workspace_id", "id")

    @action(detail=False, methods=["get"], url_path="short")
    def short_projects(self, request):
        workspace_id = request.query_params.get("workspace_id", "")
        result = FvrProjectUtil.get_short_projects(workspace_id)
        return Response(result)
