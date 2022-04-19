from rest_framework import serializers

from .models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)

    def create(self, validated_data):
        company = Company.objects.create(
            name=validated_data['name'], 
            description=validated_data['description'],
            city=validated_data['city'],
            address=validated_data['address']
        )
        return company
    
    def update(self, instance, validated_data):
        if 'name' in validated_data.keys():
            instance.name = validated_data['name']
        if 'description' in validated_data.keys():
            instance.description = validated_data['description']
        if 'city' in validated_data.keys():
            instance.city = validated_data['city']
        if 'address' in validated_data.keys():
            instance.address = validated_data['address']
        instance.save()
        return instance

class CompanyMSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')

class VacancySerializer(serializers.ModelSerializer):
    # company = serializers.SlugRelatedField(read_only=True, slug_field='company.id')

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary')