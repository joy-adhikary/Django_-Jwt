
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Joy(APIView):
    
    greeting = {
            'name': 'joy',
            'greeting': 'hello joy',
            }
    
    def get (self, request):
        print("You hit get method")
        return Response(self.greeting)
    
    def post (self, request):
        print("You hit post method")
        return Response(self.greeting)



class Roy(APIView):

    def get (self, request):
        greeting = {
            'name': 'joy',
            'greeting': 'hello joy',
        }
        return Response(greeting)
    