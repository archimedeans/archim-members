from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static('/images/', document_root=settings.BASE_DIR / "static/images")
    urlpatterns += static('/lecturenotes/', document_root=settings.BASE_DIR / "static/lecturenotes")
    urlpatterns += static('/files/', document_root=settings.BASE_DIR / "static/files")
    urlpatterns += static('/committees/', document_root=settings.BASE_DIR / "static/committees")
    urlpatterns += static('/data/', document_root=settings.BASE_DIR / "static/data")