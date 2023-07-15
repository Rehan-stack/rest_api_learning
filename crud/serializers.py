from rest_framework import serializers
from .models import Article



class Article_serializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','description']




