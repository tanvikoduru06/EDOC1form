from django.conf.urls import url
from credits import views

urlpatterns = [
    url(r'^$',views.users,name='users'),
]