from rest_framework.serializers import ModelSerializer

from fvr_metersphere.models.metersphere import Workspace


class FvrWorkspaceSerializer(ModelSerializer):

    class Meta:
        model = Workspace
        fields = "__all__"
