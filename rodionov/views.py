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
        for item in request.data:
            print(item)
            serializer = serializers.ProfessionCountSerializer(data=item)
            if serializer.is_valid(raise_exception=True):
                profession = serializer.save()

        professions = models.Profession.objects.all()
        serializer = serializers.ProfessionSerializer(professions, many=True)
        return Response(serializer.data)

    #
    # def post(self, request):
    #     if
