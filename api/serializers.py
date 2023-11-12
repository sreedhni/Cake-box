from rest_framework import serializers

from cake.models import User,CakeOccation,CakeVarient,CakeCart,CakeOrder

class UserSerializers(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=["id","username","password","email","phone","adress"]
    def create(self, validated_data):#to hiding the password
        return User.objects.create_user(**validated_data)
    
    
class CartSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    cakename=serializers.CharField(read_only=True)
    username=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    id=serializers.CharField(read_only=True)

    class Meta:
        model=CakeCart
        fields=["cakename","username","status","date","id"]

class CakeVarientSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=CakeVarient
        exclude=("occation",)

    
class CakeOccationSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField(read_only=True)
    # category=serializers.SlugRelatedField(read_only=True,slug_field="name") if there have no __str__ method
    varients=CakeVarientSerializer(many=True,read_only=True)
    class Meta:
        model=CakeOccation
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    username=serializers.CharField(read_only=True)
    cakename=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    orderd_date=serializers.CharField(read_only=True)
    expected_date=serializers.CharField(read_only=True)

    class Meta:

        model=CakeOrder
        fields="__all__"

