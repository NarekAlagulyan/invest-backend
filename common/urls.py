from django.urls import path

from common.views import UserViewSet


urlpatterns = [
    path('', UserViewSet.as_view({
        'post': 'create',
    })),
    path('<str:username>/', UserViewSet.as_view({
        'get': 'retrieve',
    }))
]
