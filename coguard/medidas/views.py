from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


class MedidasAPI(APIView):
    def get(self, request):



        return Response({"su": "su"}, '200')
