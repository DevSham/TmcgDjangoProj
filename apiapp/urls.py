from django.urls import path
from . import views
urlpatterns = [
    path('', views.listAll, name='list-all'),
    path('deposit/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update-entry'),
]
