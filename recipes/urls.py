# recipes/urls.py
# Connect the views to URLs to see the templates in action
from django.urls import path

from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='index'),
    path("", views.RecipeListView.as_view(), name="recipe-list"),
    path("recipe/<int:pk>", views.RecipeDetailView.as_view(),
         name="recipe-detail"),
    path("create", views.RecipeCreateView.as_view(),
         name="recipe-create"),
    path("recipe/<int:pk>/update", views.RecipeUpdateView.as_view(),
         name="recipe-update",
         ),
    path("recipe/<int:pk>/delete", views.RecipeDeleteView.as_view(),
         name="recipe-delete",
         ),
]
