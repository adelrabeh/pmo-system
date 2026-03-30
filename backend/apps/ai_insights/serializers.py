from rest_framework import serializers
from .models import AIProjectInsight
class AIProjectInsightSerializer(serializers.ModelSerializer):
    class Meta: model=AIProjectInsight; fields="__all__"
