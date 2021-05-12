from rest_framework import serializers
from materials.models import Material



class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        exclude = []
