from rest_framework import serializers
from labs import models


class ProfessionSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # category = serializers.DjangoModelField()

    class Meta:
        model = models.Profession
        depth = 1
        fields = "__all__"


class CategoryOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfessionCategory
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

    class Meta:
        model = models.Profession
        fields = ['count', 'category', 'name', 'first_shift_count']

    category = serializers.JSONField(required=False, allow_null=True)

    def save(self):
        validated_data = self.validated_data
        profession_qs = models.Profession.objects.filter(name=validated_data.get('name'))
        category = validated_data.get('category')

        if category:
            category = models.ProfessionCategory.objects.get(name=category.get('name'))
        else:
            category = None

        if profession_qs.exists():
            profession = profession_qs[0]
            profession.count = validated_data.get('count', profession_qs[0].count)
            profession.first_shift_count = validated_data.get('first_shift_count',
                                                                    profession_qs[0].first_shift_count)
            profession.name = validated_data.get('name', profession_qs[0].name)

            profession.category = category

            profession.save()
            print(60, profession.count)
            profession = profession_qs[0]

        else:
            del validated_data['category']
            validated_data['category'] = category
            profession = models.Profession.objects.create(**validated_data)

        return profession


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfessionCategory
        fields = ['name']

    def save(self):
        validated_data = self.validated_data
        category_qs = models.ProfessionCategory.objects.filter(name=validated_data.get('name'))
        if category_qs.exists():
            category_qs[0].name = validated_data.get('name', category_qs[0].name)
            category_qs[0].save()
            category = category_qs[0]
        else:
            category = models.ProfessionCategory.objects.create(**validated_data)

        return category


