"""
Configuation of all URLs used in resoapp
"""

from django.urls import path

from . import views

app_name = "resoapp"
urlpatterns = [
    path("", views.ResolutionListView.as_view(), name="index"),
    path("<int:pk>/", views.ResolutionView.as_view(), name="resolution"),
]
