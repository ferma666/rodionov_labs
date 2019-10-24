from rest_framework import serializers
from labs import models


class ProfessionSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # category = serializers.DjangoModelField()

    class Meta:
        model = models.Profession
        depth = 1
        fields = "__all__"
        # fields = ['id', 'name', 'count', 'first_shift_count', 'category_id',]
    # def create(self, validated_data):
    #     profession_data = {
    #         'name': validated_data.get('name'),
    #         'count': validated_data.get('count'),
    #     }
    #     profession_qs = models.Profession.objects.filter(name=profession_data['name'])
    #     if profession_qs.exists():
    #         profession_qs.update(**profession_data)
    #         return profession_qs[0]
    #     else:
    #         return models.Profession.objects.create(**profession_data)


class ProfessionCountSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = models.Profession
        fields = ['id', 'count', 'first_shift_count']

    def save(self):
        validated_data = self.validated_data
        profession = models.Profession.objects.get(id=validated_data.get('id'))
        profession.count = validated_data.get('count', profession.count)
        profession.first_shift_count = validated_data.get('first_shift_count', profession.first_shift_count)
        profession.save()
        return profession
    # def create(self, validated_data):
    #     print(validated_data)
    #
    #
    #     return profession
    #
    #     pass


