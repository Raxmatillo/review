from django.shortcuts import render


from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import JournalSerializer, ArticleSerializer, EditorSerializer, ReferencesSerializer, LanguageSerializer
from .models import Language, Editor, Journal, References, Article
from .permissions import IsOwnerOrReadOnly







class JournalListView(generics.ListAPIView):
	queryset = Journal.objects.all()
	serializer_class = JournalSerializer

class JournalCreateView(generics.CreateAPIView):
	queryset = Journal.objects.all()
	serializer_class = JournalSerializer

class JournalRetrieveView(generics.RetrieveAPIView):
	queryset = Journal.objects.all()
	serializer_class = JournalSerializer

class JournalUpdateView(generics.UpdateAPIView):
	queryset = Journal.objects.all()
	serializer_class = JournalSerializer

class JournalDestroyView(generics.DestroyAPIView):
	queryset = Journal.objects.all()
	serializer_class = JournalSerializer



# Article views

class ArticleListView(generics.ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class ArticleCreateView(generics.CreateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class ArticleRetrieveView(generics.RetrieveAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class ArticleUpdateView(generics.UpdateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class ArticleDestroyView(generics.DestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


# Editor views

class EditorListView(generics.ListAPIView):
	queryset = Editor.objects.all()
	serializer_class = EditorSerializer

class EditorCreateView(generics.CreateAPIView):
	queryset = Editor.objects.all()
	serializer_class = EditorSerializer

class EditorRetrieveView(generics.RetrieveAPIView):
	queryset = Editor.objects.all()
	serializer_class = EditorSerializer

class EditorUpdateView(generics.UpdateAPIView):
	queryset = Editor.objects.all()
	serializer_class = EditorSerializer

class EditorDestroyView(generics.DestroyAPIView):
	queryset = Editor.objects.all()
	serializer_class = EditorSerializer



# References views

class ReferencesListView(generics.ListAPIView):
	queryset = References.objects.all()
	serializer_class = ReferencesSerializer

class ReferencesCreateView(generics.CreateAPIView):
	queryset = References.objects.all()
	serializer_class = ReferencesSerializer

class ReferencesRetrieveView(generics.RetrieveAPIView):
	queryset = References.objects.all()
	serializer_class = ReferencesSerializer

class ReferencesUpdateView(generics.UpdateAPIView):
	queryset = References.objects.all()
	serializer_class = ReferencesSerializer

class ReferencesDestroyView(generics.DestroyAPIView):
	queryset = References.objects.all()
	serializer_class = ReferencesSerializer



# Language View

class LanguageListCreateView(generics.ListCreateAPIView):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer


class LanguageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer