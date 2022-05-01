from rest_framework import status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.serializers import ValidationError
from rest_framework.views import exception_handler as drf_exception_handler

from helpers.exceptions import ObjectDoesNotExist, ServiceException
from helpers.response import Response, SingleErrorResponse


def _collect_serializer_error_codes(validation_errors):
    data = validation_errors.get_full_details()

    error_code_list = []
    for field, errors in data.items():
        for error in errors:
            error_code_list.append(error['message'])

    return error_code_list


def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, MethodNotAllowed):
            return SingleErrorResponse(
                error_code='method_not_allowed',
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )

    if isinstance(exc, ValidationError):
        errors = _collect_serializer_error_codes(exc)
        return Response(error=errors, status=status.HTTP_400_BAD_REQUEST)

    if isinstance(exc, ObjectDoesNotExist):
        print(exc)
        return SingleErrorResponse(error_code=f'{exc.cls_name}_does_not_exist', error_value=exc.field_value)

    debug_message = repr(exc)
    exc = ServiceException()
    return Response(
        error=exc.payload,
        debug_message=debug_message,
        status=exc.status_code
    )


