from . import views
from django.urls import path

urlpatterns = [
    path("ind", views.index, name="index"),
    path("scrapper",views.ScrapperViewset.as_view(),name="scrapper"),
    path("register",views.RegisterView.as_view(),name="register"),
    path("alluser",views.AllUserView.as_view(),name='alluser')
]