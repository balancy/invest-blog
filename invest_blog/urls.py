import debug_toolbar
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('education.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]