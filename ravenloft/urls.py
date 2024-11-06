from django.urls import path
from ravenloft import views

urlpatterns = [
    path("domains/", views.DomainList.as_view()),
    path("domains/<int:pk>/", views.DomainDetail.as_view()),
]
