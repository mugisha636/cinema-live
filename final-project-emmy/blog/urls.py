
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('<int:id>', views.singleBlog),
    path('create', views.create, name="create"),
    path('delete/<int:id>', views.delete, name="delete"),
]
