from rest_framework import serializers
from .models import Multiple, OX

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multiple
        fields = ('title', 'body', 'answer')