from django.urls import path
from education import views

urlpatterns = [
    path('', views.CategoriesList.as_view(), name="categories_list"),
]
