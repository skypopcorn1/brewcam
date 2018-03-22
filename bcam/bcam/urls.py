from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^brewpic/', include("brewpic.urls", namespace='brewpic') )
]

# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
