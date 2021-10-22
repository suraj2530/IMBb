from django.urls  import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('watch/',include('watchlist_app.api.urls'), name='watch'),
    path('account/',include('user_app.api.urls')),

    # path('api-auth/', include('rest_framework.urls'))
]
