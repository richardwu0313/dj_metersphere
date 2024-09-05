from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from datetime import datetime

from dj_metersphere.models.metersphere import TestPlanTestCase


class TestplanTestcaseSerializer(ModelSerializer):
    create_time_str = serializers.SerializerMethodField()
    update_time_str = serializers.SerializerMethodField()

    def get_create_time_str(self, obj):
        if obj.create_time:
            return datetime.fromtimestamp(obj.create_time / 1000).strftime("%Y-%m-%d %H:%M:%S")
        return ""

    def get_update_time_str(self, obj):
        if obj.update_time:
            return datetime.fromtimestamp(obj.update_time / 1000).strftime("%Y-%m-%d %H:%M:%S")
        return ""

    class Meta:
        model = TestPlanTestCase
        fields = "__all__"
