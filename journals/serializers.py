from rest_framework import serializers

from .models import Language, Editor, Journal, References, Article


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = "__all__"
        depth = 2


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article 
        fields = "__all__"
        depth = 2


class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = "__all__"
        depth = 2

class ReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = References
        fields = "__all__"

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"
