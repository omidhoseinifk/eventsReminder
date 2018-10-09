from django.conf.urls import url
from . import views

app_name = 'reminderApp'

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
]
