from django.conf.urls import include, url
from . import views

app_name = 'brewpic'

urlpatterns = [
	url(r'^upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view(), name='upload')
    ]
