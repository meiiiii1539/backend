from rest_framework import serializers
from .models import Product,Cart,Picture

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('pId','name','description','price','brand','age','size','likes')

class CartSerializer(serializers.ModelSerializer):
    pId_name = serializers.CharField(source='pId.name', read_only = True)
    pId_brand = serializers.CharField(source='pId.brand',read_only = True)
    pId_price = serializers.DecimalField(source='pId.price', max_digits=10, decimal_places=2,read_only = True)
    pId_pic = serializers.CharField(source='pId.picture_set.first.picture', read_only = True)
    class Meta:
        model = Cart
        fields='__all__'

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'
