from rest_framework.response import Response as DrfResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


"""
{
    # Object in case of single instance, Array of objects in case of multiple instances
    "data": {} | [{}, {}], 
    
    "error": [
         # Ex. invalid email pattern
        "code": "4400", 
        "code": "3000",
    ], | 
    "error": [
        {
             # Ex. X not found with the given value
            "code": "6270",
            "value": "1"
        }
    ]
    
    "meta_data": {}
}
"""


class Response(DrfResponse):
    def __init__(self, data=None, meta_data=None, error=None, status=HTTP_200_OK, debug_message=None, **kwargs):

        payload = {}

        if data is not None:
            payload['data'] = data

        if meta_data is not None:
            assert isinstance(meta_data, dict), '"meta_data" is not a "dict" instance'
            payload['meta_data'] = meta_data

        if error is not None:
            payload['error'] = error if isinstance(error, list) else [error]

        if debug_message is not None:
            payload['debug_message'] = debug_message

        super().__init__(payload, status)


class SingleErrorResponse(Response):
    def __init__(self, error_code, error_value=None, status=HTTP_400_BAD_REQUEST):
        error = error_code

        if error_value is not None:
            error = {
                'code': error_code,
                'value': error_value,
            }

        super().__init__(data=None, meta_data=None, error=error, status=status)
