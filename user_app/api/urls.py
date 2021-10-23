from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app.api.views import registration_view , logout_view
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    # path('login/', obtain_auth_token, name='login'),  # for tokrn suth not JWT 
    path('register/', registration_view, name='register'),# don't add '' in registration_view else big error 
    # path('logout/', logout_view, name='logout'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # for JWT token login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]

