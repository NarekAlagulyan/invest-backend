from django.shortcuts import HttpResponse


def test_view(request):
    return HttpResponse('Hello world!')
