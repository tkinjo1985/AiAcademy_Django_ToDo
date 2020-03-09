from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

# from api.urls import router as api_urls

urlpatterns = [
    path('', include('todo.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include("api.urls")),
    path('api/token/', obtain_jwt_token)
]
