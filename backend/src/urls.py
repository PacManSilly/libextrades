from django.views.generic import RedirectView
from django.urls import path, include
from investors.admin import admin_site
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin_site.urls),
    path('', RedirectView.as_view(url=''), name='redirect_to_api'),
    path('api/', include('investors.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)