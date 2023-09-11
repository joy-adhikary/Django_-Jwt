from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Joy(APIView):

    def get (self, request):
        greeting = {
            'name': 'joy',
            'greeting': 'hello joy',
        }
        return Response(greeting)
