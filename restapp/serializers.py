from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    # class Meta:
    #     model = User
    #     fields = ['id','age','roll']
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    roll = serializers.IntegerField()

    def create(self,validate_data):
        return User.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        print("instance.name")
        instance.name = validated_data.get('name',instance.name)
        print("instance.name")
        instance.roll = validated_data.get('roll',instance.roll)
        instance.age = validated_data.get('age',instance.age)
        instance.save()
        return instance