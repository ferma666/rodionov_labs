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
        serializer = serializers.ProfessionCountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            profession = serializer.save()
            return Response(profession.get_data())
        else:
            return Response("ERROR")

    #
    # def post(self, request):
    #     if
