from rest_framework.serializers import ModelSerializer

from dj_metersphere.models.metersphere import Workspace


class WorkspaceSerializer(ModelSerializer):

    class Meta:
        model = Workspace
        fields = "__all__"
