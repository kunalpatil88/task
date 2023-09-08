from django.urls import path
# from .views import PropertyListView
from . import views

urlpatterns = [
    # path('api/properties/', PropertyListView.as_view(), name='property-list'),
    path('api/property-list/', views.PropertyListView.as_view(), name='property-list'),
]
