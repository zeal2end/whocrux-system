from django.urls import path
from . import views

app_name = "inception"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("problems/", views.problems, name="problems"),
    path("<int:problem_id>/", views.hiccup, name="hiccup"),
    path("<int:problem_id>/result", views.result, name="result"),
]