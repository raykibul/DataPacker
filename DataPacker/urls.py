
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('labibvai/', admin.site.urls),
    path('', include('auth.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
