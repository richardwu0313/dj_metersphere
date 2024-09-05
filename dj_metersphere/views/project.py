from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from django_filters import rest_framework as filters

from dj_metersphere.serializers.project import ProjectSerializer
from dj_metersphere.models.metersphere import Project
from dj_metersphere.utils.project_util import ProjectUtil


class ProjectFilters(filters.FilterSet):
    class Meta:
        model = Project
        fields = ["workspace_id", "id"]


class ProjectViewSet(ModelViewSet):
    # workspace -> project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("workspace_id", "id")

    @action(detail=False, methods=["get"], url_path="short")
    def short_projects(self, request):
        workspace_id = request.query_params.get("workspace_id", "")
        result = ProjectUtil.get_short_projects(workspace_id)
        return Response(result)
