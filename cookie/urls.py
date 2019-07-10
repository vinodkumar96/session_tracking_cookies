from django.conf.urls import url
from . import views
app_name="cookie"
urlpatterns = [
    url(r'^$', views.input),
    url(r'^add$',views.add),
    url(r'^display$', views.display)
]