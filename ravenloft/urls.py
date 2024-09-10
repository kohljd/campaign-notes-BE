from django.urls import path
from ravenloft import views

urlpatterns = [
    path("realms/", views.RealmList.as_view()),
    path("realms/<int:pk>/", views.RealmDetail.as_view()),
]
