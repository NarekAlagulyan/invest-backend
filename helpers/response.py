from rest_framework.response import Response as DrfResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


"""
{
    # Object in case of single instance, Array of objects in case of multiple instances
    "data": {} | [{}, {}], 
    
    "error": [
        {
            "code": "4400", # The code which describes some kind of error. For example (X does not exist)
            "value": "1" # The actual value which was needed to find X
        },
        {
            "code": "3000",
            "value": "7"
        }
    ],
    
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
    def __init__(self, error_code, error_value, status=HTTP_400_BAD_REQUEST):
        error = {
            'code': error_code,
            'value': error_value
        }
        super().__init__(data=None, meta_data=None, error=error, status=status)
