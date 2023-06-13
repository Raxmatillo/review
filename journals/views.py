from django.shortcuts import render


from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import JournalSerializer, ArticleSerializer, EditorSerializer, ReferencesSerializer, LanguageSerializer
from .models import Language, Editor, Journal, References, Article
from .permissions import IsOwnerOrReadOnly


class JournalListCreateView(generics.ListCreateAPIView):
	queryset = Journal.objects.all()
	serializer_class = JournalSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


class JournalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Journal.objects.all()
	serializer_class = JournalSerializer
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, ]






class ArticleListCreateView(generics.ListCreateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer




class EditorListCreateView(generics.ListCreateAPIView):
	queryset = Editor.objects.all()
	serializer_class = EditorSerializer


class EditorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Editor.objects.all()
	serializer_class = EditorSerializer




class ReferencesListCreateView(generics.ListCreateAPIView):
	queryset = References.objects.all()
	serializer_class = ReferencesSerializer


class ReferencesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = References.objects.all()
	serializer_class = ReferencesSerializer




class LanguageListCreateView(generics.ListCreateAPIView):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer


class LanguageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer