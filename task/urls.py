from django.urls import path
from .views import PropertyListView

urlpatterns = [
    path('api/properties/', PropertyListView.as_view(), name='property-list'),
]
