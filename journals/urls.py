from django.urls import path
from . import views



urlpatterns = [
	path('journal/', views.JournalListCreateView.as_view(), name="journal"),
	path('journal/<int:pk>/', views.JournalRetrieveUpdateDestroyView.as_view(), name='journal_detail'),

	path('article/', views.ArticleListCreateView.as_view(), name='article'),
	path('article/<int:pk>/', views.ArticleRetrieveUpdateDestroyView.as_view(), name='article_detail'),

	path('editor/', views.EditorListCreateView.as_view(), name='editor'),
	path('editor/<int:pk>/', views.EditorRetrieveUpdateDestroyView.as_view(), name='editor_detail'),

	path('language/', views.LanguageListCreateView.as_view(), name='language'),
	path('language/<int:pk>/', views.LanguageRetrieveUpdateDestroyView.as_view(), name='language_detail'),

	path('references/', views.ReferencesListCreateView.as_view(), name='references'),
	path('references/<int:pk>/', views.ReferencesRetrieveUpdateDestroyView.as_view(), name='references_detail')
]