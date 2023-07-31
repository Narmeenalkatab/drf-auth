# from rest_framework import serializers
# from .models import Thing


# class ThingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Thing
#         fields = '__all__'


from rest_framework import serializers

class ExampleSerializer(serializers.Serializer):
    message = serializers.CharField()
