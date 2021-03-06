from rest_framework.views import APIView
from rest_framework.views import Response
from . import serializers
from labs import models

users = [
    {
        "first_name": "Арутр",
        "last_name": "Артуров",
        "role": "Продавец"
    },
    {
        "first_name": "Идрис",
        "last_name": "Идрисов",
        "role": "Руководитель отдела"
    }
]


class Roles(APIView):
    parser_classes = ()
    authentication_classes = ()

    def get(self, request):
        try:
            user_id = int(request.GET.get('user_id', 0))
        except ValueError as error:
            print(error)
            user_id = 0

        if len(users) > user_id:
            return Response(users[user_id])
        return Response(users[0])


class Professions(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, request):
        professions = models.Profession.objects.all()
        categories = models.ProfessionCategory.objects.all()
        profession_serializer = serializers.ProfessionSerializer(professions, many=True)
        category_serializer = serializers.CategoryOutSerializer(categories, many=True)
        data = {
            "employees": profession_serializer.data,
            "categories": category_serializer.data,
        }
        return Response(data)

    def post(self, request):
        categories = request.data.get('categories')
        employees = request.data.get('employess')
        for category in categories:
            serializer = serializers.CategorySerializer(data=category)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                
        for employee in employees:
            serializer = serializers.ProfessionCountSerializer(data=employee)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        professions = models.Profession.objects.all()
        serializer = serializers.ProfessionSerializer(professions, many=True)
        return Response(serializer.data)
