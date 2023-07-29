from rest_framework import serializers
from app.models.test import Test, AlternateName
from app.models.panel import Panel
from app.models.organ import Organ


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'panel_id', 'name', 'description', 'info_url', 'normal_reference', 'unit_of_measure']

class AlternateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlternateName
        fields = ['id', 'test_id', 'name']

class PanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = ['id', 'name', 'organ_id']

class OrganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organ
        fields = ['id', 'name']
