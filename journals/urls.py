from django.urls import path
from . import views



urlpatterns = [

	path('journal/', views.JournalListView.as_view(), name='journal_list'),
	path('journal/new/', views.JournalCreateView.as_view(), name='journal_create'),
	path('journal/<int:pk>/', views.JournalRetrieveView.as_view(), name='journal_detail'),
	path('journal/<int:pk>/update/', views.JournalUpdateView.as_view(), name='journal_update'),
	path('journal/<int:pk>/delete/', views.JournalDestroyView.as_view(), name='journal_delete'),

	path('article/', views.ArticleListView.as_view(), name='article_list'),
	path('article/new/', views.ArticleCreateView.as_view(), name='article_create'),
	path('article/<int:pk>/', views.ArticleRetrieveView.as_view(), name='article_detail'),
	path('article/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
	path('article/<int:pk>/delete/', views.ArticleDestroyView.as_view(), name='article_delete'),

	path('editor/', views.EditorListView.as_view(), name='editor_list'),
	path('editor/new/', views.EditorCreateView.as_view(), name='editor_create'),
	path('editor/<int:pk>/', views.EditorRetrieveView.as_view(), name='editor_detail'),
	path('editor/<int:pk>/update/', views.EditorUpdateView.as_view(), name='editor_update'),
	path('editor/<int:pk>/delete/', views.EditorDestroyView.as_view(), name='editor_delete'),

	path('language/', views.LanguageListCreateView.as_view(), name='language'),
	path('language/<int:pk>/', views.LanguageRetrieveUpdateDestroyView.as_view(), name='language_detail'),

	path('references/', views.ReferencesListView.as_view(), name='references_list'),
	path('references/new/', views.ReferencesCreateView.as_view(), name='references_create'),
	path('references/<int:pk>/', views.ReferencesRetrieveView.as_view(), name='references_detail'),
	path('references/<int:pk>/update/', views.ReferencesUpdateView.as_view(), name='references_update'),
	path('references/<int:pk>/delete/', views.ReferencesDestroyView.as_view(), name='references_delete'),
]