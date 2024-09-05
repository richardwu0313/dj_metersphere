from rest_framework.serializers import ModelSerializer

from dj_metersphere.models.metersphere import Project


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"
