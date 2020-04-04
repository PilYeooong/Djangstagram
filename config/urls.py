from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.generic import RedirectView
from django_pydenticon.views import image as pydenticon_image
import django_pydenticon.urls


def root(request):
    return render(request, 'root.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('identicon/image/<path:data>/', pydenticon_image, name='pydenticon_image'),
    path('instagram/', include('instagram.urls')),
    path('', login_required(RedirectView.as_view(pattern_name='instagram:index')), name='root'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
