from django.contrib import admin
from django.urls import path,include
import products.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',products.views.home,name="home"),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
