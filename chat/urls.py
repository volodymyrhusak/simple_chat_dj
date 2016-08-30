from django.conf.urls import url
import views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^post/$', views.post),
    url(r'^login/$', views.login_user),
    url(r'^logout/$', views.logout_user)
]