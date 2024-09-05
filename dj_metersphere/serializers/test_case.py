from rest_framework.serializers import SerializerMethodField
from rest_framework.serializers import Serializer
from rest_framework import fields


class TestCaseSerializer(Serializer):
    project_name = SerializerMethodField()
    project_id = fields.CharField()
    count = fields.IntegerField()

    def get_project_name(self, obj):
        return self.context.get("projects").get(obj["project_id"])
