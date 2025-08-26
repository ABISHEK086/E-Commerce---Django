
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from DjangoEcommerceApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admindashboard/', include('DjangoEcommerceApp.adminurls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('upload-profile-picture/', views.upload_profile_picture, name='upload_profile_picture'),
    path('save-system-settings/', views.save_system_settings, name='save_system_settings'),
    path('update-features/', views.update_features, name='update_features'),
    path('update-password/', views.update_password, name='update_password'),
    path('save-security-settings/', views.save_security_settings, name='save_security_settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
