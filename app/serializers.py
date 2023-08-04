from rest_framework import serializers
from app.models.test import Test, AlternateName
from app.models.panel import Panel
from app.models.organ import Organ


class AlternateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlternateName
        fields = ['id', 'name']

class TestSerializer(serializers.ModelSerializer):
    alternate_name = AlternateNameSerializer(many=True, read_only=True, source='alternatename_set')
    class Meta:
        model = Test
        fields = ['id', 'panel_id', 'name', 'description', 'info_url', 'normal_reference', 'unit_of_measure', 'alternate_name']

class PanelSerializer(serializers.ModelSerializer):
    tests = TestSerializer(many=True, read_only=True)
    class Meta:
        model = Panel
        fields = ['id', 'name', 'organ_id', 'tests']
        
class OrganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organ
        fields = ['id', 'name']
