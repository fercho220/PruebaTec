from rest_framework import serializers
from productos.models import Producto

class serializersProducts(serializers.HyperlinkedModelSerializer):
    nombre = serializers.CharField(max_length=100)
    precio = serializers.DecimalField(max_digits=8, decimal_places=2)
    descripcion = serializers.CharField(max_length=500)
    class Meta:
        model = Producto
        fields = [ 'nombre', 'precio', 'descripcion' ]

class serializersProductsUpdate(serializers.HyperlinkedModelSerializer):
     class Meta:
         model = Producto
         fields = [ 'nombre', 'precio', 'descripcion' ]
     def update(self, instance,validated_data):
         instance.nombre=validated_data['nombre']
         instance.precio=validated_data['precio']
         instance.descripcion=validated_data['descripcion']
         instance.save()
         return instance

class ViewProductSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = [ 'nombre', 'precio', 
                  'descripcion']

class serializersAllProducts(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"