from django.urls import path

from common.views import test_view


urlpatterns = [
    path('', test_view),
]
