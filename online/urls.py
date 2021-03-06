from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.ProfileCreate.as_view(), name="register new account"),
    url(r'^login$', views.LoginView.as_view(), name="login user"),
    url(r'^profile$', views.GetUpdateProfileView.as_view(), name="user profile"),
    url(r'^api/courses$', views.course_list),
    url(r'^api/prices$', views.price_list),
    # url(r'^api/songs/(?P<pk>[0-9]+)$', views.tutorial_detail),
]
