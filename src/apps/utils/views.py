# -*- coding: utf-8 -*-
from rest_framework.views import APIView as RestAPIView
from rest_framework.response import Response
from rest_framework import status


class APIView(RestAPIView):

    def success_action(self, request, serializer):
        return True

    def success_data(self, serializer):
        return serializer.data

    def prepare_data(self, request):
        return request.data

    def post(self, request, *args, **kwargs):
        data = self.prepare_data(request)
        serializer = self.serializer_class(data=data, context=dict(request=request))
        response = {}
        if serializer.is_valid():
            self.success_action(request, serializer)
            response['status'] = 'success'
            response.update(self.success_data(serializer))
            api_status = status.HTTP_200_OK
        else:
            response['status'] = 'fail'
            response['errors'] = serializer.errors
            api_status = status.HTTP_400_BAD_REQUEST
        return Response(response, status=api_status)
