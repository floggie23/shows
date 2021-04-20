from django.urls import path     
from . import views
urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<str:id>', views.show),
    path('shows/<str:id>/edit', views.edit),
    path('shows/<str:id>/update', views.update),
    path('shows/<str:id>/delete', views.destroy),
]