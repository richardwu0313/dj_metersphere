from rest_framework.serializers import ModelSerializer

from fvr_metersphere.models.metersphere import Project


class FvrProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"
