from rest_framework.response import Response
from rest_framework import viewsets, status


class ResponseInfo(object):
    def __init__(self, user=None, **args):
        self.response = {
            "status_code": args.get('status', 'success'),
            "status": args.get('status', 'success'),
            "data": args.get('data', []),
        }


class ResponseModelViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(ResponseModelViewSet, self).__init__(**kwargs)

    def list(self, request, *args, **kwargs):
        response_data = super(ResponseModelViewSet, self).list(request, *args, **kwargs)
        self.response_format["data"] = response_data.data
        self.response_format["status_code"] = response_data.status_code
        if not response_data.data:
            self.response_format["message"] = "List empty"
            self.response_format["data"] = []
        return Response(self.response_format)

    def create(self, request, *args, **kwargs):
        response_data = super(ResponseModelViewSet, self).create(request, *args, **kwargs)
        self.response_format["data"] = response_data.data
        self.response_format["status_code"] = status.HTTP_201_CREATED
        return Response(self.response_format, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        response_data = super(ResponseModelViewSet, self).retrieve(request, *args, **kwargs)
        self.response_format["data"] = response_data.data
        self.response_format["status_code"] = response_data.status_code
        if not response_data.data:
            self.response_format["message"] = "Empty"
        return Response(self.response_format)

    def update(self, request, *args, **kwargs):
        response_data = super(ResponseModelViewSet, self).update(request, *args, **kwargs)
        self.response_format["data"] = response_data.data
        self.response_format["status_code"] = response_data.status_code
        return Response(self.response_format)

    def destroy(self, request, *args, **kwargs):
        response_data = super(ResponseModelViewSet, self).destroy(request, *args, **kwargs)
        self.response_format["data"] = response_data.data
        self.response_format["status_code"] = response_data.status_code
        self.response_format["message"] = "Deleted Done"
        if not response_data.data:
            self.response_format["data"] = []
        return Response(self.response_format)
