from django.http import Http404

from rest_framework.generics import get_object_or_404 as _drf_get_object_or_404

from helpers.exceptions import ObjectDoesNotExist


def get_object_or_404(cls, **kwargs):
    kwargs_len = len(kwargs)
    assert kwargs_len == 1, f'"get_object_or_404" kwargs should contain only one pair. {kwargs_len} were given'

    try:
        return _drf_get_object_or_404(cls, **kwargs)
    except Http404:
        cls_name = cls.__name__ if isinstance(cls, type) else cls.__class__.__name__
        raise ObjectDoesNotExist(cls_name=cls_name, **kwargs)
