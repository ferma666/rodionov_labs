from rest_framework.views import APIView
from rest_framework.views import Response
from . import serializers
from labs import models


class Professions(APIView):
    def get(self, request):
        professions = models.Profession.objects.all()
        serializer = serializers.ProfessionSerializer(professions, many=True)
        return Response(serializer.data)

    def post(self, request):
        categories = request.data.get('categories')
        employees = request.data.get('employess')
        for category in categories:
            serializer = serializers.CategorySerializer(data=category)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                
        for employee in employees:
            print(employee)
            serializer = serializers.ProfessionCountSerializer(data=employee)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        professions = models.Profession.objects.all()
        serializer = serializers.ProfessionSerializer(professions, many=True)
        return Response(serializer.data)
