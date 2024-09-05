from datetime import datetime

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from fvr_metersphere.models.metersphere import TestPlan


class FvrTestPlanSerializer(ModelSerializer):
    project_name = serializers.SerializerMethodField()
    create_time_str = serializers.SerializerMethodField()
    update_time_str = serializers.SerializerMethodField()
    planned_start_time_str = serializers.SerializerMethodField()
    planned_end_time_str = serializers.SerializerMethodField()
    actual_start_time_str = serializers.SerializerMethodField()
    actual_end_time_str = serializers.SerializerMethodField()

    def get_project_name(self, obj):
        return self.context["pid_pname_mapping"][obj.project_id]

    def get_create_time_str(self, obj):
        if obj.create_time:
            return datetime.fromtimestamp(obj.create_time / 1000).strftime("%Y-%m-%d %H:%M:%S")
        return ""

    def get_update_time_str(self, obj):
        if obj.update_time:
            return datetime.fromtimestamp(obj.update_time / 1000).strftime("%Y-%m-%d %H:%M:%S")
        return ""

    def get_planned_start_time_str(self, obj):
        if obj.planned_start_time:
            return datetime.fromtimestamp(obj.planned_start_time / 1000).strftime("%Y-%m-%d %H:%M:%S")
        return ""

    def get_planned_end_time_str(self, obj):
        if obj.planned_end_time:
            return datetime.fromtimestamp(obj.planned_end_time / 1000).strftime("%Y-%m-%d %H:%M:%S")
        return ""

    def get_actual_start_time_str(self, obj):
        if obj.actual_start_time:
            return datetime.fromtimestamp(obj.actual_start_time / 1000).strftime("%Y-%m-%d %H:%M:%S")
        return ""

    def get_actual_end_time_str(self, obj):
        if obj.actual_end_time:
            return datetime.fromtimestamp(obj.actual_end_time / 1000).strftime("%Y-%m-%d %H:%M:%S")
        return ""

    class Meta:
        model = TestPlan
        fields = ["id", "project_name", "name", "creator", "status", "stage", "create_time_str",
                  "update_time_str", "planned_start_time_str", "planned_end_time_str",
                  "actual_start_time_str", "actual_end_time_str"]
