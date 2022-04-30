from rest_framework import status


class ServiceException(Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'Internal server error'
    code = 'INTERNAL_SERVER_ERROR'
    meta = {}

    def __init__(self, message=None, code=None, errors=None, status_code=None, meta=None):
        if meta:
            self.meta = meta

        if message:
            self.message = message
        if status_code:
            self.status_code = status_code

        self.payload = {
            'message': self.message
        }

        if errors:
            self.payload['errors'] = errors

        if code:
            self.code = code

        if self.code:
            self.payload['code'] = self.code

        super().__init__(self.message)


class ObjectDoesNotExist(Exception):
    HTTP_STATUS_CODE = status.HTTP_404_NOT_FOUND

    def __init__(self, cls_name, **kwargs):
        self.cls_name = cls_name
        self.field_name, self.field_value = kwargs.popitem()

    def __str__(self):
        return f'{self.cls_name} with "{self.field_name}":"{self.field_value}" does not exist'
